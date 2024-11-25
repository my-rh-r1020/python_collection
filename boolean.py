a='Hello World'
b=9

print(bool(a),'\n', bool(b))

# Check data type in variable
print(isinstance(b,int))


# Booleans in function
def myFunction():
    return True

if myFunction():
    print('YES')
else:
    print('NO')