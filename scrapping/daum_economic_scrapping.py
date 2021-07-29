from bs4 import BeautifulSoup
import requests
import sqlite3

res = requests.get('http://media.daum.net/economic/')

if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', class_='link_txt')
    connect = sqlite3.connect('../db.sqlite3')
    cursor = connect.cursor()
    for link in links:
        title = str.strip(link.get_text())
        href = str.strip(link.get('href'))
        try:
            cursor.excute(
                "insert into polls_economics(create_data,href,title)values(datetime('now'),?,?)", (href,title)
            )
            print(title, ' : ', href)
        except:
            pass

    connect.commit()