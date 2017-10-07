import requests

headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

url = 'https://imgsa.baidu.com/forum/w%3D580%3B/sign=82dfc02bbb7eca80120539efa11896dd/77c6a7efce1b9d16cd34fc69f8deb48f8d5464c2.jpg'

response = requests.get(url, headers=headers)
html = response.content
with open('picture_1.jpg', 'wb') as f:
    f.write(html)