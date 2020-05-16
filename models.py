from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Policy(Base):
    __tablename__ = 'policies'
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    description = Column(String, index=True)
   #signature = Column(Integer, ForeignKey("signature.id"))
