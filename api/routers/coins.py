import json
from fastapi import APIRouter, Depends, HTTPException
from typing import List

# from ..context import get_current_active_user
from ..constants import MA_INDICATOR_VALS, MA_INDICATOR_COLORS, NUM_DAYS
from ..crud import coins as crud


router = APIRouter(
    prefix="/coins",
    tags=["coins"],
    # dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{coin_id}")
async def get_coin_info(coin_id: str):
    return crud.get_coin_by_id(coin_id)


@router.get("/")
async def get_coins_list():
    return crud.get_coins()
