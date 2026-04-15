from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
trows = tbody.contents
print(trows[0].parent)
print(trows[0].parent.name)
