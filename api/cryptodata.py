from coinpaprika import client as Coinpaprika
from .utils import get_ts_from_time, get_string_from_timestamp, get_ts_from_string

client = Coinpaprika.Client()

def get_all_coins():
  d = client.coins()
  return [c for c in d if c["is_active"] == True]

def get_coin_info_by_id(id):
  c = client.coin(id)
  del c["tags"]
  return c

def get_ohlcv_data_for_coin(coin_id: str, num_days: int):
  end = get_string_from_timestamp(get_ts_from_time()) # now
  start = get_string_from_timestamp(get_ts_from_time(num_days)) # num days ago

  d = client.candles(coin_id, start=start, end=end)

  return [[get_ts_from_string(r["time_open"]), r["open"], r["high"], r["low"], r["close"], r["volume"]] for r in d]



