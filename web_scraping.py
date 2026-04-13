from bs4 import BeautifulSoup
import requests
url ="https://www.newegg.com/tools/combo-builder/1740?cm_sp=homepage-pers-home%20dynamiccombo_pccomponent-amd-takeover"
result = requests.get(url)
print(result.text)
