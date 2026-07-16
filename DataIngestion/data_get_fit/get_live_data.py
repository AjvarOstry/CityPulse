
from google.transit import gtfs_realtime_pb2
import requests as rq

dynamic_URL = "https://cdn.zbiorkom.live/gtfs-rt/lodz.pb"
def get_pb_feed():

    pb_feed = gtfs_realtime_pb2.FeedMessage()
    response = rq.get(dynamic_URL)
    pb_feed.ParseFromString(response.content)
    return pb_feed




if __name__ == "__main__":

    for entity in get_pb_feed().entity:
        if entity.HasField('trip_update'):
            print(entity.trip_update)