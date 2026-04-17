from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
trows = tbody.contents
prices={}
for tr in trows[0:10]:
    name , price = tr.contents[2:4]
    final_name = name.p.string
    final_price = price.string
    prices[final_name] = final_price
print(prices)    
    
