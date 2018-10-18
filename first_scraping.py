from urllib.request import urlopen
from bs4 import BeautifulSoup

monex = "https://info.monex.co.jp/service/fee/stock/index.html"

html = urlopen(monex)
obj = BeautifulSoup(html.read(), features="html.parser")
target = obj.find_all(class_="table-cmn_01 s-mb-10")

print(len(target))

for table in obj.find_all(class_="table-cmn_01 s-mb-10"):
    print(table)


