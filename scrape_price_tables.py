import pandas as pd
import os
import re

base_path = 'csv'

if not os.path.exists(base_path):
    os.mkdir(base_path)


def get_price_matsui(url):
    path = base_path + '/松井'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[0]
    yakujo.to_csv(path + '/1日の約定金合計金額.csv', index=False)
    return yakujo


def get_price_monex(url):
    path = base_path + '/マネックス'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    target = table[0]
    target.to_csv(path + '/monex_price.csv', header=False, index=False)
    return pd.read_csv(path + '/monex_price.csv')


def get_price_rakuten(url):
    path = base_path + '/楽天'

    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)

    table[0].to_csv(path + '/現物_超割コース.csv', index=False)

    return pd.read_csv(path + '/現物_超割コース.csv')


def get_price_gmo(url):
    path = base_path + '/GMO'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[0]
    yakujo.to_csv(path + '/1約定ごとプラン.csv', header=False, index=False, columns={0, 1})
    return pd.read_csv(path + '/1約定ごとプラン.csv')


def get_price_sbi(url):
    path = base_path + '/SBI'
    if not os.path.exists(path):
        os.mkdir(path)

    table = pd.io.html.read_html(url)
    yakujo = table[1]
    standard = path + '/現物取引_standard.csv'

    yakujo.to_csv(standard, header=False, index=False, columns={0, 1})
    pd.read_csv(standard).to_csv(standard, header=False, index=False)
    r9_removed = pd.read_csv(standard).drop(9);
    r9_removed.to_csv(standard, index=False)

    return r9_removed


def createCsv():
    matsui = "https://www.matsui.co.jp/fee/"
    matsui_fee = get_price_matsui(matsui)['手数料(税抜)']

    sbi = "https://www.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_home&cat1=home&cat2=price&dir=price&file=home_price.html"
    sbi_fee = get_price_sbi(sbi)['手数料']

    gmo = "https://www.click-sec.com/corp/guide/commission_list/"
    gmo_fee = get_price_gmo(gmo)['GMOクリック証券']


    rakuten = "https://www.rakuten-sec.co.jp/web/commission/"
    rakuten_fee = get_price_rakuten(rakuten)['新手数料']


    monex = "https://info.monex.co.jp/service/fee/stock/index.html"
    monex_fee_pc = get_price_monex(monex)['パソコン']
    monex_fee_phone = get_price_monex(monex)['スマートフォン用アプリ「マネックストレーダー株式 スマートフォン」、携帯電話（ガラケー）']


    index = ["5万円", "~10万円", "~20万円", "~30万円", "~40万円", "~50万円", "~100万円", "~150万円", "~200万円", "~3000万円", "3000万円超",
             "1億超"]
    cols = {"松井証券": ["", matsui_fee[0], "", matsui_fee[1], "", matsui_fee[2], matsui_fee[3], "", matsui_fee[4], "", "", matsui_fee[6]],
            "マネックス証券": ["", monex_fee_pc[0], monex_fee_pc[1], monex_fee_pc[2], monex_fee_pc[3], monex_fee_pc[4], monex_fee_pc[5], monex_fee_pc[6], monex_fee_pc[6], monex_fee_pc[6], monex_fee_pc[6], monex_fee_pc[6]],
            "楽天証券": [rakuten_fee[0], rakuten_fee[1], rakuten_fee[2], "", "", rakuten_fee[3], rakuten_fee[4], rakuten_fee[5], "", rakuten_fee[6], rakuten_fee[7], ""],
            "GMOクリック証券": ["", gmo_fee[0], gmo_fee[1], "", "", gmo_fee[2], gmo_fee[3], "", gmo_fee[4], gmo_fee[5], gmo_fee[6], ""],
            "SBI証券": [sbi_fee[0], sbi_fee[1], sbi_fee[2], "", "", sbi_fee[3], sbi_fee[5], sbi_fee[6], "", sbi_fee[7], sbi_fee[8], ""]}

    df = pd.DataFrame(cols, index=index)
    df.to_csv('csv/fee_comparison_table.csv')


createCsv()