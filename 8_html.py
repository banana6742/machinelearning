from bs4 import BeautifulSoup as BS
data_SL = """<ul class="content-col_discover">
    <h5>Discover</h5>
    <li><a href="/resources" id="free_resources">Free resources</a></li>
    <li><a href="http://community.simplilearn.com/" id="community">Simplilearn community</a></li>
    <li><a href="/career-data-labs" id="lab">Career data labs</a></li>
    <li><a href="/scholarships-for-veterans" id="scholarships">Veterans scholarship</a></li>
    <li><a href="/http://www.simplilearn.com/" id="rss">RSS feed</a></li>
</ul>""" 
# create soup object
soup = BS(data_SL,'html.parser')
# if i want to scrape only the small portions of the data
print('practice: ', soup.get_text())

# import soupstrainer class for parsing the desired part of the web document
from bs4 import SoupStrainer as SS

extract=SS(id="free_resources")
print(BS(data_SL,'html.parser',parse_only=extract))

# create object to parse only the id(link) with lab
extract=SS(id="community")
print(BS(data_SL,'html.parser',parse_only=extract))

extract=SS(id="lab")
print(BS(data_SL,'html.parser',parse_only=extract))

extract=SS(id="scholarships")
print(BS(data_SL,'html.parser',parse_only=extract))
print('-'*50)
extract=SS(id="free_resources")

# print the part of the parsed document
# just arranges the output neatly
print(BS(data_SL,'html.parser',parse_only=extract).prettify())

extract=SS(id="community")
print(BS(data_SL,'html.parser',parse_only=extract).prettify())

extract=SS(id="lab")
print(BS(data_SL,'html.parser',parse_only=extract).prettify())

extract=SS(id="scholarships")
print(BS(data_SL,'html.parser',parse_only=extract).prettify())