from urllib.parse import urlparse

url = "https://www.example.com/products?id=10"
data = urlparse(url)

print("Scheme:", data.scheme)
print("Domain:", data.netloc)
print("Path:", data.path)
print("Query:", data.query)
