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
NUM_DAYS = 90


class PaymentStatus(str, Enum):
    PAID = "paid"
    FAILED = "failed"
    PENDING = "pending"
    CANCELLED = "cancelled"
    RENEWING = "renewing"


class WebhookEvent(str, Enum):
    CHECKOUT_SESSION_COMPLETED = "checkout.session.completed"
    CUSTOMER_SUBSCRIPTION_DELETED = "customer.subscription.deleted"
    INVOICE_CREATED = "invoice.created"
    INVOICE_PAID = "invoice.paid"
    INVOICE_PAYMENT_FAILED = "invoice.payment_failed"