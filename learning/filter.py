
l=[1,2,3,4,5]


def filter_function(a):
    return a*a*a

newl = list(filter(filter_function,l))
print(newl)

a =list(map(filter_function,l))
print(a)

c = list(map(lambda X:X+X+X,l))
print(c)


z =list(map(lambda x,y:x*y,(1,2),(3,4)))
print(z)



from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 120


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Double the elements
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")  # Output: [2, 4, 6, 8, 10, 12]

# Step 2: Filter out even numbers
filtered_numbers = list(filter(lambda x: x % 2 != 0, doubled_numbers))
print(f"Filtered (odd) numbers: {filtered_numbers}")  # Output: []

# Step 3: Find the product of the remaining elements
if filtered_numbers:
    product = reduce(lambda x, y: x * y, filtered_numbers)
    print(f"Product of remaining numbers: {product}")
else:
    print("No numbers left after filtering.")
