# import the required lib
print('_'*50)
#0. import bs4 BS url.request urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://simplilearn.com/resources'

webpage = urlopen(url)

#1. soup parser
sl_soup = BeautifulSoup(webpage,'html.parser')

webpage.close()

# print(sl_soup.contents)

# print(sl_soup.prettify)

print('_'*30+'title'+'_'*30)
print(sl_soup.title)

print('_'*30+'href'+'_'*30)
for href in sl_soup.findAll("a",href=True):
    print(href["href"])


print('_'*30+'findAll_h2'+'_'*30)
for article in sl_soup.findAll("h2"):
    print(article.string)

print('_'*30+'findAll("h4")'+'_'*30)

for article_topic in sl_soup.findAll("h4"):
    print(article_topic.string)

print('_'*30+'url2'+'_'*30)

url2="https://www.simplilearn.com/what-is-tensorflow-article?source=frs_home"

webpage2 = urlopen(url2)

sl_article=BeautifulSoup(webpage2,"html.parser")

test = sl_article.find(class_="desig_author empty-text")

# print(type(test))

print(test.findAll("p"))

print('_'*60)
first_next_p = test.p

print(first_next_p)
print('_'*60)

find_next_sibling=first_next_p.next_sibling.next_sibling
print(find_next_sibling)
print('_'*60)

print(find_next_sibling.previous_sibling.previous_sibling)  