from bs4 import BeautifulSoup
import re
with open("index2.htm","r") as f:
    doc = BeautifulSoup(f,"html.parser")
tags = doc.find_all(text = re.compile("\$.*"))
print(tags)
for tag in tags:
    print(tag.strip())
