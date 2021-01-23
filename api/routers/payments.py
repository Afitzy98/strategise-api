import json
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List, Optional


from .. import models
from ..context import get_current_active_user, authenticate_user, create_access_token
from ..crud import payments as crud
from ..schemas import users as schemas


router = APIRouter(
    prefix="/payments",
    tags=["payments"],
    responses={404: {"description": "Not found"}},
)


@router.get("/create-checkout-session")
def create_checkout_session(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return crud.create_checkout_session()


@router.get("/customer-portal")
def customer_portal(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return crud.create_checkout_session(current_user.stripe_customer_id)
