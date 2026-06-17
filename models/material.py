from sqlalchemy import Column, Integer, String
from constants.constants import TABLE_MATERIALS
from database import Base

class Material(Base):
    __tablename__ = TABLE_MATERIALS

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    quantity = Column(Integer)
    location = Column(String(100))