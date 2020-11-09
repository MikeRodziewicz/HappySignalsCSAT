from db_connection import engine
from pandas_data import read_hs_data, read_stp_mapping



def main():
    read_hs_data().to_sql('hs_data_raw', con=engine, if_exists='replace',
                            index = False)
    read_stp_mapping().to_sql('stp_mapping', con=engine, if_exists='replace',
                            index = False)


if __name__ == '__main__':
    main()
