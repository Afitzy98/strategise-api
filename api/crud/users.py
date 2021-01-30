from sqlalchemy.orm import Session

from .. import models
from ..schemas import users as schemas
from ..utils import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_stripe_id(db: Session, stripe_id: str):
    return db.query(models.User).filter(models.User.stripe_customer_id == stripe_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()


def update_user(db: Session, updated_user: schemas.User):
    user = get_user(db, updated_user.id)
    user = updated_user
    db.commit()
    return user
