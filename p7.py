#Program to check if the number is perfect square
import math
num = int(input(' enter a number : '))
sqrt=math.sqrt(num)
if sqrt==int(sqrt):
    print(num,'is a perfect square')
else:
    print(num,'is not a perfect square')



