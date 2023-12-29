# Makefile

# Variables
VENV_NAME?=venv
AIRFLOW_HOME?=~/airflow
AIRFLOW_USER?=FortyOneTech
AIRFLOW_PASSWORD?=UncleSam41!
AIRFLOW_EMAIL?=techfortyone@gmail.com
AIRFLOW_FIRSTNAME?=FortyOne
AIRFLOW_LASTNAME?=Tech
AIRFLOW_ROLE?=Admin

clean:
	rm -rf $(AIRFLOW_HOME) venv/ dataset/ *.zip *.json logs/ neo4j/ plugins/ dags/ notebooks/.ipynb_checkpoints/
	rm -rf $(AIRFLOW_HOME) notebooks/logs/ notebooks/neo4j/ notebooks/plugins/ notebooks/dags/ notebooks/config/ notebooks/data/

# Create and activate virtual environment
venv:
	python3 -m venv $(VENV_NAME) # RUN: `source venv/bin/activate` to activate

# Install required packages
install:
	$(VENV_NAME)/bin/pip install -r requirements.txt

# Initialize Airflow (database and folders)
init-airflow:
	$(VENV_NAME)/bin/airflow db init

# Create Airflow admin user
create-admin-user:
	$(VENV_NAME)/bin/airflow users create \
		--username $(AIRFLOW_USER) \
		--password $(AIRFLOW_PASSWORD) \
		--firstname $(AIRFLOW_FIRSTNAME) \
		--lastname $(AIRFLOW_LASTNAME) \
		--role ${AIRFLOW_ROLE} \
		--email $(AIRFLOW_EMAIL)

# Set Airflow home environment variable
set-airflow-home:
	mkdir -p $(AIRFLOW_HOME)/dags $(AIRFLOW_HOME)/logs $(AIRFLOW_HOME)/plugins
	cp ./src/dags/*.py $(AIRFLOW_HOME)/dags
	export AIRFLOW_HOME=$(AIRFLOW_HOME)

# Set Kaggle API credentials permissions
set-kaggle-credentials:
	mkdir -p ~/.kaggle
	cp ./assets/kaggle.json ~/.kaggle/
	chmod 600 ~/.kaggle/kaggle.json

# Default target
init: install set-airflow-home init-airflow set-kaggle-credentials create-admin-user

# Start Airflow webserver
start-webserver:
	$(VENV_NAME)/bin/airflow webserver -p 8080

# Start Airflow scheduler
start-scheduler:
	$(VENV_NAME)/bin/airflow scheduler

.PHONY: venv install init-airflow set-airflow-home set-kaggle-credentials start-webserver start-scheduler
