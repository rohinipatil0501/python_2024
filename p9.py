#Program to print math table of a number
num=(int(input('enter a number for which math table is to be formed :' )))
print('MATH TABLE FOR',num)
for i in range(1,11):
    print(num,'x',i,'=',i*num)              
    