from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime
with DAG(
    dag_id="backfill_dag",
    start_date=datetime.datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
)