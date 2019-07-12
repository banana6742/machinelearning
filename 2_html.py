#import the BS4
from bs4 import BeautifulSoup 

#import the web scraping example htmlxfile as per your location

Hfile ="C:/Users/banan/Desktop/webscrape/webhtml.html"
with open(Hfile,"r") as organization:
    soup = BeautifulSoup(organization,"html.parser")

#view the contents from the soup
print(soup.contents)

#search the content of the soup object
tag_li=soup.find("li")

#click object type
print(type(tag_li))
print('______print object_roz__________')

print(tag_li)

print('_______start search in the tree by find method________')


#select the 'HR' id
find_id=soup.find(id="HR")
#print the associated

print(find_id)

print('---------------------------------------')

#print the string value

print(find_id.li.div.string)

print('_________***____________')

#search for the particular css attr
search_for_stringOnly = soup.find(text=['Lohit','Kota'])
print(search_for_stringOnly)

print('_________???___________')
search_for_stringOnly = soup.findAll(text=['Lohit','Kota'])
print(search_for_stringOnly)

print('-'*40)
#to get the 'class' of 'ITmanager'

css_class_search = soup.find(attrs={'class':'ITManager'})

print(css_class_search)

print('______is_acconunt_manager_______')

# create a function to search the document based on the name

def is_account_manager(tag):
    return tag.has_attr("id") and tag.get("id")=="Finance"

#I'm using find method to get it id and id ='finance'
is_account_manager = soup.find(is_account_manager)

#view the account manager string name 

print(is_account_manager.li.div.string)
print('-'*40)

#this will give you all the tag with there string names
for tag in soup.findAll(True):
    print(tag.name)

print('_'*50)
print('_________HRManager______________')


#this step to get class of HRManager
#this is preasent as list

find_class = soup.findAll(class_="HRManager")
print(type(find_class))

print('_'*50)

#now im printing the HRManager Tag index of 0

print(find_class[0])
print('_'*50)
print(find_class[1])
print('_'*50)

print(find_class[0:])
print('_'*50)

find_class = find_class[0]

find_parent = find_class.find_parents("div")#liやulやdivに変えてみよう

print(find_parent)
print('_'*50)
print('_'*50)
print('_'*50)
print('_'*50)

do_it = soup.findAll(class_='ACTManager')
find1 = do_it[0]
find_para=find1.find_parents('ul')
print(find_para)
print('_'*50)
print('_'*50)



org = soup.find(attrs={'class':"ok"})
# org = soup.find(id="HR")
print(org)
print('________________________')

#below

next_sibling = org.findNextSiblings()

print(next_sibling)
print('_'*50)
print('_'*50)

#print parents
parent = org.find_parent
print(parent)


print('_'*50)
print('_'*50)
print('_'*50)

#search all previous tags
all_previous=org.findAllPrevious()
print(all_previous)
print('_'*50)

previous_sibling = org.findPreviousSibling()
print(previous_sibling)
print('_'*50)


import re 
email_example="""<br>
<p>My Email Is</p>
abc@fskjf@gmail.com"""
soup_email=BeautifulSoup(email_example,"lxml")
email_ID_regexp=re.compile("\w+@\w+\.\w+")
email_id=soup_email.find(text=email_ID_regexp)
print(email_id)

name=input()

