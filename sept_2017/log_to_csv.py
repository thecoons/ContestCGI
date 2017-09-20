'''Read data_log to convert it at csv file.'''
# pylint: disable=invalid-name, line-too-long
import re
import glob
import csv

####### ENV_VARIABLE

# FIle Test Unix: 20040227.log || 20010411.log
# file_test = "/home/thecoons/Documents/cgi_contest/sept_2017/data/syslog-v3.3/20040227.log"
# dir_log = "/home/thecoons/Documents/cgi_contest/sept_2017/data_test/"
# dir_csv = "/home/thecoons/Documents/cgi_contest/sept_2017/data_test/csv/"
## Regexp pour get le name du fichier
#regexp_filename = r'/([\w]+).log$'

# FIle Test Win: 20040610.log || 20010411.log
file_test = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\syslog-v3.3\\20040610.log"
dir_log = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data_test\\"
dir_csv = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data_test\\csv\\"
# Regexp pour get le name du fichier
regexp_filename = r'\\([\w]+).log$'

# Parsing logs files in a dir
dir_log_content = glob.glob(dir_log+'*.log')


# Regexp pour la 1er gen de log : timestamp, Ap_add, Action_string
regexp_v1 = r'^([\d]+) [\w]{3} +[\d]{1,2} [\d:]+ ([\w]+) [\w]+ \(Info\): (.*)'
regexp_v2 = r'^([\d]+) [\w]{3} +[\d]{1,2} [\d:]+ ([\w]+) [\d]+: [\w\.]* ?[\.\*]?[\w]{3} +[\d]{1,2} [\d:\.]+ %[\w]+-[\d]+-[\w]+: (.*)'

# Regexp pour les info => action, MAC
regexp_g3_v1 = r'Station (\w+) (\w+)'
regexp_g3_v2 = r'^(\w+) [from]* ?(\w+), reason'
regexp_g3_v3 = r'^Packet to client (\w+)'
regexp_g3_v4 = r'^Interface \w+, (\w+) Station (\w+)'

regexp_g3_trash = r'^(Disconnect remote|Interface Dot11Radio0, no SSIDs|Interface Dot11Radio0, unable|\w+: Drv Add|Detected probable reset|Interface Dot11Radio0, no radio|Interface Dot11Radio0, frequency|Interface Dot11Radio0, parent|Interface Dot11Radio0, upgrading|Interface Dot11Radio0, flashing|Successfully updated|Lost Association|Associated to Parent|Associate Response|Ethernet|Bound|Started|Stopped|Reassociate Response|Backbone)'
#### APP
for log_file in dir_log_content:
    ### Ouverture du fichier de log
    fo = open(log_file, "r")
    ### Récupération du nom du fichier courant
    match_name = re.search(regexp_filename, log_file)
    current_filename = match_name.group(1)
    ### Ouverture du csv de raffinement
    # co = csv.writer(open(dir_csv+current_filename+'_raf.csv','w'))
    # co.writerow(['Timestamp','AP','Action'])
    for count, line in enumerate(fo):
        # line = fo.readline()
        row_current = ['','','','']
        match = re.search(regexp_v1, line)
        if not match:
            match = re.search(regexp_v2, line)
        if match:
            # print('{0}\n{1}\n{2}\n'.format(match.group(1),
            #                                match.group(2),
            #                                match.group(3)))
            row_current[0], row_current[1] = match.group(1), match.group(2)
            info = match.group(3)
            match_info = re.search(regexp_g3_v1, info)
            if match_info:
                row_current[2], row_current[3] = match_info.group(1), match_info.group(2)
            if not match_info:
                match_info = re.search(regexp_g3_v2, info)
                if match_info:
                    row_current[2], row_current[3] = match_info.group(2), match_info.group(1)
            if not match_info:
                match_info = re.search(regexp_g3_v3, info)
                if match_info:
                    row_current[2], row_current[3] = match_info.group(1), match_info.group(2)
            if not match_info:
                match_info = re.search(regexp_g3_v4, info)
                if match_info:
                    row_current[2], row_current[3] = match_info.group(1), match_info.group(2)

            if not match_info:
                match_trash = re.search(regexp_g3_trash, info)
            # else:
            #     match_stx = re.search(r'^[a-zA-Z]+',match_info.group(1))
            # if not match_info:
            #     print(info)

            if match_info:
                print(row_current)
            
            # co.writerow([match.group(1),match.group(2),match.group(3)])

        else:
            print(line)
            print("NO MATCH ####\n####\n####\n####\n")
            break
    fo.close()
