"""Wifi logs clusturing"""
from datetime import datetime
import glob
import re
# from sklearn import cluster as skc
import pandas as pd
import seaborn as sns
import progressbar
sns.set()
# pylint: disable=invalid-name, line-too-long

### VAR ENV
# test_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr\\20010828_agr.csv"
files_raf = glob.glob(
    "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\csv\\*.csv")
list_ = []

regex_date = r'\\([0-9]+)_raf.csv$'
regex_bat = r'^([a-zA-Z]+)'

for file_ in files_raf:
    match = re.search(regex_date, file_)
    date_obj = datetime.strptime(match.group(1), '%Y%m%d')
    # Selection les csv correspondant à un jour de la semaine
    if date_obj.weekday() == 6 and date_obj.year == 2001:
        df_tmp = pd.read_csv(file_)
        list_.append(df_tmp)

# print(list_)
df_global = pd.concat(list_)
bar = progressbar.ProgressBar(max_value=df_global.shape[0])

col_co = ['Start', 'Batiment']
col_deco = ['End', 'Batiment']

df_co = pd.DataFrame()
df_deco = pd.DataFrame()

for i, row in bar(df_global.iterrows()):
    if row['Action'] == 'authenticated':
        match_co = re.search(regex_bat, row['Batiment'])
        df_co = df_co.append(pd.Series([row['Timestamp'], match_co.group(1)], index=col_co), ignore_index=True)
    if row['Action'] == 'deauthenticating':
        match_co = re.search(regex_bat, row['Batiment'])
        df_deco = df_deco.append(pd.Series([row['Timestamp'], match_co.group(1)], index=col_deco), ignore_index=True)
        # print(pd.Series([row['Timestamp'], match_co.group(1)], index=col_co))
        # break
    # print(match_bat.group(1))
    # df_global.set_value(i,'Batiment',match_bat.group(1))

df_co.to_csv(
    "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity_global\\co_dimanche_2001.csv")
df_deco.to_csv(
    "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity_global\\deco_dimanche_2001.csv")

print(df_co.head())
print(df_deco.head())



