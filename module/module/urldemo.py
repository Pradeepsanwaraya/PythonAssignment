import urllib.request  
url="https://www.google.com"
response=urllib.request.urlopen(url)
print(response.status)
print(response.geturl())
print(response.read())