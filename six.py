
two_digit_no = int (input("Enter a two-digit number: ")) 

# Get the sum of the digits
tens = two_digit_no // 10 
units = two_digit_no % 10 
sum_of_digits = tens + units 

print(f"The sum of the digits is: {sum_of_digits}")
