from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
tbody = doc.tbody
print(tbody.prettify())
