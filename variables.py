"""
Note
Python has no command for declaring a variable
"""

# Declare variable in python has two types:
# 1. Without declare data type
# firstName = 'Rifaldi'
# lastName = 'Herikson'
# lastName = str('Herikson')
firstName, lastName = 'Rifaldi', 'Herikson'

# 2. With casting data type
# currentYear = int(2024)
# birthYear = int(1997)
currentYear, birthYear = int(2024), int(1997)
myHobby = list(('Badminton','Coding'))

# Get data type of variable
print(type(firstName))
print(type(myHobby))


# v1 - Calling two string
print('Hello, Mr.',firstName,lastName)

# v2 - String combination
print('Hello, Mr.',firstName+lastName)

# Integer calculation
print('Your age is',currentYear-birthYear,'years')