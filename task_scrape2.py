from bs4 import BeautifulSoup as BS

cities="""


<head>
    <title>This is cities in India</title>
</head>

<body>
    
<category>
    <p class="title">
        <b>This is India cities</b>
    </p>

    <cities>
        <city id="B">
            <cityname>Bangalore</cityname>
            <state>Karnataka</state>
            <address>South india</address>
            <feature>live in foreignes, IT cities, R&Dcenter</feature>
        </city>

        <city id="C">
            <cityname>Chennai</cityname>
            <state>Tamil Nadu</state>
            <address>South india</address>
            <feature>Detroit in india, port , large beach</feature>
        </city>

        <city id="D">
            <cityname>Delhi</cityname>
            <state>Delhi</state>
            <address>north india</address>
            <feature>capita, government, 2nd populous city</feature>
        </city>    

        <city id="M">
            <cityname>Mumbai</cityname>
            <state>Maharastra</state>
            <address>north india</address>
            <feature>most populous city,financial center</feature>
        </city>    

    </cities>

</category>

<aboutus>
    <nav>
        <ul>
            <li>a</li>            
            <li>b</li>
            <li>c</li>
        </ul>
    </nav>
</aboutus>

</body>
</address>"""

c = BS(cities,'html.parser')
print(c)

print('-'*50)

# if i want to make content in the list format
print(c.head)

print('-'*50)
print('='*50)

print(c.address)


print('-'*50)
print('='*50)

print(c.head)

print('-'*50)
print('='*50)

cn= c.cityname
print(cn)
print('-'*50)
print('='*50)

for you in cn.descendants:
    print(you)
print('-'*50)
print('='*50)


for you in cn.descendants:
    print(repr(you))

print('-'*50)
print('='*50)


for string in cn.stripped_strings:
    print(string)

print('-'*50)
print('='*50)

print(you.parent)
print('='*50)
print(you.parent.parent)

print('-'*50)
print('='*50)

navigate_up =cn.next_element
print(navigate_up)
print('-'*50)

navigate_upp =cn.next_element.next_element.next_element
print(navigate_upp)
print('-'*50)


for you in navigate_upp.stripped_strings:
    print(repr(string))
print('@'*50)


for you in cn.stripped_strings:
    print(cn)




