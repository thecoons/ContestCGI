'''Read data_log to convert it at csv file.'''
# pylint: disable=invalid-name, line-too-long
import re

# ENV_VARIABLE
# FIle Test : 20040227.log || 20010411.log
#file_test = "/home/thecoons/Documents/cgi_contest/sept_2017/data/syslog-v3.3/20040227.log"
# FIle Test : 20040610.log || 20010411.log
file_test = "C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\syslog-v3.3\\20040610.log"
# Regexp pour la 1er gen de log : timestamp, Ap_add, Action_string
regexp_v1 = r'^([\d]+) [\w]{3} [\d]{2} [\d:]+ ([\w]+) [\w]+ \(Info\): (.*)'
regexp_v2 = r'^([\d]+) [\w]{3} [\d]{2} [\d:]+ ([\w]+) [\d]+: [\w\.]* ?[\.\*]?[\w]{3} [\d]{1,2} [\d:\.]+ %[\w]+-[\d]+-([\w]+): (.*)'
# OPEN A FILE
fo = open(file_test, "r")
for count, line in enumerate(fo):
    # line = fo.readline()
    match = re.search(regexp_v1, line)
    if not match:
        match = re.search(regexp_v2, line)
    if match:
        # print('{0}\n{1}\n{2}\n'.format(match.group(1),
        #                                match.group(2),
        #                                match.group(3)))
        pass

    else:
        print(line)
        print("NO MATCH ####\n####\n####\n####\n")
