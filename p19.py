#Program to print the Right angled Triangle of N lines
number_of_lines=int(input('enter number of lines'))
for i in range(1,number_of_lines+1):
    for j in range(i):
        print('*',end=' ')
    print()
       

