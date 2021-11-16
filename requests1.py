import requests
# import requests module

import pip._vendor.requests
from pip._vendor import requests


  
# Making a get request
response = requests.get('https://github.com/ruchitiwari20012/PythonTraining-')
  
# print request object
print(response.url)
  
# print status code
print(response.status_code)