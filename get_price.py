from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://info.monex.co.jp/service/fee/stock/index.html")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class" : "table-cmn_01 s-mb-10"})[0]

rows = table.findAll("tr")

count = 1
for r in rows:
    print("row", count)
    print(r)
   
    count+=1