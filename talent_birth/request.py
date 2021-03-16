
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

### request web page

def get_birth(url, my_birth):
    """ wikipediaから誕生日情報を取得する """
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    birth = soup.find(class_="bday")
    birth = str(birth.text)
    date_birth = dt.strptime(birth, '%Y-%m-%d')
    date_my_birth = dt.strptime(my_birth, '%Y-%m-%d')
    date_diff = date_my_birth - date_birth
    if abs(date_diff.days) < 3650:
        print()
        print(date_diff.days // 365, '年差')
        print('歳の差は10年もないから、大丈夫！')
    else:
        print()
        print(date_diff.days // 365, '年差')
        print('ちょっと歳が離れすぎかなぁ。。。')



