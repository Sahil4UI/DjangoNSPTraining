import urllib.request as url
import bs4
product = input("Enter Product Name : ")
path = "https://www.flipkart.com/search?q="+product
res = url.urlopen(path)
data = bs4.BeautifulSoup(res)
# print(type(data))
name = data.find("div",class_="KzDlHZ")
print(name.text)
 