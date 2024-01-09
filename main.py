import requests
from send_email import send_email

api_key = "cc761e6f33d1464c9edc8e58403c3dc9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-08&sortBy=publishedAt&apiKey=cc761e6f33d1464c9edc8e58403c3dc9&language=en"

request = requests.get(url)
content = request.json()

body=''
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + str(article["description"]) + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

