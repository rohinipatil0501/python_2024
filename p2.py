# Read a number from the user and check if it is an Even number or not.
number = int(input('Enter a number to check if it is Even or not: '))
print(type(number))
if number % 2 == 0:
    print(number, 'is an Even number')
else:
    print(number ,'is not an Even number')
