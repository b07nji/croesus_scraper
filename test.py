import pandas as pd
import os


tables = pd.read_html("https://www.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_home&cat1=home&cat2=price&dir=price&file=home_price.html")

yakujo = tables[1]

#yakujo_a = tables[1]

yakujo.to_csv('sbi_test.csv')

