from airflow.decorators import dag, task
import time
import datetime
import pendulum
from airflow import Dataset

def sla_callback(dag, task_list, blocking_task_list, slas, blocking_tis):
    print(
        "The callback arguments are: ",
        {
            "dag": dag,
            "task_list": task_list,
            "blocking_task_list": blocking_task_list,
            "slas": slas,
            "blocking_tis": blocking_tis,
        },
    )

my_file = Dataset("/tmp/my_fule.txt")

@dag(
    schedule=[my_file],
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    sla_miss_callback=sla_callback,
    default_args={"email": "vn3848587@gmail.com"},
)
def example_sla_dag():
    @task(sla=datetime.timedelta(seconds=10))
    def sleep_20():
        """Sleep for 20 seconds"""
        time.sleep(20)

    @task
    def sleep_30():
        """Sleep for 30 seconds"""
        time.sleep(30)

    sleep_20() >> sleep_30()


example_dag = example_sla_dag()
