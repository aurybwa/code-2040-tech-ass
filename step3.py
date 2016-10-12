import requests

req = requests.post('http://challenge.code2040.org/api/haystack', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})

data=req.json()
needle=data["needle"]
haystack=data["haystack"]

# getting index of 'needle' in the 'haystack' array
ind = haystack.index(needle)

# posting a request with the index of 'needle' in the 'haystack' array
r = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':'38df9b96ac91674fd872c4d7c5438e24','needle':ind})
print r.text
