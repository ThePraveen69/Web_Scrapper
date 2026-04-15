from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
trows = tbody.contents
prices={}
for tr in trows:
    for td in tr:
        print(td)
        print()
