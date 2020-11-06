import sqlite3
import pandas as pd
import os

conn = sqlite3.connect('CSAT.db')
c = conn.cursor()
# c.execute("""
# SELECT * FROM stp_mapping
# """)

# stp_csv = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/STP.csv',
#     header=0, skip_blank_lines=True))
#
# stp_csv.to_sql('stp_mapping', conn, if_exists='replace', index = False)
# print(c.fetchall())
# conn.commit()

hs_data_csv = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/Sep_INC_data.csv',
    header=0, skip_blank_lines=True))

hs_data_csv.to_sql('remedy_inc', conn, if_exists='replace', index = False)


conn.commit()
conn.close()
