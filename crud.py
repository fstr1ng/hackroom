from sqlalchemy.orm import Session

import models, schemas

def get_object(db: Session, model, id: int):
    return db.query(model).filter(model.id == id).first()


#def get_items(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.Item).offset(skip).limit(limit).all()
