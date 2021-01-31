from enum import Enum

DEFAULT_FAVOURITES = [
    "btc-bitcoin",
    "eth-ethereum",
    "ltc-litecoin",
    "xrp-ripple",
    "ada-cardano",
]
MA_INDICATOR_VALS = [5, 10, 20]
MA_INDICATOR_COLORS = ["#FFD700", "#FF69B4", "#7F00FF"]
NUM_DAYS = 365


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    INCOMPLETE = "incomplete"
    INCOMPLETE_EXPIRED = "incomplete_expired"
    PAST_DUE = "past_due"
    TRIALING = "trialing"
    UNPAID = "unpaid"


class WebhookEvent(str, Enum):
    CHECKOUT_SESSION_COMPLETED = "checkout.session.completed"
    CUSTOMER_SUBSCRIPTION_UPDATED = "customer.subscription.updated"
