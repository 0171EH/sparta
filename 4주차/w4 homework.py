import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client=MongoClient('localhost', 27017)
db=client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

rank = 1
for i in range(len(soup.find_all(class_='title ellipsis'))):
    title = soup.find_all(class_='title ellipsis')[i].get_text().strip()
    artist = soup.find_all(class_='artist ellipsis')[i].get_text()
    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.geniemusic.insert_one(doc)
    rank += 1

