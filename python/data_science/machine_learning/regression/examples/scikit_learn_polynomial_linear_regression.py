from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt

# Transformación de los datos a características polinómicas de grado 2
x = np.array([45, 50, 60, 60, 70, 80, 90, 90, 100, 110]).reshape(-1, 1)  # Independent variable (features)
y = np.array([150, 160, 200, 180, 230, 250, 300, 280, 400, 500])  # Dependent variable (target)

# Ajuste al modelo de regresión lineal
lin_reg = LinearRegression()
lin_reg.fit(x, y)
y_pred_lin = lin_reg.predict(x)

# Ajuste al modelo de regresión polinómica de grado 2
# Las características de x se han transformado de (x) a (1, x, x²)
poly_features = PolynomialFeatures(degree=2)
x_poly = poly_features.fit_transform(x)
print(x_poly)
poly_reg = LinearRegression()
poly_reg.fit(x_poly, y)
y_pred_poly = poly_reg.predict(x_poly)

# Calcular R^2 para ambos modelos
r2_lin = r2_score(y, y_pred_lin)
r2_poly = r2_score(y, y_pred_poly)

# Gráfico
plt.scatter(x, y, color='gray', label='Datos reales')
plt.plot(x, y_pred_lin, color='blue', label=f'Regresión Lineal (R^2 = {r2_lin:.2f})')
plt.plot(x, y_pred_poly, color='red', label=f'Regresión Polinómica (R^2 = {r2_poly:.2f})')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.legend()
plt.title('Comparación de Regresión Lineal y Polinómica')
plt.show()
