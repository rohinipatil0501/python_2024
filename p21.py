#Program to print a Hollow Square of N lines
number_of_lines=int(input('enter number of lines'))
for i in range(number_of_lines):
  for j in range(number_of_lines):
   if i==0 or i==number_of_lines-1 or j==0 or j==number_of_lines-1:
     print('*',end=' ')
   else:
     print(' ',end=' ')
  print()