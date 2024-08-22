#Program to find count of digits of a number
number=int(input('enter a number'))
count=0
while number != 0:
    i = number % 10
    count += 1
    number = number//10
    
print('the count of digits of the given number is',count)



