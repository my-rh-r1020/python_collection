# Single line string
name = 'Rifaldi Herikson'
print(name)


# Multi line string
introduction = '''
My name is Rifaldi Herikson. You can call me Rifaldi
'''
print(introduction)


# String are arrays
fullName = 'Rifaldi Herikson, M.Kom'
print(fullName[3])


# Looping through string
for fullName in 'Rifaldi Herikson':
    print(fullName)


# String length
hobby = 'Coding and Badminton'
print(len(hobby))


# Check string
test = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quod, sapiente.'
print('Quod' in test)


# Uppercase & Lowercase
text = 'Lorem ipsum dolor'
print(text.upper())
print(text.lower())


# Remove whitespace
print(text.strip())
# Replace
print(text.replace('o','a'))
# Split
print(text.split())


# String concatenation
firstName = 'Rifaldi'
lastName = 'Herikson'
print(firstName + ' ' + lastName)