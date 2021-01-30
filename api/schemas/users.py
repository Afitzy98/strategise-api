from typing import List, Optional
from pydantic import BaseModel

from ..constants import PaymentStatus

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    favourites: str
    is_active: bool
    payment_status: PaymentStatus
    stripe_customer_id: str = None

    class Config:
        orm_mode = True
