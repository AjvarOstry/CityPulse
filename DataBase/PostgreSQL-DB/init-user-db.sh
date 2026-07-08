#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP_1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER docker WITH NOSUPERUSER PASSWORD 'docker' LOGIN;
    GRANT CONNECT ON DATABASE "CityPulseDB" TO docker;
    GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO docker;
EOSQL