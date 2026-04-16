from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
trows = tbody.contents
prices={}
for tr in trows:
    name , price = tr.contents[2:4]
    print(name)
    print()
