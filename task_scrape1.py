from bs4 import BeautifulSoup

Hfile = "C:/Users/banan/Desktop/webscrape/task-1.html"
with open(Hfile,"r") as org:
    soup = BeautifulSoup(org,"html.parser")

print(soup.contents)

tag_li=soup.find("li")

print(tag_li)

print('-'*30)
find_class=soup.find(attrs={'class':'anime-character'})

print(find_class)

print('-'*40)
find_id = soup.find(id="ex1")
print(find_id)
print('_________***____________')
print(find_id.li.string)

    print('_________***____________')

    searchstring= soup.find(text=['sazaesan','misae','shinchan'])
    print(searchstring)
    searchstring= soup.find(text=['sazaesan'])
    print(searchstring)



searchstring= soup.findAll(text=['sazaesan','misae','shinchan','pokemon'])
print(searchstring)

