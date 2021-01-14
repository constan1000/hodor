#!/bin/bash/python3
import requests 

url = "http://158.69.76.135/level1.php"
for i in range(0, 4096):
    requests.post(url, allow_redirects=False, data ={
	'id': 69,
	'holdthedoor': 'Submit'
    })
