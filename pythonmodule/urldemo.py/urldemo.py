# import urllib.request

# url = "https://example.com"
# response = urllib.request.urlopen(url)

# print("Status:", response.status)
# print("URL opened successfully")
import urllib.request

response=urllib.request.urlopen("https://google.com")
print(response)