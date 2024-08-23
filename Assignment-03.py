
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
# Area of recatangle
print("\nWe are going to calculates the 'Area of a rectangle'. \nBelow:")
length=float(input("Enter the lenght:"))
width=int(input("Enter the width:"))
area=length*width
print("The area of rectangle is:",area)

# Write a program that calculates the area of a circle.
# Area of circle
print("We are going to calculate the 'Area of Circle' :\n Below:")
rad=int(input("Enter the radius to calculate the area of circle:"))
area_of_circle=((math.pi)*(rad**2))
print("The area of circle is:",area_of_circle)





