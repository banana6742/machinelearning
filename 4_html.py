#Demo3 Navigating tree

#1.import the required lib

from bs4 import BeautifulSoup

#2.create the document
book_shop_doc="""
<catalog>

<head>
    <title>The web book catalog</title></head>
    <p class="title"><b>The Book Catalog</b></p>
<books>
    <book id="bk001">
        <Author>HighTower</Author>
        <genre>Fiction</genre>
        <price>44.34</price>
        <pub_date>2000-10-10</pub_date>
        <review>An Amazing story of nothing.</review>
    </book>


    <book id="bk002">
        <Author>Nagata,Suanne</Author>
        <title>Becoming somebody</title>
        <genre>Biography</genre>
        <review>A masterPiece of the art</review>
    </book>

    <book id="bk003">
        <Author>Oberg,Bruce</Author>
        <title>The Poet's First Poem</title>
        <genre>poem</genre>
        <price>28.2</price>
        <review>The Least Poetic Poems</review>
    </book>
        
</books>

</catalog>
    
"""

#3.create a soup object
book_soup = BeautifulSoup(book_shop_doc,"html.parser")

#4.print the catalog tag
print(book_soup)

print("-"*50)
#create a sub objects
print(book_soup.catalog)

print("-"*50)
#get head
print(book_soup.head)

#get title tag
title_tag=book_soup.title
print(title_tag)
print("-"*50)
print("-"*50)

#print catalog bold tag

#navigate down the decendants and print them
for desc in book_soup.head.descendants:
    print(desc)

print("-"*50)

#navigate down using stripped stringed method
for string in book_soup.stripped_strings:
    print(repr(string))

print('_________parents_________________')

#navigate up using the parent method

print(title_tag.parent)


print('________navigate back and forth_________________')
#create element object to navigate back and forth
element_soup=book_soup.catalog.books
print(element_soup)

print('______======================_______')

next_element= element_soup.next_element.next_element
print(next_element)

print('______=========previous_element=============_______')

#navigate back using the previous_element method
previous_element=next_element.previous_element.previous_element
print(previous_element)


print('______======================_______')

#create a sibling 
next_sibling = book_soup.catalog.books.book
print(next_sibling)

#navigator to next sibling
next_sibling2= next_sibling.next_sibling
print(next_sibling2.next_sibling)

#navigate to previous sibling
previous_sibling=next_sibling2.previous_sibling
print(previous_sibling)