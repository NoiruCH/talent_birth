
import click
from talent_birth.request import get_birth

query = input('Please type here: ')
url = "https://ja.wikipedia.org/wiki/" + query
# my_birth = "2005-1-11"

@click.command() # 以下の関数をdecoratorで修飾してる
@click.option("--url", "-m",default=url,
              show_default=True, help="タレントと誕生日を比較")
@click.option("--my_birth", prompt='Your birth', help="xxxx-yy-zzの形で入力してね") # optionが引数に渡される
def cli(url, my_birth):
    get_birth(url, my_birth) # 引数は定数を定義するファイルとで分離する必要がある



