from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

import enums

class Category(BaseModel):
    name: str = None
    description: str = None
    class Config:
        orm_mode = True

class CategoryOut(Category):
    id: int = None

class Policy(BaseModel):
    name: str = Field(...)
    type: enums.PolicyType = None
    issue: int = None
   #categories: List[int] = []
    description: str = None
    example: str = None
    signature_id: int = None
   #files_list: List[int] = []
   #active: bool = False


class PolicyOut(Policy):
    id: int = None
   #categories: List[Category] = []
    ts_added: datetime = datetime.now()


class Option(BaseModel):
    id: int = None
    key: enums.SignatureKeys = enums.SignatureKeys.engine
    value: str = '81-255'

class Subsign(BaseModel):
    id: int = None
    type: enums.SubSignType =  enums.SubSignType.hex
    value: str = '3c3f706870'

class Signature(BaseModel):
    options: List[int] = None
    subsigns: List[int] = None
    logic: str = '1'

class File(BaseModel):
    pass
