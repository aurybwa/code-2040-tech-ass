import requests

r = requests.post('http://challenge.code2040.org/api/register', data = {'token':'38df9b96ac91674fd872c4d7c5438e24', 'github':'https://github.com/aurybwa/code-2040-tech-ass'})

print r.status_code
print r.text
