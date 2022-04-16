name = 'Dini'
age = 30
#concatenate
print('my name is ' + name + ' and i am ' +str(age), 'years old')
#Arguments by position
print('my name is {name} and my age is {age}'.format(name = name, age=age))
#F string (available in python 3.6+)
print(f'my name is {name} and i am {age}')
#String Methods
s = 'hello world'
#Capitalizing first letters of string
print(s.capitalize())
print(s.upper())
print(s.split())
print(s.swapcase())
print(len(s))
print(s.replace('world', 'everyone'))
print(s.startswith('hello'))
print(s.endswith('d'))
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isalnum())
print(s.isnumeric())