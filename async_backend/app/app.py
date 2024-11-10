import asyncio
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal, init_db
from .models import GroundsForUnpublishing
from .schemas import GroundCreate, Ground, TenderURL
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
from .services import get_tender_data, download_document, parse_docx, parse_pdf, check_compliance
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники. В продакшене стоит указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы (POST, GET, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешает все заголовки
)

@app.on_event("startup")
async def startup_event():
    await init_db()

async def get_db():
    async with SessionLocal() as session:
        yield session

# @app.post("/grounds/", response_model=Ground)
# async def create_ground(ground: GroundCreate, db: AsyncSession = Depends(get_db)):
#     db_ground = GroundsForUnpublishing(**ground.dict())
#     db.add(db_ground)
#     await db.commit()
#     await db.refresh(db_ground)
#     return db_ground

# @app.get("/grounds/{ground_id}", response_model=Ground)
# async def get_ground(ground_id: int, db: AsyncSession = Depends(get_db)):
#     ground = await db.get(GroundsForUnpublishing, ground_id)
#     if not ground:
#         raise HTTPException(status_code=404, detail="Ground not found")
#     return ground

# @app.post("/api/tender/", response_model=dict)
# async def process_tender(data: TenderURL):
#     session_info, file_urls = await get_tender_data(str(data.url))
#     answers = []
    
#     # Создаем папку для документов
#     os.makedirs("documents", exist_ok=True)

#     for doc_url, doc_name in file_urls:
#         save_path = f"documents/{doc_name}"
#         await download_document(doc_url, save_path)
#         if save_path.endswith(".docx"):
#             doc_text = parse_docx(save_path)
#         elif save_path.endswith(".pdf"):
#             doc_text = parse_pdf(save_path)
#         answer = await check_compliance(session_info, doc_text)
#         answers.append(answer)
#     return {"answers": "\n".join(answers)}

@app.get("/api/tender-stream/")
async def process_tender_stream(url: str):
    async def generate_response():
        # Шаг 1: Получаем session_info и ссылки на документы
        session_info, file_urls = await get_tender_data(url)
        
        print(session_info)
        
        # Отправляем session_info сразу после получения
        yield f"data: Session Info: {session_info}\n\n"

        # Создаем папку для документов
        os.makedirs("documents", exist_ok=True)

        # Шаг 2: Обрабатываем каждый документ по очереди и отправляем результаты проверки
        for doc_url, doc_name in file_urls:
            save_path = f"documents/{doc_name}"
            await download_document(doc_url, save_path)

            # Извлекаем текст документа в зависимости от типа файла
            if save_path.endswith(".docx"):
                doc_text = parse_docx(save_path)
            elif save_path.endswith(".pdf"):
                doc_text = parse_pdf(save_path)

            # Проверка на соответствие и отправка результата
            answer = await check_compliance(session_info, doc_text)
            yield f"data: Answer for {doc_name}: {answer}\n\n"
            await asyncio.sleep(0.1)  # Небольшая задержка для обеспечения потоковой передачи

    return StreamingResponse(generate_response(), media_type="text/event-stream")