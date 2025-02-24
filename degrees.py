#Martha Moreno Gonzalez
#02/22/2025
#convert radian to degrees (using my own equation and degrees functions in math module)

import math

radians = int(input("Value in radians you want to convert to degrees: "))

radians_to_degrees = radians * 180/math.pi
math_degrees = math.degrees(radians)

print("This the degrees using the plug in equation:", radians_to_degrees)
print("This the degrees using the math.degrees:", math_degrees)