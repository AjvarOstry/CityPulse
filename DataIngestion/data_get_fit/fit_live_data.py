import pandas as pd
from fit_data_helpers import parse_time_to_gtfs

def fit_live_data(live_df):

    live_df["service_date"] = parse_time_to_gtfs(live_df["service_date"])

    return live_df
