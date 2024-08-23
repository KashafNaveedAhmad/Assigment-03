
import math
import time

# Assignment-03
print("Let's start the assignment!!")

# Calculate your age based on the current year and your birth year.
# Age using current year and birth year
print("\nWe are going to calculate your age.\nBelow:")
birth_year=int(input("Enter your birth year:"))
current_year=int(time.strftime('%Y'))
age=current_year-birth_year
print("Your age based on your birth year is:",age,"years old.2")

# Write a program that calculates the area of a rectangle using length and width variables.
# Area of recatangle(length*width)
print("\nLet's calculates the 'Area of a rectangle'.\nBelow:")
length=float(input("Enter the lenght:"))
width=float(input("Enter the width:"))
area=length*width
print("The area of rectangle is:",area)

# Write a program that calculates the area of a circle.
# Area of circle (Formula:(math.pi)*(radius**2))
print("\nLet's calculate the 'Area of Circle'.\nBelow:")
radius_of_circle=float(input("Enter the radius:"))
area_of_circle=((math.pi)*(radius_of_circle**2))
print("The area of circle is:",area_of_circle)

# Write a program that calculates the area of the cube.
# Area of circle (Formula:6(a^2))
print("\nLet's calculate the 'Area of Cube'.\nBelow:")
side_of_cube=int(input("Enter the it's side:"))
area_of_cube=(6*(side_of_cube**2))
print("The area of cube is:",area_of_cube)

# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
# Fahrenheit to Celsius (Formula:(5/9)*(F-32))
print("\nWe are going to convert 'Fahrenheit' into 'Celsius': \nBelow:")
input_fahrenheit=float(input("Enter the temperature in 'Fahrenheit':"))
celsius=float((5/9)*(input_fahrenheit-32))
print("The converted temperature in 'Celsius' is:",celsius,"°C")

# Celsius to Fahrenheit (Formula:((9/5)*C)+32))
print("\nWe are going to convert 'Celsius' into 'Fahrenheit': \nBelow:")
input_celsius=float(input("Enter the temperature in 'Celsius':"))
fahrenheit=(((9/5)*input_celsius)+32)
print("The converted temperature in 'Fahrenheit' is:",fahrenheit,"°F")



