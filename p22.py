#Program tp print X shape of N lines
Number = int(input("Enter the number of lines for the X shape: "))

for i in range(Number):
    for j in range(Number):
        if j == i or j == Number - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
