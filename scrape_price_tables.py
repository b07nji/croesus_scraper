import pandas as pd
import os

base_path = 'csv'

if not os.path.exists(base_path):
    os.mkdir(base_path)

def get_price_monex(url):
    path = base_path + '/マネックス'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    target = table[0]
    target.to_csv(path + '/monex_price.csv')


def get_price_rakuten(url):
    path = base_path + '/楽天'

    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)

    table[0].to_csv(path + '/現物_超割コース.csv')
    table[2].to_csv(path + '/現物_超割コース(大口).csv')

    table[1].to_csv(path + '/信用取引_超割コース.csv')
    table[3].to_csv(path + '/信用取引_超割コース(大口).csv')

    table[4].to_csv(path + '/一日定額コース.csv')


monex = "https://info.monex.co.jp/service/fee/stock/index.html"
get_price_monex(monex)

rakuten = "https://www.rakuten-sec.co.jp/web/commission/"
get_price_rakuten(rakuten)








