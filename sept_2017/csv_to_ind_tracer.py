'''Organize to tracker.'''
import glob
import os
import re
import csv
import progressbar as prb
import pandas as pd

# Format Vecteur ['AcadBldg', 'ResBldg', 'LibBldg', 'SocBldg', 'AdmBldg', 'OthBldg', 'AthBldg']

# pylint: disable=invalid-name, line-too-long
### Env Variables Windows
csv_ref_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\csv\\"
user_tracker_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\tracker\\"
user_agr_path = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity\\"

regexp_filename = r'\\([\w]+)_raf.csv$'

csv_dir_content = glob.glob(csv_ref_path + '*.csv')

regexp_building = r'^([A-Za-z]+)[0-9]+'

bar = prb.ProgressBar()

for csv_file in bar(csv_dir_content):
    match_name = re.search(regexp_filename, csv_file)
    current_filename = match_name.group(1)
    
    # os.makedirs(user_tracker_path+current_filename)

    co = csv.writer(open(user_agr_path+current_filename+"_agr.csv", "w"))
    co.writerow(['Mac_ID', 'AcadBldg', 'ResBldg', 'LibBldg', 'SocBldg', 'AdmBldg', 'OthBldg', 'AthBldg'])

    df_csv = pd.read_csv(csv_file)
    df_grouped_mac = df_csv.groupby('Mac')
    for name, group in df_grouped_mac:
        # group.to_csv(user_tracker_path+current_filename+"\\"+name+"_trk.csv", index=False)
        # print(group)
        current_build = ''
        start_time = -1
        end_time = -1
        dict_build = {
            'AcadBldg' : [],
            'ResBldg' : [],
            'LibBldg' : [],
            'SocBldg' : [],
            'AdmBldg' : [],
            'OthBldg' : [],
            'AthlBldg' : []
        }
        for idx, row in group.iterrows():
            match_build = re.search(regexp_building, row['Batiment'])
            # print('{0} {1}'.format(row['Timestamp'], row['Batiment']))
            if match_build.group(1) != current_build and current_build != '':
                if start_time != end_time:
                    dict_build[current_build].append([start_time, end_time])
                current_build = match_build.group(1)
                start_time = row['Timestamp']
                end_time = row['Timestamp']
            elif current_build == '':
                current_build = match_build.group(1)
                start_time = row['Timestamp']
                end_time = row['Timestamp']
            else:
                end_time = row['Timestamp']
        if start_time != end_time:
            dict_build[current_build].append([start_time, end_time])
        # print(dict_build)
        dict_return = {}
        for key, item in dict_build.items():
            sum_mesure = 0
            sum_quo = 0
            for snap in item:
                sum_mesure += snap[0]
                sum_quo += snap[1] - snap[0]
            if sum_quo != 0:
                dict_return[key] = sum_quo
            else:
                dict_return[key] = 0
        # print(dict_return)
        # print([x for x, y in dict_return.items()])
        co.writerow([name]+[y for x, y in dict_return.items()])
        # print([name]+[y for x, y in dict_return.items()])
         
