from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as Req

url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

Client = Req(url)

page_html=Client.read()

page_soup = soup(page_html,"html.parser")

# print(page_soup.contents)

containers = page_soup.findAll("div",{"class":"_3O0U0u"})

container = containers[0]

print(container.div.img['alt'])

price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})

print(price[0].text)

rating=container.findAll("div",{"class":"hGSR34"})

print(rating[0].text)

filename="flpphn.csv"
f = open(filename,"w")

headers="Products_Name,Pricing,Ratings\n"
print(f.write(headers))

for container in containers:
    product_name = container.findAll("div",{"class":"_3wU53n"})
    product=product_name[0].text

    price_container = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container = container.findAll("div",{"class":"hGSR34"})
    rating=rating_container[0].text.strip()

    print("Productname:"+product)
    print("Price:"+price.replace("₹"," ₹"))
    print("Rating:",rating)
    
    rm_rupee =price.split("₹")
    add_rs_price="Rs."+ rm_rupee[1]

    split_price=add_rs_price.split("E")
    final_price=split_price[0]

    print("Summary:(Product: ",product.replace(",","|")+" ,Price: " +  final_price + ", Rating: " + rating + ")\n")
    f.write(product.replace(",", "|") + " , "+ final_price + ", " +rating+ "\n" )
f.close()