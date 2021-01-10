import json
from typing import Optional

from api import app
from .contants import MA_INDICATOR_VALS, MA_INDICATOR_COLORS, NUM_DAYS
from .cryptodata import get_all_coins, get_coin_info_by_id, get_ohlcv_data_for_coin
from .indicators import get_ma_indicators
from .signals import get_simple_ma_signal

@app.get("/")
def read_root():
    return {"Status": "OK"}


@app.get("/coin/{coin_id}")
async def get_coin_info(coin_id: str):
  len_data = max(MA_INDICATOR_VALS) + NUM_DAYS

  coin = get_coin_info_by_id(coin_id)
  ohlcv_data = get_ohlcv_data_for_coin(coin_id, len_data)
  signal = get_simple_ma_signal(ohlcv_data)
  ma_indicators = get_ma_indicators(ohlcv_data, MA_INDICATOR_VALS, NUM_DAYS, MA_INDICATOR_COLORS)
  
  return { "coin": coin,  "signal": str(signal), "ohlcv": ohlcv_data[-NUM_DAYS:], "indicators": ma_indicators }


@app.get("/coins")
async def get_coins_list():
  return get_all_coins()