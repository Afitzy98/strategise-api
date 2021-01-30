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


class WebhookEvent(str, Enum):
    INVOICE_PAID = "invoicce.paid"
    INVOICE_PAYMENT_FAILED = "invoice.payment_failed"
    CHECKOUT_SESSION_COMPLETED = "checkout.session.completed"