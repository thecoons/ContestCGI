import pandas as pd
import csv
import os
import glob
import re
# pylint: disable=invalid-name, line-too-long
### Env Variables Windows
csv_ref_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data_test\\csv\\"
user_tracker_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data_test\\tracker\\"

regexp_filename = r'\\([\w]+)_raf.csv$'

csv_dir_content = glob.glob(csv_ref_path + '*.csv')

for csv_file in csv_dir_content:
    match_name = re.search(regexp_filename, csv_file)
    current_filename = match_name.group(1)
    os.makedirs(user_tracker_path+current_filename)
    df_csv = pd.read_csv(csv_file)
    df_grouped_mac = df_csv.groupby('Mac')
    for name, group in df_grouped_mac:
        group.to_csv(user_tracker_path+current_filename+"\\"+name+"_trc.csv", index=False)
