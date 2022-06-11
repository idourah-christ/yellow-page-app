#!/bin/sh 

#check if the db is postgres 
if ["$DATABASE" = "postgres"]
then 
    echo "waiting for postgres..."
    
    while ! nc -z $SQL_HOST $SQL_PORT; do 
        sleep 0.1
    done 

    echo "PostgresSQL started"
fi 
if ["$FLASK_DEV" = "development"]
then 
    echo "creating database tables..."
    python manage.py create_db
    echo "Tables created.."  
fi
exec "$@"