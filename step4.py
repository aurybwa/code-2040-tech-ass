import requests
import json

req = requests.post('http://challenge.code2040.org/api/prefix', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})
# print req.status_code
print req.text

data=req.json()
pre=data.get("prefix")
arr=data.get("array")

nw_arr=[]

for i, item in enumerate(arr):
    if not item.startswith(pre):
        nw_arr.append([item])

print nw_arr
# arrv=json.dumps(nw_arr, ensure_ascii=False)
# print arrv[1]


# r = requests.post('http://challenge.code2040.org/api/prefix/validate', data = {'token':'38df9b96ac91674fd872c4d7c5438e24','array':arrv})
# print r.status_code
# print r.text
