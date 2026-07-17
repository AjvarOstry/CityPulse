import pandas as pd
from collections import OrderedDict
from fit_data_helpers import parse_time_to_gtfs

def fit_static_data(pd_dictionary):

# CALENDAR
    pd_dictionary["Calendar"] = pd_dictionary["Calendar"][[
        "service_id",
        "start_date",
        "end_date"
    ]]
    pd_dictionary["Calendar"]["start_date"] = pd.to_datetime(
        pd_dictionary["Calendar"]["start_date"],
        format="%Y%m%d",
        yearfirst=True
    )
    pd_dictionary["Calendar"]["end_date"] = pd.to_datetime(
        pd_dictionary["Calendar"]["end_date"],
        format="%Y%m%d",
        yearfirst=True)

#CALENDAR_DATES
    pd_dictionary["Calendar_Dates"]["exception_type"] = pd_dictionary["Calendar_Dates"]["exception_type"].replace(
        {2: False, 1: True})
    pd_dictionary["Calendar_Dates"].rename(
        columns={"exception_type": "is_running"},
        inplace=True
    )
    pd_dictionary["Calendar_Dates"]["date"] = pd.to_datetime(
        pd_dictionary["Calendar_Dates"]["date"],
        format="%Y%m%d",
        yearfirst=True)
    pd_dictionary["Calendar_Dates"].rename(columns={"date": "service_date"}, inplace=True)

# ROUTES
    pd_dictionary["Routes"] = pd_dictionary["Routes"][[
        "route_id",
        "route_type"
    ]]
    pd_dictionary["Routes"]["route_type"] = pd_dictionary["Routes"]["route_type"].replace(
        {0: "tram", 3:"bus"}
    )

# SHAPES
    pd_dictionary["Shapes"] = pd_dictionary["Shapes"][[
        "shape_id",
        "shape_pt_sequence",
        "shape_pt_lat",
        "shape_pt_lon"
    ]]

# STOP_TIMES
    pd_dictionary["Stop_Times"] = pd_dictionary["Stop_Times"][[
        "trip_id",
        "arrival_time",
        "departure_time",
        "stop_id",
        "stop_sequence"
    ]]
    pd_dictionary["Stop_Times"]["arrival_time"] = pd_dictionary["Stop_Times"]["arrival_time"].apply(parse_time_to_gtfs)
    pd_dictionary["Stop_Times"]["departure_time"] = pd_dictionary["Stop_Times"]["departure_time"].apply(parse_time_to_gtfs)


# STOPS
    pd_dictionary["Stops"] = pd_dictionary["Stops"][[
        "stop_id",
        "stop_code",
        "stop_name",
        "stop_lat",
        "stop_lon"
    ]]

# TRIPS
    pd_dictionary["Trips"] = pd_dictionary["Trips"][[
        "trip_id",
        "route_id",
        "service_id",
        "trip_headsign",
        "direction_id",
        "shape_id"
    ]]

    pd_dictionary["Trips"].rename(
        columns={"direction_id": "direction"},
        inplace=True
    )
    pd_dictionary["Trips"]["direction"] = pd_dictionary["Trips"]["direction"].replace(
        {0: False, 1: True}
    )

# SHAPE_HEADERS
    pd_dictionary["Shape_Headers"] = pd.DataFrame(
        pd_dictionary["Trips"]["shape_id"].unique(),
        columns=["shape_id"]
    )

    pd_dictionary = OrderedDict(pd_dictionary)
    pd_dictionary.move_to_end("Shape_Headers", last=False)
    pd_dictionary.move_to_end("Stop_Times", last=True)

    return pd_dictionary
