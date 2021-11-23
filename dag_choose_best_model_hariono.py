# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:40:28 2021

@author: gendutkiy
"""

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, timedelta

def _choose_best_model():
    accuracy = 5
    if accuracy > 5:
        return 'accurate'
    else:
        return 'inaccurate'


default_args = {
    'owner': 'hariono',
    'depends_on_past': False,
    'email_on_failuer': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

with DAG('dag_choose_best_model_hariono',
    start_date=datetime(2021,10,27),
    default_args=default_args
) as dag:
    t0 = DummyOperator(
        task_id='start'
    )

    t1 = BranchPythonOperator(
        task_id='choose_best_model',
        python_callable=_choose_best_model
    )

    t2 = DummyOperator(
        task_id='accurate'
    )

    t3 = DummyOperator(
        task_id='inaccurate',
    )

    t0 >> t1 >> [t2, t3]
