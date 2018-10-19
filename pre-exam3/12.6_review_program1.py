# file_list = ['data_1.csv','data_1.csv','data_3.csv']
# final_list = []
# for i in file_list:
#     key = open(i)
#     for line in key:
#         row = line.strip().split(',')

import re

file_list=['data_1.csv','data_2.csv', 'data_3.csv']
gradebook= {}
for file_name in file_list:
    data_file = open(file_name)
    for line in data_file:
        split_line = line.split(',')
        if split_line[0] not in gradebook:
            gradebook[split_line[0]] = []
        i = 1
        while i<len(split_line):
            gradebook[split_line[0]].append(int(split_line[i]))
            i +=1
    data_file.close()

for id in gradebook:
    student = id + ','
    for score in gradebook[id]:
        student += str(score) +','
    print(student[:-1])

text = 'akjghe mq dklj djw'
finder = re.compile(r'[a-z]{2,3}')
for m in finder.finditer(text):
   print(m.group())



