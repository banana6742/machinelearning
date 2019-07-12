from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

url = "https://catalog.data.gov/dataset?q=&sort=metadata_created+desc"

Data=urlopen(url)

pghtml=Data.read()

Data.close()

pgsoup =BS(pghtml,"html.parser")

print(pgsoup.contents)

contents = pgsoup.findAll("div",{"class":"dataset-content"})
content = contents[0]

print(content)

title = content.findAll("h3")

print(title[0].text)

filename="task.csv"
f = open(filename,"w")

headers="Name,Story\n"
print(f.write(headers))

for content in contents:
    title = content.findAll("h3")
    title = title[0].text

    story = content.findAll("div",{"class":"notes"})
    story = story[0].text

    print(title)
    print(story)

    f.write(title+ ", " +story )
f.close()