from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=0.5),
}

dag = DAG('create_dwh_tables_arxiv',
          default_args=default_args,
          description='Create tables in PostgreSQL for arXiv dataset',
          schedule_interval='@once',
          start_date=datetime(2023, 1, 1),
          catchup=False)

# SQL commands to create tables
create_author_dimension = """
CREATE TABLE IF NOT EXISTS dim_author (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    author_parsed VARCHAR(255)
);
"""

create_publication_dimension = """
CREATE TABLE IF NOT EXISTS dim_publication (
    publication_id SERIAL PRIMARY KEY,
    journal_ref VARCHAR(255),
    doi VARCHAR(255)
);
"""

create_category_dimension = """
CREATE TABLE IF NOT EXISTS dim_category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255)
);
"""

create_submission_dimension = """
CREATE TABLE IF NOT EXISTS dim_submission (
    submission_id SERIAL PRIMARY KEY,
    submitter VARCHAR(255),
    submission_date DATE
);
"""

create_details_dimension = """
CREATE TABLE IF NOT EXISTS dim_details (
    detail_id SERIAL PRIMARY KEY,
    title TEXT,
    abstract TEXT,
    comments TEXT
);
"""

create_arxiv_fact_table = """
CREATE TABLE IF NOT EXISTS fact_arxiv (
    id SERIAL PRIMARY KEY,
    author_ids INT[],
    publication_id INT,
    category_ids INT[],
    submission_id INT,
    detail_id INT,
    versions TEXT,
    update_date DATE
);
"""

# Define tasks
create_author_dim_task = PostgresOperator(
    task_id='create_author_dim',
    postgres_conn_id='postgres_default',
    sql=create_author_dimension,
    dag=dag,
)

create_publication_dim_task = PostgresOperator(
    task_id='create_publication_dim',
    postgres_conn_id='postgres_default',
    sql=create_publication_dimension,
    dag=dag,
)

create_category_dim_task = PostgresOperator(
    task_id='create_category_dim',
    postgres_conn_id='postgres_default',
    sql=create_category_dimension,
    dag=dag,
)

create_submission_dim_task = PostgresOperator(
    task_id='create_submission_dim',
    postgres_conn_id='postgres_default',
    sql=create_submission_dimension,
    dag=dag,
)

create_details_dim_task = PostgresOperator(
    task_id='create_details_dim',
    postgres_conn_id='postgres_default',
    sql=create_details_dimension,
    dag=dag,
)

create_arxiv_fact_task = PostgresOperator(
    task_id='create_arxiv_fact',
    postgres_conn_id='postgres_default',
    sql=create_arxiv_fact_table,
    dag=dag,
)

# Set task dependencies
create_author_dim_task >> create_publication_dim_task >> create_category_dim_task
create_category_dim_task >> create_submission_dim_task >> create_details_dim_task
create_details_dim_task >> create_arxiv_fact_task
