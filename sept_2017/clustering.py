"""Wifi logs clusturing"""
from datetime import datetime
import glob
import re
from sklearn import cluster as skc
import pandas as pd
import seaborn as sns
sns.set()
# pylint: disable=invalid-name, line-too-long

### VAR ENV 
# test_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr\\20010828_agr.csv"
files_agr = glob.glob("C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity\\*.csv")
list_ = []

regex_date = r'\\([0-9]+)_agr.csv$'

for file_ in files_agr:
    match = re.search(regex_date, file_)
    date_obj = datetime.strptime(match.group(1), '%Y%m%d')
    if date_obj.weekday() == 6:
        df_tmp = pd.read_csv(file_)
        list_.append(df_tmp)

# print(list_)

df_global = pd.concat(list_)

# print(df_global.head())

df_learning = df_global.iloc[:, 1:]

print(df_learning.describe())

model = skc.KMeans(n_clusters=2)
# model = skc.DBSCAN(eps=0.3, min_samples=100)
# model = skc.Birch(n_clusters=3)

model.fit(df_learning)

print(model.labels_)

df_learning['Cluster'] = pd.Series(model.labels_, index=df_learning.index)

plot = sns.pairplot(df_learning, hue="Cluster")
plot.savefig("C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\plot\\activity_clu02_KMEAN_dimanche.png")
