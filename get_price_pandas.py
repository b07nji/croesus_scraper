import pandas 

url = "https://info.monex.co.jp/service/fee/stock/index.html"
table = pandas.io.html.read_html(url)
#test = pandas.io.html.read_html("https://www.bloomberg.co.jp/")

price_per_order = table[0][0]
pc = table[0][1]
phone = table[0][2]

for value in price_per_order:
    print(value)
    
    
for value in pc:
    print(value)
    
    
for value in phone:
    print(value)
    
    
    