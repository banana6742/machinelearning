import requests
url = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(url.text,'html.parser')

results = soup.find_all('span',attrs={'class':'short-desc'})

records=[]

for result in results:
    date = result.find('strong').text[0:-1]+', 2019'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date,lie,explanation,url))

import pandas as pd
df = pd.DataFrame(records, columns=['date','lie','explanation','url'])

df['date']= pd.to_datetime(df['date'])
print(df)

df.to_csv('susumu_trump.csv',index=False,encoding='utf-8')
df = pd.read_csv('susumu_trump.csv',parse_dates=['date'],encoding='utf-8')

# 文字化け
# import requests
# url = requests.get('https://www.nikkei.com/')

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(url.text,'html.parser')

# results = soup.find_all('span',attrs={'class':'m-miM10_titleL'})

# records=[]

# for result in results:
#     title = result.contents[0]
#     records.append(title)

# import pandas as pd
# df = pd.DataFrame(records,columns=['title'])
# print(df)


# import pandas as pd
# df = pd.DataFrame(records, columns=['title'])

# # df['date']= pd.to_datetime(df['date'])
# print(df)

# df.to_csv('nikkei.csv',index=False,encoding='utf-8')
# df = pd.read_csv('nikkei.csv',encoding='utf-8')