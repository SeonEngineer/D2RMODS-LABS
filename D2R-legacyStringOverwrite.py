# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


main_filename = 'item-names' + '.json'

#1 = 레거시, 2=레저렉션, 3=새로만드는파일 헷갈리지말것

filename1 = r"C:\Users\circi\Documents\python\번역변경\strings-legacy\\" + main_filename
filename2 = r"C:\Users\circi\Documents\python\번역변경\strings\\" + main_filename

filename3 = r"C:\Users\circi\Documents\python\번역변경\\" + main_filename

errname = r"C:\Users\circi\Documents\python\번역변경\errlist.txt"

file_1 = open(filename1, "r", encoding="UTF-8")
file_2 = open(filename2, "r", encoding="UTF-8")
file_3 = open(filename3, "w", encoding="UTF-8")
file_err = open(errname, "a", encoding="UTF-8")

f1_strs = file_1.readlines()
f2_strs = file_2.readlines()

idx_a = 0
idx_b = 0
data_list1=[]

id_org = ''
kokr_org = ''

id_new = ''
kokr_new = ''
for i in range(1,50000):
    data_list1.append('')


lineNum = 0
kokr_org = ''
for fstr in f1_strs:
    
    if fstr.find('"id"') > 0:
        idx_a = fstr.find('"id"') + 6
        idx_b = fstr.find(',')
        id_org = int(fstr[idx_a:idx_b])
    if fstr.find('"koKR"') > 0:
        idx_a = fstr.find('"koKR"') + 8
        idx_b = fstr.find("\",")+1
        kokr_org = fstr[idx_a:idx_b]
    if len(kokr_org) > 1:
        #print('id:', id_org, 'str=',kokr_org,  ' lineNum[idx]=', lineNum)
        data_list1[id_org] = kokr_org
        #print('입력id=', id_org, 'str=', kokr_org)
        kokr_org = ''
        
for fstr in f2_strs:
    if fstr.find('"id"') > 0:
        idx_a = fstr.find('"id"') + 6
        idx_b = fstr.find(',')
        id_new = int(fstr[idx_a:idx_b])
        #print(id_new)
    if fstr.find('"koKR"') > 0:
        idx_a = fstr.find('"koKR"') + 8
        idx_b = fstr.find('\",')
        kokr_new = fstr[idx_a:idx_b]
        #   print(data_list1[id_new])
        new_str = str(data_list1[id_new])
        if len(new_str) > 0:
            #print('id:', id_new, 'old_str=',data_list1[id_new],  ' newStr=',kokr_new)
            output_Str = "    \"koKR\": "+ new_str + ",\n"
            file_3.write(output_Str)
            
        else:
            print('id:', id_new ,' / 데이터가 없습니다 아래내용으로 입력합니다.')
            print(fstr)
            file_3.write(fstr)
            file_err.write(fstr)
    else:
        file_3.write(fstr)
        

file_1.close()
file_2.close()
file_3.close()
file_err.close()
