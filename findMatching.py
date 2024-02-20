a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.difference(b))
# find any item only in one of either lists
print(a.symmetric_difference(b))

# make a unique list of all elements from both lists
print(a.union(b))