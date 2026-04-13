from bs4 import BeautifulSoup
with open("index2.htm","r") as f:
    doc = BeautifulSoup(f,"html.parser")
tag = doc.find("option")
tags = doc.find_all("option")
print(tag)
print(tags)
