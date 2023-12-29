#!/bin/bash

# Wait for the database to be ready
until nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for database connection..."
  sleep 2
done

# Initialize Airflow database
airflow db init

# Create admin user
airflow users create \
    --username ${AIRFLOW_USER} \
    --password ${AIRFLOW_PASSWORD} \
    --firstname ${AIRFLOW_FIRSTNAME} \
    --lastname ${AIRFLOW_LASTNAME} \
    --role ${AIRFLOW_ROLE} \
    --email ${AIRFLOW_EMAIL}

# Start the main process
exec "$@"
