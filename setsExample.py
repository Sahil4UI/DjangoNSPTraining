data1 = '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.'''
data2 = '''Django is a Python framework that makes it easier to create web sites using Python.
Django takes care of the difficult stuff so that you can concentrate on building your web applications.
Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).'''

#1 Tokenization
token1 = data1.split()
token2 = data2.split()
#2 Remove Stop Words
import nltk
# Natural Language processing Tool Kit
# nltk.download("stopwords")
from nltk.corpus import stopwords
st = stopwords.words("english")
print(len(token1))
set1 = set(token1)
set2 = set(token2)
for i in st:
    set1.discard(i)
    set2.discard(i)
# print(len(set1))
# Jaccards Index

res = (len(set1.intersection(set2))/len(set1.union(set2)))*100
print(res)
print(len(set1.intersection(set2)))
print(len(set1.union(set2)))


