# # import math
# # math.floor(4.2132)

# # result = math.sqrt(256)
# # print(result)



# import numpy as np

# # Create a 1D array
# a = np.array([1, 2, 3, 4, 5])
# print("1D Array:")
# print(a)

# # Create a 2D array
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print("\n2D Array:")
# print(b)

# # Array operations
# c = a + 2
# print("\nArray addition:")
# print(c)

# d = np.sqrt(a)
# print("\nSquare root of array elements:")
# print(d)

# # Matrix operations
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# C = np.dot(A, B)
# print("\nMatrix multiplication:")
# print(C)

# # Array slicing
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("\nArray slicing:")
# print(arr[:2, 1:])

# # Array manipulation
# arr = np.array([1, 2, 3, 4, 5])
# print("\nArray manipulation:")
# arr = np.append(arr, [6, 7])
# print(arr)
# arr = np.delete(arr, [0, 1])
# print(arr)

# # Random number generation
# rand_arr = np.random.rand(3, 2)
# print("\nRandom 3x2 array:")
# print(rand_arr)

# # Statistics
# print("\nMean of array elements:")
# print(np.mean(rand_arr))
# print("Standard deviation of array elements:")
# print(np.std(rand_arr))
import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(a)

# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(b)

# Array operations
c = a + 2
print("\nArray addition:")
print(c)

d = np.sqrt(a)
print("\nSquare root of array elements:")
print(d)

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)
print("\nMatrix multiplication:")
print(C)

# Array slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray slicing:")
print(arr[:2, 1:])

# Array manipulation
arr = np.array([1, 2, 3, 4, 5])
print("\nArray manipulation:")
arr = np.append(arr, [6, 7])
print(arr)
arr = np.delete(arr, [0, 1])
print(arr)

# Random number generation
rand_arr = np.random.rand(3, 2)
print("\nRandom 3x2 array:")
print(rand_arr)

# Statistics
print("\nMean of array elements:")
print(np.mean(rand_arr))
print("Standard deviation of array elements:")
print(np.std(rand_arr))
