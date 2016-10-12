import requests
import json

req = requests.post('http://challenge.code2040.org/api/prefix', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})

data=req.json()
pre=data["prefix"]
arr=data["array"]

nw_arr=[]

# append strings without the prefix to the new array
for i in arr[:]:
    if not i.startswith(pre):
        nw_arr.append(i)

# posting a request with the new array of strings without the prefix
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = {'token':'38df9b96ac91674fd872c4d7c5438e24','array':nw_arr})
print r.text
