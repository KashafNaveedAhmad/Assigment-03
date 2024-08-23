
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
print("Your age based on your birth year is:",age,"years old")

# Write a program that calculates the area of a rectangle using length and width variables.
# Area of recatangle(length*width)
print("\nLet's calculates the 'Area of a rectangle'.\nBelow:")
length=float(input("Enter the lenght:"))
width=int(input("Enter the width:"))
area=length*width
print("The area of rectangle is:",area)

# Write a program that calculates the area of a circle.
# Area of circle(((math.pi)*(radius**2)))
print("\nLet's calculate the 'Area of Circle'.\nBelow:")
radius_of_circle=int(input("Enter the radius:"))
area_of_circle=((math.pi)*(radius_of_circle**2))
print("The area of circle is:",area_of_circle)

# Write a program that calculates the area of the cube.
# Area of circle(6(a^2))
print("\nLet's calculate the 'Area of Cube'.\nBelow:")
side_of_cube=int(input("Enter the it's side:"))
area_of_cube=(6*(side_of_cube**2))
print("The area of cube is:",area_of_cube)





