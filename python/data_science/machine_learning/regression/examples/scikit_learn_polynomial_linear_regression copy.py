from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
x = np.arange(6).reshape(3, 2)
# [[0 1]
#  [2 3]
#  [4 5]]

# Ajustar el modelo degree = 1
# Las características de x se han transformado de (x1, x2) a (1, x1, x2)
transformer = PolynomialFeatures(degree=1)
x_polynomial = transformer.fit_transform(x)
# [[1. 0. 1.]
#  [1. 2. 3.]
#  [1. 4. 5.]]

# Ajustar el modelo degree = 2
# Las características de x se han transformado de (x1, x2) a (1, x1, x2, x1², x1x2, x2²)
transformer = PolynomialFeatures(degree=2)
x_polynomial = transformer.fit_transform(x)
# [[ 1.  0.  1.  0.  0.  1.]
#  [ 1.  2.  3.  4.  6.  9.]
#  [ 1.  4.  5. 16. 20. 25.]]

# Ajustar el modelo degree = 2
# interaction_only=True > se excluyen las potencias
# Las características de x se han transformado de (x1, x2) a (1, x1, x2, x1x2)
transformer = PolynomialFeatures(degree=2, interaction_only=True)
x_polynomial = transformer.fit_transform(x)
# [[ 1.  0.  1.  0.]
#  [ 1.  2.  3.  6.]
#  [ 1.  4.  5. 20.]]

# Ajustar el modelo degree = 2
# interaction_only=True > se excluyen las potencias
# include_bias=True
transformer = PolynomialFeatures(degree=2, include_bias=True)
x_polynomial = transformer.fit_transform(x)
print(x_polynomial)
# [[ 1.  0.  1.  0.]
#  [ 1.  2.  3.  6.]
#  [ 1.  4.  5. 20.]]

# Ajustar el modelo degree = 3
# Las características de x se han transformado de (x1, x2, x3) a (1, x1, x2, x3, x1x2, x1x3, x2x3, x1x2x3)
x = np.arange(9).reshape(3, 3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
transformer = PolynomialFeatures(degree=3, interaction_only=True)
x_polynomial = transformer.fit_transform(x)
print(x_polynomial)
# [[  1.   0.   1.   2.   0.   0.   2.   0.]
#  [  1.   3.   4.   5.  12.  15.  20.  60.]
#  [  1.   6.   7.   8.  42.  48.  56. 336.]]






