# reading the web page into python

import requests
url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

print(url.text[0:2000])

print('_'*55)

from bs4 import BeautifulSoup
soup = BeautifulSoup(url.text,'html.parser')

print('_'*55)

results=soup.findAll('span',attrs={'class':'short-desc'})
print(len(results))

print('_'*55)

print(results[0:3])
print('_'*55)

#from the bottom of the website

print(results[-1])
print('_'*55)

print('_'*55)

#extracting the date
first_result = results[0]
print(first_result)

print('-'*50)
print(first_result.find('strong'))
print('-'*50)

print(first_result.find('strong').text)
print('-'*50)
print(first_result.find('strong').text[0:-5])

print('-'*50)
# below both are same
print(first_result.find('strong').text[0:-5]+',2019')
print(first_result.find('strong').text,',2019')

print('_'*55)
# extracting the lie

# lets first see the result
print(first_result)
print('_'*55)
print(first_result.contents)
print('_'*55)
print('_'*55)
print(first_result.contents[1])

print('_'*55)
print(first_result.contents[1][1:-2])
print('_'*25,'first_result.contents','_'*25)
print(first_result.contents[2   ])

print('_'*55)
print(first_result.find('a'))
print('_'*55)
print(first_result.find('a')['href'])
print('_'*55)



