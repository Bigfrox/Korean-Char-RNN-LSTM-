#! auto merging
import os
import datetime

filepath = "D:/Yonsei/ai/hw5/sample2/"

file_list = os.listdir(filepath)

#print(file_list)
now = datetime.datetime.now()
merged = ""
for file in file_list:
    with open(filepath+file,'r',encoding='utf-8') as f:
        text = f.read()
        text.strip()
        merged += text
    f.close()
    print("merge length : ", len(merged))

filename = 'new_merged_'+now.strftime("%Y_%m_%d_%H_%M")+'_.txt'
print(filename)
output_file = open(filename, 'w', encoding='utf-8')
output_file.write(merged)
output_file.close()
print("DONE")