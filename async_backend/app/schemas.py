from pydantic import BaseModel, HttpUrl


class GroundBase(BaseModel):
    reason: str
    description: str

class GroundCreate(GroundBase):
    pass

class Ground(GroundBase):
    id: int
    class Config:
        orm_mode = True

class TenderURL(BaseModel):
    url: HttpUrl
