from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import time

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 16),
    'retries': 1,
    'email': 'vn3848587@gmail.com',
    
}

def print_nested_kwargs(kwargs, indent=""):
    for key, value in kwargs.items():
        if isinstance(value, dict):
            print(f"{indent}Nested kwargs for {key}:")
            print_nested_kwargs(value, indent + "  ")
        else:
            print(f"{indent}{key}: {value}")
            print(vars(value))
            
# Define the function to print "Hello, World!"
def print_hello(**kwargs):
    print_nested_kwargs(kwargs)
    print("end here", datetime.now())

# Instantiate the DAG
dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple DAG that prints Hello, World!',
    schedule_interval='@daily',  # Execute daily
)

# Define the task to print "Hello, World!"
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

# Define the task dependencies
hello_task
