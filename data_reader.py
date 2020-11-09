import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine


param_dic = {
    "host"      : "localhost",
    "database"  : "happy_signals",
    "user"      : "postgres",
    "password"  : os.getenv('DB_PASS')
}

connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (
    param_dic['user'],
    param_dic['password'],
    param_dic['host'],
    param_dic['database']
)

engine = create_engine(connect)
