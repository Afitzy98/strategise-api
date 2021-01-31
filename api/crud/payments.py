import stripe

from config import (
    STRIPE_SECRET_KEY,
    STRIPE_SUB_PRICE_ID,
    REDIRECT_URL,
    STRIPE_WEBHOOK_SECRET,
)

stripe.api_key = STRIPE_SECRET_KEY


def create_checkout_session(user_id: int):
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=REDIRECT_URL + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=REDIRECT_URL + "login",
            payment_method_types=["card"],
            mode="subscription",
            line_items=[{"price": STRIPE_SUB_PRICE_ID, "quantity": 1}],
            metadata={"userId": user_id},
        )

        return {"sessionId": checkout_session["id"]}

    except Exception as e:
        return {"error": {"message": str(e)}}


def create_customer_portal(customer_id: str):
    session = stripe.billing_portal.Session.create(
        customer=customer_id, return_url=REDIRECT_URL + "favourites"
    )

    return {"url": session.url}


def construct_webhook_event(payload, signature: str):
    return stripe.Webhook.construct_event(
        payload=payload,
        sig_header=signature,
        secret=STRIPE_WEBHOOK_SECRET,
    )
