# #import bs4 from beatifulsoup
# from bs4 import BeautifulSoup 

# #create the doc
# html_doc="""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
# </head>
# <body>
#     <h1>Heading</h1>    
#     <b>""this is 'comment' 1""</b>
#     <p title="This is about me" class="test">my first website web scrape</p>
#     <div class="cities">

#         <h2>London</h2>
#         <h2>Mumbai</h2>

#     </div>

# </body>
# </html>"""

# #parse it using html parser

# soup = BeautifulSoup(html_doc, 'html.parser') # as BS 省略可能

# #view the soup type

# print('_________type of soup_________')
# print(type(soup))

# #view the soup object
# print('_________printing of soup_________')
# print(soup)

# #view the soup object
# print('__________tag___________')
# tag=soup.p

# #print the tag
# print(tag)
# print('______________________')

# #create a comment object type

# #below line will give only tag only string inside<b> tag
# comment = soup.b.string
# #below line will give only tag only string
# comment1 = soup.b

# print(type(comment))

# print(type(comment1))
# #print the comment 
# print('___print comment_____')
# print(comment)
# print(comment1)

# print('-'*40)
# tag = soup.p.string
# print(tag)
# comment = soup.b.string
# print(comment)



# print('-'*40)
from bs4 import BeautifulSoup as BS

html_doc="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Heading</h1>    
    <b>""this is 'comment' 1""</b>
    <p title="This is about me" class="test">my first website web scrape</p>
    <div class="cities">

        <h2>London</h2>
        <h2>Mumbai</h2>

    </div>

</body>
</html>"""

soup = BS(html_doc,'html.parser')

print(soup)

tag = soup.p
comment = soup.b
tag1 = soup.p.string
comment1 = soup.b.string

print(tag)
print(comment)

print(tag1)
print(comment1)e
# print(soup)




print(comment1[0:])
print(comment1[0:6])
#contains indices(1,3)
print(comment1[0:6:2])

#print the string value in the tag
print(tag.string)
print(tag.string[0:7:])

#this below line will give you 'class' and 'title' of the tag
print(tag.attrs)

