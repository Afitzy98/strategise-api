import json
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Header, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any

from .. import models
from ..constants import PaymentStatus, WebhookEvent
from ..context import get_current_active_user, authenticate_user, create_access_token
from ..crud import payments as crud
from ..crud import users as users_crud
from ..dependencies import get_db
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
    return crud.create_checkout_session(current_user.id)


@router.get("/customer-portal")
def customer_portal(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return crud.create_customer_portal(current_user.stripe_customer_id)


@router.post("/hooks")
async def stripe_webhook(
    request: Request,
    stripe_signature: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    try:
        body = await request.body()
        event = crud.construct_webhook_event(body, stripe_signature)

        event_type = event["type"]
        print(f"[SERVER] Incoming Stripe {event_type} Event")
        if event_type == WebhookEvent.CHECKOUT_SESSION_COMPLETED:
            # payment completed so set payment status for current user to paid
            session = event["data"]["object"]
            user_id = int(session["metadata"]["userId"])
            stripe_id = session["customer"]

            user = users_crud.get_user(db, user_id)

            user.stripe_customer_id = stripe_id
            user.payment_status = PaymentStatus.PAID

            users_crud.update_user(db, user)

        if event_type == WebhookEvent.INVOICE_PAYMENT_FAILED:
            # payment failed so set the payment status for the current user to failed
            stripe_id = event["data"]["object"]["customer"]

            user = users_crud.get_user_by_stripe_id(db, stripe_id)

            user.payment_status = PaymentStatus.FAILED

            users_crud.update_user(db, user)

        if event_type == WebhookEvent.INVOICE_PAID:
            stripe_id = event["data"]["object"]["customer"]

            user = users_crud.get_user_by_stripe_id(db, stripe_id)

            if user is not None:
                user.payment_status = PaymentStatus.PAID

                users_crud.update_user(db, user)

        if event_type == WebhookEvent.CUSTOMER_SUBSCRIPTION_DELETED:
            stripe_id = event["data"]["object"]["customer"]

            user = users_crud.get_user_by_stripe_id(db, stripe_id)

            user.payment_status = PaymentStatus.CANCELLED

            users_crud.update_user(db, user)

        if event_type == WebhookEvent.INVOICE_CREATED:
            stripe_id = event["data"]["object"]["customer"]

            user = users_crud.get_user_by_stripe_id(db, stripe_id)

            if user is not None:
                user.payment_status = PaymentStatus.RENEWING

                users_crud.update_user(db, user)

        return json.dumps({"status": "success"})

    except Exception as e:
        print(e)  # remove
        return e