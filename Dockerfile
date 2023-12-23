# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV AIRFLOW_HOME=/usr/local/airflow
ENV AIRFLOW_USER=FortyOneTech
ENV AIRFLOW_PASSWORD=UncleSam41!
ENV AIRFLOW_EMAIL=techfortyone@gmail.com
ENV AIRFLOW_FIRSTNAME=FortyOne
ENV AIRFLOW_LASTNAME=Tech
ENV AIRFLOW_ROLE=Admin
ENV KAGGLE_CONFIG_DIR=/usr/local/airflow/.kaggle

# Set the working directory
WORKDIR ${AIRFLOW_HOME}

# Copy the requirements file into the container
COPY requirements.txt ${AIRFLOW_HOME}/

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Airflow and other necessary packages
RUN pip install -r requirements.txt

# Create directories for Airflow and copy DAGs
RUN mkdir -p ${AIRFLOW_HOME}/dags ${AIRFLOW_HOME}/logs ${AIRFLOW_HOME}/plugins
COPY ./src/dags/*.py ${AIRFLOW_HOME}/dags/

# Initialize Airflow (database and folders)
RUN airflow db init

# Create Airflow admin user
RUN airflow users create \
    --username ${AIRFLOW_USER} \
    --password ${AIRFLOW_PASSWORD} \
    --firstname ${AIRFLOW_FIRSTNAME} \
    --lastname ${AIRFLOW_LASTNAME} \
    --role ${AIRFLOW_ROLE} \
    --email ${AIRFLOW_EMAIL}

# Set up Kaggle API credentials
RUN mkdir -p ${KAGGLE_CONFIG_DIR}
COPY ./assets/kaggle.json ${KAGGLE_CONFIG_DIR}/
RUN chmod 600 ${KAGGLE_CONFIG_DIR}/kaggle.json

# Switch to non-root user for security
RUN useradd -ms /bin/bash airflow
RUN chown -R airflow:airflow ${AIRFLOW_HOME}
USER airflow
