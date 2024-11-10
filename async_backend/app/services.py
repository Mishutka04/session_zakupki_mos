import httpx
import re
from bs4 import BeautifulSoup
from docx import Document
import fitz  # для работы с PDF
import os
from gradio_client import Client


client = Client("https://qwen-qwen2-72b-instruct.hf.space/")

async def get_tender_data(url: str):
    auction_id = re.search(r'auction/(\d+)', url)
    if not auction_id:
        return None
    auction_id = auction_id.group(1)
    api_url = f"https://zakupki.mos.ru/newapi/api/Auction/Get?auctionId={auction_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        data = response.json()

        session_info = {
            "customer": data["customer"]["name"],
            "state": data["state"]["name"],
            "startCost": data["startCost"],
            "items": [
                {
                    "name": item["name"],
                    "currentValue": item["currentValue"],
                    "okeiName": item["okeiName"],
                    "costPerUnit": item["costPerUnit"]
                } for item in data["items"]
            ]
        }
        
        file_urls = [(f"https://zakupki.mos.ru/newapi/api/FileStorage/Download?id={file['id']}", file['name']) for file in data.get("files", [])]
        
    return session_info, file_urls

async def download_document(doc_url: str, save_path: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(doc_url)
        with open(save_path, 'wb') as file:
            file.write(response.content)

def parse_docx(doc_path: str) -> str:
    doc = Document(doc_path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

async def check_compliance(session_info: dict, doc_text: str) -> str:
    session_description = f"Закупка: {session_info['customer']}, начальная стоимость: {session_info['startCost']}.\n" \
                          "Товары:\n" + \
                          "\n".join(f"- {item['name']}: {item['currentValue']} {item['okeiName']} по {item['costPerUnit']} руб."
                                    for item in session_info['items'])
    
    prompt = f"""
    Проверьте соответствие спецификации закупки данным из документа.
    Данные из карточки тендера: {session_description}
    Данные из документа: {doc_text}
    """
    return client.predict(prompt, [["None", "None"]], "None", api_name="/model_chat")[1][1][1]
