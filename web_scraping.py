from bs4 import BeautifulSoup
with open("index2.htm","r") as f:
    doc = BeautifulSoup(f,"html.parser")
tags = doc.find_all(["p",'option','div'])
tag1 = doc.find_all(class_="btn-item")
print(tag1)
