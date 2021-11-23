# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:38:14 2021

@author: gendutkiy
"""

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

def retrieve_data(url, filename):
  result = requests.get(url).json()
  textfile = open(filename+".txt", "w")
  for element in result:
      print(element)
      textfile.write(str(element) + ",\n")
  textfile.close()

default_args = {
    'owner': 'hariono',
    'depends_on_past': False,
    'email_on_failuer': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

with DAG('dag_ds_intro_hariono',
    start_date=datetime(2021,10,27),
    default_args=default_args
) as dag:
    t0 = DummyOperator(
        task_id='start'
    )

    t1 = PythonOperator(
        task_id='retrieve_todo_list',
        python_callable=retrieve_data,
        op_kwargs={'url':'https://jsonplaceholder.typicode.com/todos', 'filename':'file_result_rian'}
    )

    t2 = BashOperator(
        task_id='print_status',
        bash_command='echo `Data sudah ditarik dan berhasil disimpan pada file`'
    )

    t0 >> t1 >> t2
