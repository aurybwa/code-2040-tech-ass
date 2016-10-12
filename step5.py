from datetime import timedelta
from datetime import datetime
import requests

req = requests.post('http://challenge.code2040.org/api/dating', data = {'token':'38df9b96ac91674fd872c4d7c5438e24'})

data=req.json()

datestamp=data["datestamp"]
interval=data["interval"]

# change the string datestamp into a datetime object
date = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')

# Get the duration of the seconds into a datetime object
seconds=timedelta(seconds=interval)

# adding datestamp and seconds
new_date=date+seconds

# change the new date object into a string
new_date_str=new_date.strftime('%Y-%m-%dT%H:%M:%SZ')

# posting a request with the new date
r = requests.post('http://challenge.code2040.org/api/dating/validate', data = {'token':'38df9b96ac91674fd872c4d7c5438e24','datestamp':new_date_str})
print r.text
