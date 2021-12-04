# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:51:17 2021

@author: circi
"""
import json

#내가쓰던거
path_myUi = r"data\my_ui.json"
#새로운 버전
path_D2R_patch = r"data\ui_patched.json"
#출력될곳
path_export = r"data\ui_export.json"

data1 = []
data2 = []
data1idList = []

with open(path_myUi, encoding="UTF-8-sig") as f_org:
    data1 = json.load(f_org)
    for datas in data1:
        data1idList.append(datas.get("id"))
 
with open(path_D2R_patch, encoding="UTF-8-sig") as f_org:
    data2 = json.load(f_org)
    
for index, datas in enumerate(data2):
    data_id = datas.get("id")
    if not data_id in data1idList:
        print(index, "-",  data_id, "-", datas.get("koKR"))
        data1.append(data2[index])
        
with open(path_export, 'w', encoding="UTF-8-sig") as f_org:
    #json.dump(data2, f_org, indent = 2, ensure_ascii = False)
    f_org.write('[\n')
    for datas in data1:
        f_org.write('  {\n')
        for key, value in datas.items():
            if type(value) is str:
                value = value.replace('\n','\\n')
                value = value.replace('\"','\\"')
                value = value.replace('\uE01D','\\uE01D')
            if key == 'id':
                f_org.write('    "%s": %s,\n' % (key, value))
            elif key == list(datas)[-1]:
                f_org.write('    "%s": "%s"\n' % (key, value))
            else:
                f_org.write('    "%s": "%s",\n' % (key, value))
                
        if datas is data1[-1]:
            f_org.write('  }\n')
        else:
            f_org.write('  },\n')
    f_org.write(']')
