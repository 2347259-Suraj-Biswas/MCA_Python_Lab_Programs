# Q1. Create two 3×3 matrices using the random function in Numpy and perform the following operations.
#     1. Product (prod)
#     2. Multiplication (multiply)
#     3. Dot Product (dot)

import numpy as np

def product(matr1,matr2):
    result = np.prod([matr1, matr2], axis=0)
    return result

def multiply(matr1,matr2):
    result = np.multiply(matr1, matr2)
    return result

def dotproduct(matr1, matr2):
    result = np.dot(matr1, matr2)
    return result

matrix1 = np.random.randint(50, size=(3,3))
matrix2 = np.random.randint(50, size=(3,3))

print("Matrix 1:")
print(matrix1)
print("\n")
print("Matrix 2:")
print(matrix2)
print("\n")
print("Product(prod) of 3x3 Matrix:")
print(product(matrix1,matrix2))
print("\nMultiplication(multiply) of 3x3 Matrix:")
print(multiply(matrix1,matrix2))
print("\nDot Product of 3x3 Matrix:")
print(dotproduct(matrix1,matrix2))


# Q2. Perform the following set operations using the Numpy functions.
    # 1. Union
    # 2. Intersection
    # 3. Set difference
    # 4. XOR

import numpy as np

arr1 = np.array([5,4,6,7,8])
arr2 = np.array([7,5,4,3,5])

arr_union = np.union1d(arr1, arr2)
arr_intersection = np.intersect1d(arr1, arr2)
arr_setdifference = np.setdiff1d(arr1, arr2)
arr_xor = np.setxor1d(arr1 ,arr2)

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)
print("\nUnion of 2 arrays:")
print(arr_union)
print("\nIntersection of 2 arrays:")
print(arr_intersection)
print("\nSet difference of the 2 arrays:")
print(arr_setdifference)
print("\nXOR of the 2 arrays:")
print(arr_xor)

# Q3. Create a 1D array using Random function and perform the following operations.
    # 1. Cumulative sum
    # 2. Cumulative Product
    # 3. Discrete difference (with n=3)
    # 4. Find the unique elements from the array

import numpy as np

arr1 = np.random.randint(30, size=(5))

cummulative_sum = np.cumsum(arr1)
cummulative_prod = np.cumprod(arr1)
discrete_diff = np.diff(arr1, n=3)
unique_elem_arr = np.unique(arr1)

print("Original Array:")
print(arr1)
print("\nCummulative Sum:")
print(cummulative_sum)
print("\nCummulative Product:")
print(cummulative_prod)
print("\nDiscrete Difference(with n=3):")
print(discrete_diff)
print("\nUnique elements from the array:")
print(unique_elem_arr)

# Q4. Create two 1D array and perform the Addition using zip(), add() and user defined function (frompyfunc())

import numpy as np

def addition_zip(arr1, arr2, arr3):
    for i, j in zip(arr1, arr2):
        arr3.append(i + j)

def add_arr(x, y):
    return x + y

array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
array3 = []

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

addition_zip(array1, array2, array3)

print("\nAddition using zip():")
print(array3)

print("\nAddition using add():")
z = np.add(array1, array2)
print(z)

print("\nAddition using frompyfunc():")
frompy_add = np.frompyfunc(add_arr, 2, 1)
result = frompy_add(array1, array2)
print(result)


# Q5. Find the LCM (Least Common Multiple) and GCD (Greatest Common Divisor) of an array of elements using reduce().

import numpy as np

def find_gcd(arr):
    return np.gcd.reduce(arr)

def find_lcm(arr):
    return np.lcm.reduce(arr)

arr = np.array([23, 12, 14, 15, 20])
print("Array:")
print(arr)

gcd_result = find_gcd(arr)
print(f"\nGCD of {arr} is {gcd_result}")

lcm_result = find_lcm(arr)
print(f"\nLCM of {arr} is {lcm_result}")
