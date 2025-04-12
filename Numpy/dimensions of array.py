import numpy as np

# Arrays can be created up to 32 dimensions in NumPy

# 1-dimensional array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array a:", a)
print("This is a 1-dimensional array. You can check the number of dimensions using a.ndim")
print("Dimensions of array a:", a.ndim)

# 2-dimensional array
b = np.array([[1, 2, 3], [9, 7, 8]])
print("\nArray b:\n", b)
print("This is a 2-dimensional array.")
print("Dimensions of array b:", b.ndim)

# 4-dimensional array
c = np.array([[[1, 2, 3], [4, 5, 6]]])
print("\nArray c:\n", c)
print("This is a 4-dimensional array.")
print("Dimensions of array c:", c.ndim)
