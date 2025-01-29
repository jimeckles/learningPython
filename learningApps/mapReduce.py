from functools import reduce

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(list(map(lambda n: round(n**2, 2), my_floats)))

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda name: len(name) <= 7, my_names)))

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(filter(lambda name: name, my_names))


def multiply(num1, num2):
    print("1: " + str(num1))
    print("2: " + str(num2))
    return num1 * num2


# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)
reduce_result = reduce(multiply, my_numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)
