from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .db import engine
from .routers import coins, payments, users

models.Base.metadata.drop_all(bind=engine)  # remove
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(coins.router)
app.include_router(payments.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=[
        "Content-Type",
        "Access-Control-Allow-Headers",
        "Authorization",
        "X-Requested-With",
    ],
)


@app.get("/")
async def root():
    return {"Status": "OK"}
