from db_connection import engine
from pandas_data import read_hs_data, read_stp_mapping
import plotly.offline as pyo
import plotly.graph_objs as go

#
# def main():
#     read_hs_data().to_sql('hs_data_raw', con=engine, if_exists='replace',
#                             index = False)
#     read_stp_mapping().to_sql('stp_mapping', con=engine, if_exists='replace',
#                             index = False)


# data_y = data_source['Created']
#
# data_x = data_source["Score"]
# result = []
#
# print(data_x)
#
#
# for day in data_y:
#     trace = go.Scatter(x=data_x,
#                         y=data_y,
#                         mode='lines',
#                         name=day)
#     result.append(trace)


#
# if __name__ == '__main__':
#     print(main())


data_source = read_hs_data()

data = [{
    'x': data_source["Created"],
    'y': data_source["Score"]

} for day in data_source["Created"].unique()]

layout = go.Layout(title='csat scores')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
