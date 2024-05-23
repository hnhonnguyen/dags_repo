from airflow.decorators import task, dag
from datetime import datetime, timedelta
import pendulum

@dag(dag_id="param_dag",
     schedule="*/5 * * * *",
     start_date=datetime(2024,1,1),
     params={"name": "Nhon",
             "age": 18},
     default_args={
    "owner" : "Nhon",
    "retries" : 1,
    "retry_delay" : timedelta(minutes=1),
    "email":"hnhonnguyen@gmail.com"
})
def my_dag():
    @task
    def print_custom(**context):
        print("ahihi")
        print(context)

    print_custom()

my_dag()