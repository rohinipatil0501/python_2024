#Program to find sum of digits of a number
num=(int(input('enter a number : ')))
sum_of_digits=0
n=num
while n>0:
    digit=n%10
    sum_of_digits+=digit
    n//=10
print('ths sum of digit of number is',sum_of_digits)

