import pandas as pd
import datetime

TRAIN_FILE = 'input/train.csv'


# x0: 2017-11-06 14:32:21 -> 2017-11-08 16:00:00
# x1: 2017-11-09 04:00:00 -> 2017-11-09 15:00:00
#
# def read_train_data_from_specfic_hours(df_all_hours):
#     TRAIN_HOURS_END = datetime.datetime(2017, 11, 8, 16, 0, 0)
#     VALID_HOURS_START = datetime.datetime(2017, 11, 9, 4, 0, 0)
#     VALID_HOURS_END = datetime.datetime(2017, 11, 9, 15, 0, 0)
#     df_all_hours[df_all_hours.]
#     # valid_df = df[
#     #     (df.click_time > date.datetime(2017, 11, 9, 4, 0, 0)) & (df.click_time < date.datetime(2017, 11, 9, 15, 0, 0))]
#     return df


# def get_sample_data_from_df():
#     return df
#
#
# def save_to_sample_file():
#     return df


def read_train_file(train_file):
    df = pd.read_csv(train_file)
    return df


df_raw = read_train_file(TRAIN_FILE)
df_raw.describe()
# df_specific_hours = read_train_data_from_specfic_hours(df)
