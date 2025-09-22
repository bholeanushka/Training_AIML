import numpy as np

# 1D Array
arr1 = np.array([1,2,3,4,5])

# 2D Array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr1)
print(arr2)

# Numpy Operations
print(f"Max : {np.max(arr1)}")
print(f"Min : {np.min(arr1)}")
print(f"Average : {np.mean(arr1)}")

print(f"First 3 elements : {arr1[:3]}")
print(f"Sum : {np.sum(arr1)}")
print(f"Reversed : {arr1[::-1]}")
print(f"Standard deviation : {np.std(arr1)}")