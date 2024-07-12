import datetime

def convert_isostirng_date_to_datetime(iso_string: str) -> datetime.datetime:
  date = datetime.date.fromisoformat(iso_string)
  return datetime.datetime(date.year, date.month, date.day)