#Data Pipeline Orchestration:
#In the pipeline_orchestration/ folder, create a workflow definition file called data_pipeline.py using Apache Airflow

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'finance_data_pipeline',
    default_args=default_args,
    schedule_interval='0 0 * * *',  # Daily at midnight
)

fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    op_args=['https://api.example.com/finance-data', 'data/raw_data.json'],
    dag=dag
)

clean_data_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    op_args=['data/raw_data.json', 'data/cleaned_data.csv'],
    dag=dag
)

validate_data_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    op_args=['data/cleaned_data.csv'],
    dag=dag
)

upload_to_database_task = PythonOperator(
    task_id='upload_to_database',
    python_callable=upload_to_database,
    op_args=['data/cleaned_data.csv', 'postgresql://user:password@localhost/mydatabase', 'finance_data'],
    dag=dag
)

# Define task dependencies
fetch_data_task >> clean_data_task >> validate_data_task >> upload_to_database_task
    
