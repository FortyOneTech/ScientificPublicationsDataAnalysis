# How to Work with Makefile

## Overview

This README provides instructions for setting up and managing an Apache Airflow environment using a `Makefile`. The `Makefile` simplifies the process of environment setup, Airflow initialization, user creation, and server management. Below are detailed instructions on how to use each command defined in the `Makefile`.

## Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- Access to a terminal or command-line interface

## Setup

### 0. Purge and Clean

Before you do anything, make sure you purge and clean all the remnants remaining from the past runs.

**Command:**

```bash
make clean
```

### 1. Creating a Virtual Environment

Before you start, you need to create a Python virtual environment which helps to keep dependencies required by different projects separate.

**Command:**

```bash
make venv
```

After running this command, activate the virtual environment:

- On Unix or MacOS: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

### 2. Installing Required Packages

Install all required Python packages listed in `requirements.txt`.

**Command:**

```bash
make install
```

This command installs Apache Airflow and other necessary packages in the virtual environment.

### 3. Initializing Airflow

Set up the initial Airflow environment including the database and default folders.

**Command:**

```bash
make init-airflow
```

### 4. Creating an Admin User for Airflow

Create an admin user for accessing the Airflow web interface.

**Command:**

```bash
make create-admin-user
```

This creates a user with the credentials specified in the `Makefile`.

### 5. Setting Airflow Home Environment Variable

Set the `AIRFLOW_HOME` environment variable. This defines where Airflow stores its configuration and DAG files.

**Command:**

```bash
make set-airflow-home
```

### 6. Configuring Kaggle API Credentials

Set the correct permissions for Kaggle API credentials (used for downloading datasets from Kaggle).

**Command:**

```bash
make set-kaggle-credentials
```

This command assumes that your Kaggle API key (`kaggle.json`) is located in the `./assets` directory.

### 7. Copying DAGs to Airflow

Copy your DAGs from the `src/dags` directory to the Airflow DAGs folder.

**Command:**

```bash
make cp-dags
```

## Default Commands

### Initialize Everything

To perform all initialization steps (install, initialize Airflow, set environment variables, set Kaggle credentials, and create an admin user) in one go:

**Command:**

```bash
make init
```

## Running Airflow

### 1. Starting the Airflow Webserver

Launch the Airflow webserver which provides the web UI to interact with Airflow.

**Command:**

```bash
make start-webserver
```

By default, the webserver will be available at `http://localhost:8080`.

### 2. Starting the Airflow Scheduler

Open new tab with `Ctrl + T` and start the Airflow scheduler which orchestrates the execution of jobs after activating `venv`.

**Command:**

```bash
make start-scheduler
```

## Note
1. Ensure that you activate the virtual environment every time you open a new terminal session before running these `make` commands. 
2. Make sure you start both webserver and scheduler processes in two separate tabs.
3. For more advanced usage and troubleshooting, refer to the official Apache Airflow documentation.