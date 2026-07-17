from google.transit import gtfs_realtime_pb2
import requests as rq
import pandas as pd

from fit_live_data import fit_live_data

def get_live_data(dynamic_URL = "https://cdn.zbiorkom.live/gtfs-rt/lodz.pb"):

    try:
        live_data = gtfs_realtime_pb2.FeedMessage()
        response = rq.get(dynamic_URL)
        live_data.ParseFromString(response.content)

    except Exception as e:
        raise ConnectionError(f"ERROR: Cannot get live data from the API: {e}")


    dict = []

    for ent in live_data.entity:

        if ent.HasField('trip_update'):
            trip_up = ent.trip_update
            for stop_t_up in trip_up.stop_time_update:
                dict.append({
                    "trip_id": trip_up.trip.trip_id,
                    "stop_sequence": stop_t_up.stop_sequence,
                    "vehicle_id": trip_up.vehicle.id,
                    "arrival": stop_t_up.arrival.time,
                    "departure": stop_t_up.departure.time,
                    "service_date": trip_up.trip.start_date,
                    "trip_timestamp": trip_up.timestamp
                })

    live_df = pd.DataFrame(dict)

    live_df = fit_live_data(live_df)


    return live_df





if __name__ == "__main__":

    live_df = get_live_data()
    # pd.set_option('display.max_columns', 7)
    # pd.set_option('display.max_rows', len(live_df))
    print(live_df)
    # pd.reset_option('display.max_columns')
    # pd.reset_option('display.max_rows')