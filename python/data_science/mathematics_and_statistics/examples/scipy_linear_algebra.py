import numpy as np
import scipy.linalg as la

# Luego definiremos los coeficientes del sistema lineal
# - Matriz de 3x3 que representa los coeficientes de las tres ecuaciones del sistema. 
# – contiene los términos constantes de las ecuaciones del sistema.

# Define the coefficients of the linear system
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
b = np.array([1, 2, 3])
# [1 2 3]

# Esta función resuelve el sistema de ecuaciones lineales a x = b 
x = la.solve(a, b)
print(x)
# [-0.33333333  0.66666667 -0.        ]

# Validate de result
b = a.dot(x)
print(b)


