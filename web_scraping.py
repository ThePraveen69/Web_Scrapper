from bs4 import BeautifulSoup
import requests
url ="https://www.newegg.com/gigabyte-gv-n3080vision-oc-10gd-geforce-rtx-3080-10gb-graphics-card-windforce-3x/p/N82E16814932460"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
prices = doc.find_all(text ="$")
print(prices)
