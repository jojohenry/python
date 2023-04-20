
# Variables in Python

first_name = 'Jodiann'
last_name = 'Henry'
country = 'USA'
city = 'NY'
age = 100
is_married = False
skills = ['HTML', 'Go', 'JavaScript', 'SQL', 'Python']
person_info = {
    'firstname':'Jodiann', 
    'lastname':'Henry', 
    'country':'USA',
    'city':'NYC'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Jodiann', 'Henry', 'USA', 100, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
