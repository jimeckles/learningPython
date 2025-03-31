# Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# comprehension [output arrray, for var in list if condition]
newlist = [positiveNumber for positiveNumber in numbers if positiveNumber > 0]
print(newlist)
