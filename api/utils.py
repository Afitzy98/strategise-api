import dateutil.parser
from datetime import datetime, timedelta
from pytz import utc


def get_string_from_timestamp(ts: int) -> str:
  dt = datetime.fromtimestamp(ts/1000)
  return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def get_ts_from_string(date_str: str) -> int:
  d = dateutil.parser.parse(date_str)
  d.replace(tzinfo=utc) - d.utcoffset()
  return int(datetime.timestamp(d) * 1000)

def get_ts_from_time(days: int = 0, hours: int = 0, mins:  int = 0) -> int:
  now = datetime.now()
  d = now - timedelta(days, hours, mins)
  return int(datetime.timestamp(d) * 1000)
