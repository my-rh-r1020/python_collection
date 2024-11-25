fruit = ['banana','apple','orange','mango','banana']
print('List fruit =',fruit)

# List start from begin
print('Fruit =',fruit[1])

print('Fruit data length =',len(fruit))
print(type(fruit))


# Constructor
hobby = list(['badminton','coding','watching','traveling','reading'])
print(hobby)

# List start from end
print('Hobby =',hobby[-1])

# Range list
print(hobby[1:3])

# Check item in list
if 'coding' in hobby:
    print('Yes, coding is in hobby list')
else:
    print('No, coding is not in hobby list')

# Change item list
hobby[4]='playing games'
print('Change list item =',hobby)

# Insert item list
hobby.insert(4,'reading')
print('New list item =',hobby)

# Append list
hobby.append('hacking')
print('Append new item in lists =',hobby)

# Extend list
fruit.extend(hobby)
print('List fruit extends hobby =',fruit)