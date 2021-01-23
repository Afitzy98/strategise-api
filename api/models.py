import json
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from .constants import DEFAULT_FAVOURITES, PaymentStatus
from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    favourites = Column(String, unique=False, default=json.dumps(DEFAULT_FAVOURITES))
    payment_status = Column(String, default=PaymentStatus.PENDING)
    stripe_customer_id = Column(String, unique=True)
