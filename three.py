
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))

# if the number is odd, even, or zero
highest = num1  # Assume num1 is the largest

if num2 > highest:
    highest = num2

if num3 > highest:
    highest = num3

print(f"The highest number is: {highest}")
