from pydantic import BaseModel

class MaterialCreate(BaseModel):
    name: str
    quantity: int
    location: str


class MaterialResponse(MaterialCreate):
    id: int

    class Config:
        from_attributes = True