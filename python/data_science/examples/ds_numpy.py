import numpy as np

# Multiplicamos 2 numeros escalares
A = 2 * 3
A = np.dot(2, 3)
print(A)
# 6

# Multiplicamos un numeros escalar y una matric
A = np.dot(2,[5, 6])
print(A)
# [10 12]

# Create a 3x3 matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Transpose the matrix
B = A.T
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

# producto por elementos
result = A * B
# [[ 1  8 21]
#  [ 8 25 48]
#  [21 48 81]]

# Producto matricial
# Example item 1 
#   [(1*1)+(2*2)+(3*3)  (1*4)+(2*5)+(3*6)  (1*7)+(2*8)+(3*9)]
#   [14  32  50]
result = A @ B
result = A.dot(B)
result = np.dot(A, B)
print(result)
# [[ 14  32  50]
#  [ 32  77 122]
#  [ 50 122 194]]