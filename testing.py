from db_connection import engine
from pandas_data import read_hs_data, read_stp_mapping
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd



data_source = read_hs_data()
# days = data_source[["Score","Created"]].groupby(["Created"]).agg('count')
# print(days["Score"])


data = [{
    'x': data_source["Score"].agg('count'),
    'y': data_source["Created"]

} for day in data_source["Created"].unique()]


# scores_per_day = data_source.groupby("Created")["Score"].count().head()
# month_days = data_source['Created'].unique()
# print(scores_per_day)
