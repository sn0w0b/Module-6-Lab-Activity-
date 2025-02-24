#Martha Moreno Gonzalez
#02/22/2025
#Use a for statement to calculate the factorial of a user input value. Print this value
#as well as the calculated value using the factorial function in the math module.

import math

value_enter = int(input("Please enter value you want to know the factorial for: "))
factorial_for = 1

for i in range(1, value_enter + 1):
    factorial_for *= i

math_factorial = math.factorial(value_enter)

print("This the factorial for the value using 'for' loop: ", factorial_for)
print("This the factorial for the value using the factorial function in the math module: ", math_factorial)
