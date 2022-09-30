"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

"""SOLUTION"""
numbers.sort()

if len(numbers) % 2 == 1:
    median = numbers[int(((len(numbers) + 1) / 2)-1)]
else:
    midleft = int(len(numbers)/2 - 1)
    midright = int(len(numbers)/2)
    median = (numbers[midleft] + numbers[midright]) / 2

print (median)
