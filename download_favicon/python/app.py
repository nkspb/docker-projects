from sys import argv
from requests import get

url = argv[1] + '/favicon.ico'
response = get(url)
open('/downloads/favicon.ico', 'wb').write(response.content)