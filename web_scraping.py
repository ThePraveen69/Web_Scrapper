from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
trows = tbody.contents
print(trows[0])
print(trows[0].next_sibling)
print(trows[1].previous_sibling)
print(list(trows[0].next_siblings))
