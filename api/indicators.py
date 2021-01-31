import pandas as pd
import numpy as np
from typing import List

from .constants import NUM_DAYS
from .types import Num


def get_trade_indicators(ohlcv_data: List[Num]):
    trades = []
    data = np.array(ohlcv_data)

    df = pd.DataFrame(
        data[-NUM_DAYS:, 1:],
        index=data[-NUM_DAYS:, 0],
        columns=["open", "high", "low", "close", "volume"],
    )

    MA5 = df["open"].rolling(5).mean()
    MA10 = df["open"].rolling(10).mean()
    MA20 = df["open"].rolling(20).mean()

    longs = (MA5 > MA20) & (MA10 > MA20)

    prev = False

    for i in range(len(longs)):
        v = longs.values[i]
        t = longs.index[i]
        p = df["open"].values[i]

        if v == True and prev == False:
            trades.append([t, 1, p])

        if v == False and prev == True:
            trades.append([t, 0, p])

        prev = v

    return [
        {
            "name": "Bot Trades",
            "type": "Trades",
            "data": trades,
        }
    ]