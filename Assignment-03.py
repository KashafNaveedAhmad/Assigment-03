
import math
import time

# Assignment-03
print("Let's start the assignment!!")

# Age using current year and birth year
print("\nWe are going to calculate your age.\nBelow:")
birth_year=int(input("Enter your birth year:"))
current_year=int(time.strftime('%Y'))
age=current_year-birth_year
print("Your age based on your birth year is:",age,"years old")
