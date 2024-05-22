from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="backfill_dag",
    catchup=False,
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
)