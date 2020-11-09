import pandas as pd
import os



def read_hs_data():
    hs_data_raw = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/hs_data.csv',
        header=0, skip_blank_lines=True))
    hs_data_raw['Created'] = hs_data_raw['Created'].str[:11]
    return hs_data_raw


def read_stp_mapping():
    stp_mapping = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/STP.csv',
        header=0, skip_blank_lines=True))
    return stp_mapping
