#!/bin/sh 

exec docker-compose exec db psql --username="$POSTGRES_USER" --dbname="$POSTGRES_DB"