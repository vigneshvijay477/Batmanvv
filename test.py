import requests

x = requests.get('https://w3schools.com/python/dempage.htm')

#print(x.text)
print(x.status_code)
