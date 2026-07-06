#syntax=docker/dockerfile:1
FROM postgis/postgis:18-3.6-alpine

# default psql user password
ENV POSTGRES_PASSWORD=password

#copy database structure files into the container
RUN mkdir -p /home/db-structure
COPY PostgreSQL-DB /home/db-structure

#execute commands and run db server
CMD ["post"]



