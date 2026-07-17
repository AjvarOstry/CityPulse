-- CityPulse Database creation file

-- DROP DATABASE IF EXISTS "CityPulseDB";
-- CREATE DATABASE "CityPulseDB";
\c "CityPulseDB"


CREATE TABLE "Calendar" (
    service_id VARCHAR(12) PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);


CREATE TABLE "Calendar_Dates" (
    service_id VARCHAR(12) NOT NULL,
    service_date DATE NOT NULL,
    is_running BOOLEAN NOT NULL,

    PRIMARY KEY (service_id, service_date),

    CONSTRAINT fk_calendardates_calendar
        FOREIGN KEY (service_id)
        REFERENCES "Calendar"(service_id)
);


CREATE TYPE Vehicles AS ENUM ('bus', 'tram');

CREATE TABLE "Routes" (
    route_id VARCHAR(4) PRIMARY KEY,
    route_type Vehicles NOT NULL
);


CREATE TABLE "Shape_Headers" (
    shape_id INT PRIMARY KEY
);

-- lat i lon do przerobienia na postgis
CREATE TABLE "Shapes" (
    shape_id INT NOT NULL,
    shape_pt_sequence INT NOT NULL,
    shape_pt_lat DOUBLE PRECISION NOT NULL,
    shape_pt_lon DOUBLE PRECISION NOT NULL,

    PRIMARY KEY(shape_id, shape_pt_sequence),

    CONSTRAINT fk_shapes_shapeheaders
        FOREIGN KEY (shape_id)
        REFERENCES "Shape_Headers"(shape_id)
);

-- lat i lon do przerobienia na postgis
CREATE TABLE "Stops" (
    stop_id INT PRIMARY KEY,
    stop_code INT NOT NULL,
    stop_name VARCHAR(100) NOT NULL,

    stop_lat DOUBLE PRECISION NOT NULL,
    stop_lon DOUBLE PRECISION NOT NULL
);


CREATE TABLE "Trips" (
    trip_id VARCHAR(16) PRIMARY KEY,
    route_id VARCHAR(4) NOT NULL,
    service_id VARCHAR(12) NOT NULL,
    trip_headsign VARCHAR(100),
    direction BOOLEAN NOT NULL,
    shape_id INT NOT NULL,

    CONSTRAINT fk_trips_routes
        FOREIGN KEY (route_id)
        REFERENCES "Routes"(route_id),
    CONSTRAINT fk_trips_calendar
        FOREIGN KEY (service_id)
        REFERENCES "Calendar"(service_id),
    CONSTRAINT fk_trips_shapeheaders
        FOREIGN KEY (shape_id)
        REFERENCES "Shape_Headers"(shape_id)
);


-- arrival i departure nie są null, bo krańcówki
CREATE TABLE "Stop_Times" (
    trip_id VARCHAR(16) NOT NULL,
    arrival_time INTERVAL,
    departure_time INTERVAL,
    stop_id INT NOT NULL,
    stop_sequence INT NOT NULL,

    PRIMARY KEY (trip_id, stop_sequence),

    CONSTRAINT fk_stoptimes_trips
        FOREIGN KEY (trip_id)
        REFERENCES "Trips"(trip_id),
    CONSTRAINT fk_stoptimes_stops
        FOREIGN KEY (stop_id)
        REFERENCES "Stops"(stop_id)
);


-- REALTIME DATA TABLE
CREATE TABLE "RT_Trips" (
    trip_id VARCHAR(16) NOT NULL,
    stop_sequence INT NOT NULL,
    vehicle_id VARCHAR(10),
    delay_seconds INT NOT NULL,
    service_date DATE NOT NULL,
    trip_timestamp TIMESTAMP NOT NULL,

    PRIMARY KEY (trip_id, stop_sequence, trip_timestamp),

    CONSTRAINT fk_rttrips_trips
        FOREIGN KEY (trip_id)
        REFERENCES "Trips"(trip_id)
);


