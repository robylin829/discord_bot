import json

def load(file_path):
  with open(file_path,mode='r',encoding='utf-8') as jfile:
      return json.load(jfile)

def save(file_path,jdata):
    with open(file_path,'w',encoding='utf-8') as jfile:
      json.dump(jdata,jfile,indent=4)
#id OTkyMDM5NDE0NDQ2NDI4MjAw.GmifAH.exynKvsEYKvmgJiK_gVl2e9Zzxnm9NR5wvj5Rc