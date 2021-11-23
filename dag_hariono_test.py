# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:13:35 2021

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
    'retry_delay': timedelta(minutes=3)
}

with DAG('dag_ds_intro_rian_pauzi',
    start_date=datetime(2021,10,26),
    default_args=default_args
) as dag:
    t0 = DummyOperator(
        task_id='start'
    )
    t2 = BashOperator(
        task_id='print_status',
        bash_command='echo testing...harionooooo'
    )

    t0 >>  t2