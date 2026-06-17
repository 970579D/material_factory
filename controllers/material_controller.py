from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from constants.constants import API_PREFIX_MATERIALS, API_TAGS_MATERIALS, MESSAGE_SUCCESS
from database import SessionLocal
from models.response import BaseResponse
from schemas.material import (
    MaterialCreate,
    MaterialResponse
)
from services.material_service import MaterialService

router = APIRouter(prefix=API_PREFIX_MATERIALS, tags=API_TAGS_MATERIALS)
service = MaterialService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=BaseResponse[List[MaterialResponse]])
def get_materials(db: Session = Depends(get_db)):
    return BaseResponse(message=MESSAGE_SUCCESS, data=service.get_all(db))


@router.get("/{material_id}",
            response_model=BaseResponse[MaterialResponse])
def get_material(material_id: int,
                 db: Session = Depends(get_db)):
    return BaseResponse(message=MESSAGE_SUCCESS, data=service.get_by_id(db, material_id))


# @router.post("/", response_model=MaterialResponse)
# def create_material(material: MaterialCreate,
#                     db: Session = Depends(get_db)):
#     return service.create(db, material)


@router.post("/", response_model=BaseResponse[List[MaterialResponse]])
def create_materials(materials: List[MaterialCreate], 
                     db: Session = Depends(get_db)):
    return BaseResponse(message=MESSAGE_SUCCESS, data=service.create_list(db, materials))