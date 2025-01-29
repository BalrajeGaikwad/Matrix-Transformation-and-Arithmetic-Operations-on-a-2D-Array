#Matrix Transformation and Arithmetic Operations on a 2D Array

import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
array1=np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Array")
print(array)

print("Array 1")
print(array1)

addition=array+array1
print("Additiion of array : ")
print(addition)

subtraction=array-array1
print("Subtraction of array")
print(subtraction)

multiplication=array*array1
print("multiplication of array :")
print(multiplication)

matrix_multiplication=array @array1.T
print("Matrix Multiplication (array @array1.T) ")
print(matrix_multiplication)

threshold=5
logical_condition=array> threshold
print(logical_condition)

filtered_array=array[logical_condition]
print(" filtered array")
print(filtered_array)


transposed_array=array.T
print("Transpose of array ")
print(transposed_array)