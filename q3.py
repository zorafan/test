import requests
from bs4 import BeautifulSoup


def gettitle():
    url = 'https://www.nytimes.com'
    reqs = requests.get(url)

    headinglist = []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('h3', class_='e1lsht870'):
        headinglist.append(title.get_text())

    length = len(headinglist)
    i = 0
    for i in range(length):
        print(headinglist[i])
        i = i + 1


gettitle()
