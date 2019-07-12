#0 imppr
from bs4 import BeautifulSoup as BS
import requests

url = 'https://lohitbadiger.herokuapp.com'

getWeb = requests.get(url)

pagecontent= getWeb.content

#1
soup = BS(pagecontent,'html.parser')

#2
# print(soup.contents)
print(soup.body.nav.div.prettify())
print("="*50)
# print(soup.body.a.prettify())

