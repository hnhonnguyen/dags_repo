# Airflow DAGs — Spark on Kubernetes

A collection of Airflow DAGs used to run PySpark jobs on Kubernetes with the
`SparkKubernetesOperator`, plus examples of parameterized DAGs, task groups,
and backfills.

## DAGs and files

| File | What it shows |
| --- | --- |
| `spark_operator.py` | Submits `spark8s/spark-k8s.yaml` via `SparkKubernetesOperator` into the `spark-operator` namespace |
| `param_dag.py`, `test_params.py` | DAG-level `params` and Airflow `Variable` usage |
| `group_dag_test.py` | Task groups |
| `backfill.py` | Backfill workflow |
| `second_dags.py`, `nhon_test_dags.py`, `test.py` | Smaller examples and scratch DAGs |
| `spark8s/spark-k8s.yaml` | `SparkApplication` manifest submitted by the operator |
| `pyspark/pyspark_scripts/basic_spark.py` | The PySpark job itself |

## How the Spark DAG works

`spark_operator.py` first checks that the manifest exists
(`/opt/airflow/dags/repo/spark8s/spark-k8s.yaml` — the `git-sync` mount
convention), then submits it with `SparkKubernetesOperator` using the
`kubernetes_default` connection in the `spark-operator` namespace. The
`SparkApplication` runs `basic_spark.py` on the cluster.

## Prerequisites

- Airflow 2.x with `apache-airflow-providers-cncf-kubernetes`
- A Kubernetes cluster with the Spark Operator installed
  (`spark-operator` namespace)
- This repository synced to `/opt/airflow/dags/repo` (or adjust
  `template_searchpath` in the DAG)

## Notes

These DAGs are examples written while exploring Airflow + Spark Operator
patterns — adapt naming, schedules, and connections before production use.
