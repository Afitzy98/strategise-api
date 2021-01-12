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

  data = client.candles(coin_id, start=start, end=end)

  out = []

  for row in data:
    ts = get_ts_from_string(row.get("time_open"))
    o = row.get("open")
    h = row.get("high")
    l = row.get("low")
    c = row.get("close")
    v = row.get("volume")

    out.append([ts, o, h, l, c, v])

  return out



