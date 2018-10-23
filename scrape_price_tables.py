import pandas as pd
import os

base_path = 'csv'

if not os.path.exists(base_path):
    os.mkdir(base_path)


def get_price_sbi(url):
    path = base_path + '/SBI'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[1]
    yakujo.to_csv(path + '/現物取引_standard.csv', header=False, index=False, columns={0, 1})
    yakujo.to_csv(path + '/現物取引_active.csv', header=False, index=False, columns={2, 3})


def get_price_matsui(url):
    path = base_path + '/松井'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[0]

    yakujo.to_csv(path + '/1日の約定金合計金額.csv', index=False)


def get_price_gmo(url):
    path = base_path + '/GMO'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[0]
    tegaku = table[1]

    yakujo.to_csv(path + '/1約定ごとプラン.csv', header=False, index=False, columns={0, 1})
    tegaku.to_csv(path + '/1日定額プラン.csv', header=False, index=False, columns={0, 1})


def get_price_monex(url):
    path = base_path + '/マネックス'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    target = table[0]
    target.to_csv(path + '/monex_price.csv', header=False, index=False)


def get_price_rakuten(url):
    path = base_path + '/楽天'

    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)

    table[0].to_csv(path + '/現物_超割コース.csv', index=False)
    table[2].to_csv(path + '/現物_超割コース(大口).csv', index=False)

    table[4].to_csv(path + '/一日定額コース.csv', index=False)


monex = "https://info.monex.co.jp/service/fee/stock/index.html"
get_price_monex(monex)

rakuten = "https://www.rakuten-sec.co.jp/web/commission/"
get_price_rakuten(rakuten)

gmo = "https://www.click-sec.com/corp/guide/commission_list/"
get_price_gmo(gmo)

matsui = "https://www.matsui.co.jp/fee/"
get_price_matsui(matsui)

sbi = "https://www.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_home&cat1=home&cat2=price&dir=price&file=home_price.html"
get_price_sbi(sbi)



