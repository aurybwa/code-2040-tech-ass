import requests

r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})

res= r.text

# reversing the string
string=res[::-1]

# posting a request with the reversed string
r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token':'38df9b96ac91674fd872c4d7c5438e24','string':string})
print r.text
