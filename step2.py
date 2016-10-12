import requests

r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})

res= r.text
string=res[::-1]

r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token':'38df9b96ac91674fd872c4d7c5438e24','string':string})
print r.text
