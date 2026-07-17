import pandas as pd

def parse_time_to_gtfs(time):
    h, m, s = map(int, time.split(":"))
    return pd.Timedelta(hours=h, minutes=m, seconds=s)
