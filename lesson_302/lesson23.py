import requests

url_1 = "https://jsonplaceholder.typicode.com/posts"

url_2 = "https://jsonplaceholder.typicode.com/comments"
qwery_params = {"postId": 100}
# currency=UAH&search[filter_float_price:from]=100000
olx_params = {"currency": "UAH", "search[filter_float_price:from]": 100000}
response = requests.get(url_2, params=qwery_params)

def post_out(response):
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    print("===================")
    print(response.url)
    print(response.status_code)
    print(response.headers)
    print(response.json())

#post_out(response)

post_url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    'Content-type': 'application/json; charset=UTF-8',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"
  }
data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
  }
response_post = requests.post(post_url, json=data, headers=headers)

post_out(response_post)

from urllib.parse import urlparse
    
url = "https://www.example.com/path/to/resource?param1=value1&param2=value2#id"

parsed_url = urlparse(url)

print("Схема:", parsed_url.scheme)
print("Мережева адреса:", parsed_url.netloc)
print("Шлях:", parsed_url.path)
print("Параметри:", parsed_url.params)
print("Запити:", parsed_url.query)
print("Фрагмент:", parsed_url.fragment)

from urllib.parse import urlunparse
    
scheme = "https"
netloc = "www.example.com"
path = "/path/to/resource"
params = "param1=value1"
query = "param2=value2"
fragment = "section"

composed_url = urlunparse((scheme, netloc, path, params, query, fragment))

print("Складений URL:", composed_url)
