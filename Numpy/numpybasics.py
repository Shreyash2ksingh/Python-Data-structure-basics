import numpy as np

# Creating a 1D array of 10 digits
a = np.arange(10)


b = np.array([1,2,3,4,5,6,7,8,10,9])

print(a.shape)        # Shape of the array
print(a.dtype)        # Data type
print(a.nbytes)       # Total bytes consumed
print(a.itemsize)     # Size of one item in bytes
print(a.size)         # Number of elements
print(a.ndim)         # Dimension of array

# Taking user input
c = int(input("Enter index where you want to insert the value: "))
d = int(input("Enter the value to insert: "))

# Insert using numpy's insert function
e = np.insert(a, c, d)
print("New array after insertion:", e)
reverse=np.flip(a)
print(a)

m=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(m)

L=np.array([[[1,2,3],[5,6,7]]])