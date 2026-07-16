import pandas as pd
from datetime import date, timedelta

def test_dataframe():

    pd_dictionary = {}

    # Calendar
    pd_dictionary["Calendar"] = pd.DataFrame([
        {
            "service_id": "WKD_001",
            "start_date": "2026-01-01",
            "end_date": "2026-12-31"
        },
        {
            "service_id": "WKD_002",
            "start_date": "2026-01-01",
            "end_date": "2026-12-31"
        },
    ])

    # Calendar_Dates
    pd_dictionary["Calendar_Dates"] = pd.DataFrame([
        {
            "service_id": "WKD_001",
            "service_date": "2026-07-16",
            "is_running": True
        },
        {
            "service_id": "WKD_001",
            "service_date": "2026-07-17",
            "is_running": True
        },
        {
            "service_id": "WKD_002",
            "service_date": "2026-07-16",
            "is_running": False
        },
    ])


    # Routes
    pd_dictionary["Routes"] = pd.DataFrame([
        {
            "route_id": "101",
            "route_type": "bus"
        },
        {
            "route_id": "15",
            "route_type": "tram"
        },
        {
            "route_id": "8",
            "route_type": "tram"
        },
    ])


    # Shape_Headers
    pd_dictionary["Shape_Headers"] = pd.DataFrame([
        {"shape_id": 1001},
        {"shape_id": 1002},
        {"shape_id": 1003},
    ])


    # Shapes
    pd_dictionary["Shapes"] = pd.DataFrame([
        {
            "shape_id": 1001,
            "shape_pt_sequence": 1,
            "shape_pt_lat": 51.759,
            "shape_pt_lon": 19.457
        },
        {
            "shape_id": 1001,
            "shape_pt_sequence": 2,
            "shape_pt_lat": 51.760,
            "shape_pt_lon": 19.460
        },
        {
            "shape_id": 1002,
            "shape_pt_sequence": 1,
            "shape_pt_lat": 51.770,
            "shape_pt_lon": 19.450
        },
        {
            "shape_id": 1003,
            "shape_pt_sequence": 1,
            "shape_pt_lat": 51.750,
            "shape_pt_lon": 19.470
        },
    ])


    # Stops
    pd_dictionary["Stops"] = pd.DataFrame([
        {
            "stop_id": 1,
            "stop_code": 1001,
            "stop_name": "Piotrkowska Centrum",
            "stop_lat": 51.765,
            "stop_lon": 19.456
        },
        {
            "stop_id": 2,
            "stop_code": 1002,
            "stop_name": "Plac Wolnosci",
            "stop_lat": 51.772,
            "stop_lon": 19.457
        },
        {
            "stop_id": 3,
            "stop_code": 1003,
            "stop_name": "Dworzec Fabryczny",
            "stop_lat": 51.770,
            "stop_lon": 19.465
        },
    ])


    # Trips
    pd_dictionary["Trips"] = pd.DataFrame([
        {
            "trip_id": "TRIP_0001",
            "route_id": "101",
            "service_id": "WKD_001",
            "trip_headsign": "Centrum",
            "direction": True,
            "shape_id": 1001
        },
        {
            "trip_id": "TRIP_0002",
            "route_id": "15",
            "service_id": "WKD_001",
            "trip_headsign": "Retkinia",
            "direction": False,
            "shape_id": 1002
        },
        {
            "trip_id": "TRIP_0003",
            "route_id": "8",
            "service_id": "WKD_002",
            "trip_headsign": "Dworzec",
            "direction": True,
            "shape_id": 1003
        },
    ])


    # Stop_Times
    pd_dictionary["Stop_Times"] = pd.DataFrame([
        {
            "trip_id": "TRIP_0001",
            "arrival_time": "08:00:00",
            "departure_time": "08:00:30",
            "stop_id": 1,
            "stop_sequence": 1
        },
        {
            "trip_id": "TRIP_0001",
            "arrival_time": "08:05:00",
            "departure_time": "08:05:30",
            "stop_id": 2,
            "stop_sequence": 2
        },
        {
            "trip_id": "TRIP_0002",
            "arrival_time": "09:00:00",
            "departure_time": "09:00:30",
            "stop_id": 3,
            "stop_sequence": 1
        },
    ])

    return pd_dictionary