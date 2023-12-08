import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import kaggle

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('arxiv_dataset_acquisition',
          default_args=default_args,
          description='Download and explore ArXiv dataset',
          schedule_interval=timedelta(days=1),
          start_date=datetime(2023, 1, 1),
          catchup=False)

def download_dataset():
    os.system('kaggle datasets download -d Cornell-University/arxiv')
    os.system('unzip arxiv.zip -d dataset')

def explore_dataset():
    # Data exploration code goes here
    df = pd.read_csv('dataset/arxiv-metadata-oai-snapshot.json')
    # Example: print dataset structure and summary
    print(df.head())
    print(df.describe())

download_task = PythonOperator(
    task_id='download_arxiv_dataset',
    python_callable=download_dataset,
    dag=dag,
)

explore_task = PythonOperator(
    task_id='explore_arxiv_dataset',
    python_callable=explore_dataset,
    dag=dag,
)

download_task >> explore_task
