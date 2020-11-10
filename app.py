from db_connection import engine
from pandas_data import read_hs_data, read_stp_mapping
import plotly.offline as pyo
import plotly.graph_objs as go


# def main():
    # read_hs_data().to_sql('hs_data_raw', con=engine, if_exists='replace',
    #                         index = False)
    # read_stp_mapping().to_sql('stp_mapping', con=engine, if_exists='replace',
    #                         index = False)
    #

data_source = read_hs_data()
data_x = data_source['Score']
data_y = data_source["Reassignment Count"]

done = [go.Scatter(x=data_x,y=data_y,mode='markers')]
pyo.plot(done)

#
# if __name__ == '__main__':
#     print(main())
