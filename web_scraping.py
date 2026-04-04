from bs4 import BeautifulStoneSoup

with open("index.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")
