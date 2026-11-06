"""Sample DAG for the multi-bundle test - lives on the MAIN branch."""
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="c360_ingest_main",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["sbi-poc", "branch:main"],
)
def c360_ingest_main():
    @task
    def extract():
        return {"rows": 100, "branch": "main"}

    @task
    def load(payload: dict):
        print(f"loading {payload['rows']} rows from branch {payload['branch']}")

    load(extract())


c360_ingest_main()
