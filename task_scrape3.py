# from bs4 import BeautifulSoup as BS

# room="""<office>
# <room class="firstfloor">
# <room_no1>101</room_no1> <room_no2>102</room_no2> <room_no3>103</room_no3>
# </room>

# <room class="secondfloor">
# <room_no1>201</room_no1> <room_no2>202</room_no2> <room_no3>203</room_no3>
# </room>

# <room class="thirdfloor">
# <room_no1>301</room_no1> <room_no2>302</room_no2> <room_no3>303</room_no3>
# </room>"""

# soup_room=BS(room,'html.parser')

# print(soup_room)

# print('='*25+'room'+"="*25)

# room = soup_room.room
# print(room)


# print('='*25+'secondfloor'+"="*25)

# room['class']='secondfloor'
# print(room)


# print('='*25+'fourthfloor'+"="*25)

# room=soup_room.new_tag('room_no4')

# room.string='304'

# print(room)


# from urllib.request import urlopen
# f = urlopen('http://sample.scraping-book.com/dp')

# type(f)

# f.read()

# f.status()
# f.getheader('Content-Type')


# import sys
# from urllib.request import urlopen

# f = urlopen('http://sample.scraping-book.com/dp')
# encoding = f.info().get_content_charset(failobj="utf-8")
# print('encoding:',encoding,file=sys.stderr)

# text = f.read().decode(encoding)
# print(text)

# import re
# import sys
# from urllib.request import urlopen
# f=urlopen('http://sample.scraping-book.com/dp')
# bytes_content = f.read()
# scanned_text=bytes_content[:1024].decode('ascii',errors='replace')
# match=re.search(r'charset=["\']?([\w-]+)',scanned_text)
# if match:
#     encoding = match.group(1)
# else:
#     encoding = 'utf-8'

# print('encoding:',encoding,file=sys.stderr)

# text = bytes_content.decord(encoding)
# print(text)


# import re
# from html import unescape
# with open('dp.html') as f:
#     html = f.read()

# for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>',html,re.DOTALL):
#     url = re.search(r'<p itemprop="url" href="(.*?)">',partial_html).group(1)
#     url = 'https://gihyo.jp'+ url

#     title = re.search(r'<p itemprop="name".*?</p>',partial_html).group(0)
#     title = title.replace('<br/>',' ')
#     title = re.sub(r'<.*?>','',title)
#     title = unescape(title)

# print(url,title)
    
# print('rank,city,population')
# print(','.join(['1','上海','24150000']))
# print(','.join(['2','カラチ','23500000']))
# print(','.join(['3','北京','215160000']))
# print(','.join(['4','天津','14722100']))
# print(','.join(['5','イスタンブール','14160467']))

# import requests
# r = requests.get('http://sample.scraping-book.com/dp')
# type(r)
# r.status_code

