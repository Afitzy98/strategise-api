import pandas as pd
import numpy as np
from typing import List

from .types import Num

def get_simple_ma_signal(ohlcv_data: List[Num]) -> bool:
  data = np.array(ohlcv_data)

  df = pd.DataFrame(data[:,1:], index=data[:,0], columns=["open", "high", "low", "close", "volume"])

  df["MA20"] = df["open"].rolling(20).mean()
  df["MA10"] = df["open"].rolling(10).mean()
  df["MA5"] = df["open"].rolling(5).mean()

  longs = (df["MA5"] > df["MA20"]) & (df["MA10"] > df["MA20"])
  return longs.values[-1]
