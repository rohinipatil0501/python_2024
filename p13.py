 #program to find biggest(smallest) digit in a number

number = int(input("Enter a number: "))


biggest_digit = 0

while number != 0:
    digit = number % 10  
    if digit > biggest_digit:
        biggest_digit = digit
    number = number // 10 

print("The biggest digit is:", biggest_digit)