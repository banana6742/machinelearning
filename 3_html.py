from bs4 import BeautifulSoup

file = "C:/Users/banan/Desktop/webscrape/webhtml2.html"
with open(file,"r") as orgz:
    soup=BeautifulSoup(orgz,"html.parser")

print(soup.contents)
print('-'*40)

tag_lr=soup.find("table")
print(type(tag_lr))
print('-'*40)

# テーブルタグの読み取り
print(tag_lr)
print('-'*40)

# idがnameのものを抽出
find_name=soup.find(id = "name")
print(find_name)
print('-'*40)

# idがnameのものでtr,td,stringに関するものを抽出
print(find_name.tr.td.string)


print('~%'*20)
# class="lo"のものを抽出
print(find_name.find(attrs={"class":"lo"}))

# ["whitefield",'bangalore']のワードをすべて抽出
print('-'*40)
search_perticular_string = soup.findAll(text=["whitefield",'bangalore'])
print(search_perticular_string)

# class="location"のものを抽出
print('-'*40)
css_class_attrs = soup.find(attrs={'class':"location"})
print(css_class_attrs)
