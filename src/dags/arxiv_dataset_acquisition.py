import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=0.5),
}

dag = DAG('arxiv_dataset_acquisition',
          default_args=default_args,
          description='Download and explore ArXiv dataset',
          schedule_interval=timedelta(days=1),
          start_date=datetime(2023, 1, 1),
          catchup=False)

def download_dataset():
    if not os.path.exists('arxiv.zip'):
        os.system('kaggle datasets download -d Cornell-University/arxiv')
    if not os.path.exists('dataset/arxiv-metadata-oai-snapshot.json'):
        os.system('unzip -o arxiv.zip -d dataset')

download_task = PythonOperator(
    task_id='download_arxiv_dataset',
    python_callable=download_dataset,
    dag=dag,
)

download_task
