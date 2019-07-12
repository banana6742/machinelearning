# 0. creating employee based on basic details

# 1.import the required Library

from bs4 import BeautifulSoup

# create employee html Document

employee_html_doc="""<employees>
            <employee class="accountant">
            <firstname>John</firstname>  <lastname>Doe</lastname>
            </employee>

            <employee class="manager">
            <firstname>Anna</firstname>  <lastname>Smith</lastname>
            </employee>

            <employee class="developer">
            <firstname>Lohit</firstname>  <lastname>Badiger</lastname>
            </employee>

<employees>"""
# 2. create soup object


soup_emp=BeautifulSoup(employee_html_doc,'html.parser')

print(soup_emp)

print('='*25+'tag'+"="*25)

# access and view the tag
tag = soup_emp.employee
print(tag)

print('='*25+'magager'+"="*25)

# modify the tag im adding new tag
tag['class']='manager'
print(tag)

print('='*25+'developer'+"="*25)

tag['class']="developer"
print(tag)

print('='*25+'NewTag'+"="*25)

print('\n')
# add a tag
tag=soup_emp.new_tag('NewTag')

print(tag)

print('-'*50)

tag=soup_emp.new_tag('NewTag')

tag.string='Lohith Learning Process'

print(tag)

# tag=soup_emp.new_tag('boss')
# tag.string='KOtA'
# print(tag)

print('='*25+'insert_after'+"="*25)
soup_emp.employees.employee.insert_after(tag)
print(soup_emp)

print('='*25+'clear'+"="*25)
#clear all the modified tag
#it will delete the last generated output from the tag i.e 'Lohit Leaning Processs'
tag.clear()

print(soup_emp)

print('-'*50)
print('-'*50)

# create a tag object and view it
tag = soup_emp.employee
print(tag)

print('-'*50)
print('-'*50)

print(tag.firstname.string.extract())

print('-'*50)
print('-'*50)

print(tag.firstname.replace_with('goal'))

print('-'*50)
print('-'*50)

print(soup_emp.employees)


