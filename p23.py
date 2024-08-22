#Program to Print X shape inside Hollow Square
number=int(input('enter a number'))
for i in range(number):
    for j in range(number):
      if(i==0 or i==number-1 or j==0 or j==number-1 or j==i or j==number-i-1):
        print('*', end=' ')
      else:
        print(' ',end=' ')
    print()
