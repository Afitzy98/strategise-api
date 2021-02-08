from coinpaprika import client as Coinpaprika

from ..constants import NUM_DAYS
from ..indicators import get_trade_indicators
from ..signals import get_simple_ma_signal
from ..utils import get_ts_from_time, get_string_from_timestamp, get_ts_from_string

from datetime import datetime

client = Coinpaprika.Client()


def get_coin_by_id(coin_id: str):
    len_data = 20 + NUM_DAYS  # biggest ma val + num days

    coin = get_coin_info_by_id(coin_id)
    ohlcv_data = get_ohlcv_data_for_coin(coin_id, len_data)
    signal = get_simple_ma_signal(ohlcv_data)
    indicators = get_trade_indicators(
        ohlcv_data,
    )
    return {
        "coin": coin,
        "signal": str(signal),
        "ohlcv": ohlcv_data[-NUM_DAYS:],
        "indicators": indicators,
    }


def get_coins():
    d = client.coins()
    return [c for c in d if c["is_active"] == True]


def get_coin_info_by_id(id):
    c = client.coin(id)
    del c["tags"]
    return c


def get_ohlcv_data_for_coin(coin_id: str, num_days: int):
    end = get_string_from_timestamp(get_ts_from_time())  # now
    start = get_string_from_timestamp(
        get_ts_from_time(min(364, num_days))
    )  # num days ago

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
