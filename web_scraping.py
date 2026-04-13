from bs4 import BeautifulSoup
with open("index2.htm","r") as f:
    doc = BeautifulSoup(f,"html.parser")
tag = doc.find("option")
tag["selected"] = "false"
tag['value'] = "praveen"
print(tag)
