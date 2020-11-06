import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine


hs_data_csv = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/STP.csv',
    header=0, skip_blank_lines=True))

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


hs_data_csv.to_sql('stp_mapping', con=engine, if_exists='replace', index = False)


# conn.commit()
# cur.close()
# conn.close()
