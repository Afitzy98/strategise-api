import pandas as pd
import numpy as np
from typing import List

from .types import Num

def get_ma_indicators(ohlcv_data: List[Num], avgs: List[int], max_num_vals: int, colors: List[str]) -> List[Num]:
  data = np.array(ohlcv_data)
  indicators = []
  df = pd.DataFrame(data[:,1:], index=data[:,0], columns=["open", "high", "low", "close", "volume"])

  for i in range(len(avgs)):
    a = avgs[i]
    ma = df["open"].rolling(a).mean().dropna()

    data = [[int(ma.index[i]), ma.values[i]] for i in range(len(ma))]

    indicators.append({
      "name": f"MA({a})",
      "type": "SMA",
      "data": data[-max_num_vals:],
      "settings": {
        "color": colors[i]
      }
    })

  return indicators




