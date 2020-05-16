import pdb
from enum import Enum
from typing import List, Set
from datetime import datetime

from fastapi import FastAPI, Query, Path, Body, Depends
from sqlalchemy.orm import Session

import enums, models, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from schemas import (
    Category, CategoryOut,
    Policy,   PolicyOut,
    File,
    Signature,
    Subsign,
    Option,
    )

model_values = [
    ('category',  Category,  CategoryOut),
    ('policy',    Policy,    PolicyOut),
    ('file',      File,      File),
    ('signature', Signature, Signature),
    ('subsign',   Subsign,   Subsign),
    ('option',    Option,    Option),
]

model_maps = [{'name':i[0], 'input':i[1], 'output':i[2]} for i in model_values]
model_names = [i[0] for i in model_values]
ModelNames = Enum('ModelNames', {n:n for n in model_names}, type=str)

# Dependensy
async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Dependensy
async def get_model_map(model_name: ModelNames):
    return [d for d in model_maps if (d['name'] == model_name.value)][0]

@app.get('/{model_name}/')
async def get_objects(model_map: dict = Depends(get_model_map), db: Session = Depends(get_db)):
   db_user = crud.get_object(db, models.Category, 1)
   return response

#@app.get('/{model_name}/{id}')
#async def get_object(id: int, model_map: dict = Depends(get_model_map)):
#    model = model_map['name']
#    [data] = db.read(model, id=id)
#    object = model_map['output'](**data)
#    response = {model: object}
#    return response
#
#@app.post('/{model_name}/')
#async def create_object(model_map: dict = Depends(get_model_map), data = Body(...)):
#    object = model_map['input'](**data)
#    db.update(model_map['name'], object.dict())
#    return model_map['output'](**data)
#
#@app.put('/{model_name}/{id}')
#async def update_object(id: int, model_map: dict = Depends(get_model_map), data = Body(...)):
#    object = model_map['input'](**data)
#    db.update(model_map['name'], object.dict(), id=id)
#    return model_map['output'](**data)
#    
#@app.get(
#    '/policy/',
#    tags=['policy'])
#async def get_policies(
#        t: List[enums.PolicyType] = Query(default = None, alias = 'type'),
#        c: List[int] = Query(default = None, alias = 'category')
#        ):
#    if t:
#        return [p for p in db.read('policy') if p["type"] == t] 
#    else:
#        return db.read('policy')
#
#@app.get(
#    '/policy/{id}',
#    tags=['policy'],
#    response_model=PolicyOut)
#async def get_policy(policy_id: int = Path(..., alias = 'id', ge=0)):
#    for p in db.read('policy'):
#        if p['id'] == policy_id:
#            categories_out = [c for c in db.read('policy') if c['id'] in p['categories']]
#            p['categories'] = categories_out
#            return p
#
##@app.post(
##    '/policy/',
##    tags=['policy'])
##async def create_policy(policy: Policy):
##    now = datetime.now()
##    result = Policy(**policy.dict(), ts_added=now, ts_updated=now)
##    db.update('policy', result.dict())
##    return result
#
