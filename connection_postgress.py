# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:29:24 2021

@author: gendutkiy
"""

import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

PG_HOST = "27.112.79.65"
PG_DATABASE = "postgres"
PG_USER = "gendutkiy"
PG_PASSWORD = "spidey34."

try:
    connection = psycopg2.connect(
        host=PG_HOST,
        user=PG_USER,
        password=PG_PASSWORD,
        database=PG_DATABASE,
        port=5432
    )
    cursor = connection.cursor(cursor_factory=RealDictCursor)
except Exception as e:
    raise e