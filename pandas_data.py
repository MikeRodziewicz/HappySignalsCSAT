import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


def read_hs_data():
    hs_data_raw = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/hs_data.csv',
        header=0, skip_blank_lines=True))
    hs_data_raw['Created'] = hs_data_raw['Created'].str[:11]
    hs_data_raw.drop(['Unnamed: 31','Unnamed: 32'], axis='columns', inplace=True)
    return hs_data_raw


def read_stp_mapping():
    stp_mapping = pd.DataFrame(pd.read_csv(f'/home/mike/Documents/Python/HappySignals/sanitizeddata/STP.csv',
        header=0, skip_blank_lines=True))
    return stp_mapping


# print(read_stp_mapping())
print(read_hs_data())


class Date_Stamps():

    the_date = None

    def __init__(self):
        self.time = date.today()

    def get_today(self):
        return self.time

    def get_yesterday(self):
        the_date = self.time - timedelta(days=1)
        return the_date

    def count_in_weekend(self):
        if self.time.isoweekday() == 1:
            the_date = self.time - timedelta(days=3)
            return the_date
        else:
            the_date = self.time - timedelta(days=1)
            return the_date

    def get_start_month(self):
        the_date = self.time.replace(day=1)
        return the_date

    def __str__(self):
        return f'today is {self.time}'
