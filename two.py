"""
Get input from the user for two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 Check if the numbers are equal and print the result
if number1 == number2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
"""
# user input
number = int(input("Enter a number: "))

# if the number is odd, even, or zero
if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
