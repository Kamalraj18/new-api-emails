import requests

api_key = "cc761e6f33d1464c9edc8e58403c3dc9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-08&sortBy=publishedAt&apiKey=cc761e6f33d1464c9edc8e58403c3dc9"

request = requests.get(url)
content = request.json()

for articles in content["articles"]:
    print(articles["title"])


