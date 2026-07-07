#syntax=docker/dockerfile:1
FROM postgis/postgis:18-3.6-alpine

RUN apk add --no-cache musl-locales

COPY ./PostgreSQL-DB/* /docker-entrypoint-initdb.d





