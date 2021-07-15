import requests
from bs4 import BeautifulSoup
from .models import Event

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&page=1&PageSize=10"

def fetchEvent():
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text,"html.parser")
    tags = soup.find(id='ContentPlaceHolder1_gvIndex')
    List = tags.find_all('tr')
    List.pop(0)
    for i in range(10):
        if Event.objects.filter(title = List[i].find('a').text):
            return
        date = List[i].find(align="center").text.split('-')
        date[0] = str(int(date[0]) + 1911)
        e = Event(
            date = '-'.join(date),
            title = List[i].find('a').text,
            link = f"https://www.edu.tw/{List[i].find('a')['href']}",
            unit = List[i].find(align="left").text
        )
        e.save()
    return