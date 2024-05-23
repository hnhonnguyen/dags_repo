from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
 
from datetime import datetime

my_file = Dataset('/tmp/my_file.txt')

def print_dataset_uri():
    print(my_file.uri)
    with open(my_file.uri, 'a') as f:
        f.write('Hello World!')
 
with DAG('group_dag', start_date=datetime(2022, 1, 1), 
    schedule_interval='42 15 * * *', catchup=False) as dag:
 
    download_a = PythonOperator(
        task_id = 'print_dataset_uri',
        python_callable=print_dataset_uri
    )
 
    download_b = BashOperator(
        task_id='download_b',
        bash_command='sleep 10'
    )
 
    download_c = BashOperator(
        task_id='download_c',
        bash_command='sleep 10'
    )
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
 
    transform_a = BashOperator(
        task_id='transform_a',
        bash_command='sleep 10'
    )
 
    transform_b = BashOperator(
        task_id='transform_b',
        bash_command='sleep 10'
    )
 
    transform_c = BashOperator(
        task_id='transform_c',
        bash_command='sleep 10',
        outlets=[my_file]
    )
 
    [download_a, download_b, download_c] >> check_files >> [transform_a, transform_b, transform_c]