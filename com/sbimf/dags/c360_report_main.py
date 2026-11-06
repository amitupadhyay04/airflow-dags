"""Sample DAG for the multi-bundle test - lives on the MAIN branch."""
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="c360_report_main",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["sbi-poc", "branch:main"],
)
def c360_report_main():
    @task
    def build_report():
        print("building report on branch main")

    build_report()


c360_report_main()
