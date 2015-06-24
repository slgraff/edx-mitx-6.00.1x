# lec4.8-circle.py
# Lecture 4.8, Modules

# Demonstrating how to import functions from a file, such as this one
# Use import command (import circle)
# Use dot notation to access variables and functions within this file

# Another way to import circle (from circle import *)
# then don't need to use dot notation to access imported functions
# Stil need to use dot notation to access variables

pi = 3.14159

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius
