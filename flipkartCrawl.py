import urllib.request as url
import bs4,lxml
import webbrowser
def getData(path):
    res = url.urlopen(path)
    return bs4.BeautifulSoup(res,"lxml")

product = input("Enter Product Name : ").replace(" ","+")
path = "https://www.flipkart.com/search?q="+product
data = getData(path)
# # print(type(data))
# name = data.find("div",class_="KzDlHZ")
# print(name.text)
path = "https://www.flipkart.com"+data.find("a",class_="CGtC98")['href']
# webbrowser.open(path)
data = getData(path)
name=data.find("span",class_="VU-ZEz")
print("Product Name=>",name.text)
highlights_div=data.find("div",class_="xFVion")
li = highlights_div.findAll("li")
for i in li:
    print(i.text)

table = data.find("table",class_="_0ZhAN9")
tables = []
tr=table.findAll("tr")
for i in tr:
    tr_list = i.findAll("td")
    for j in range(len(tr_list)):
        tr_list[j] = tr_list[j].text
    tables.append(tr_list)

import pandas as pd
df = pd.DataFrame(tables)
print(df)
