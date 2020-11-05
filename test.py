import sqlite3
import pandas as pd
import os

conn = sqlite3.connect('CSAT.db')
c = conn.cursor()
c.execute('SELECT * FROM stp')
print(c.fetchall())
conn.commit()
conn.close()
#
# stp_csv = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/STP.csv',
#     header=1, skip_blank_lines=True))
#
#
# stp_csv.to_sql('stp', conn, if_exists='replace', index = False)
