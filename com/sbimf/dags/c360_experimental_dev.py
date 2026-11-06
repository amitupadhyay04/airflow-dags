"""Sample DAG that exists ONLY on the DEV branch (a feature-branch-only DAG)."""
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="c360_experimental_dev",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["sbi-poc", "branch:dev"],
)
def c360_experimental_dev():
    @task
    def try_new_logic():
        print("experimental logic, dev branch only")

    try_new_logic()


c360_experimental_dev()
