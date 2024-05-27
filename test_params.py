from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


default_args = {
    "owner": "airflow",
    "email": "vn3848587@gmail.com",
    "email_on_failure": False,
    "email_on_retry": False,
}
with DAG(
    dag_id="python_operator_dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
) as dag:

    def print_hello(ds):
        print(f"Hello world! {ds}")

    task = PythonOperator(task_id="print_hello", python_callable=print_hello)

    task
