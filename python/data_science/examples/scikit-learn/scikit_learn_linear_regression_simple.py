import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
x = np.array([45, 50, 60, 60, 70, 80, 90, 90, 100, 110]).reshape(-1, 1)  # Independent variable (features)
y = np.array([150, 160, 200, 180, 230, 250, 300, 280, 300, 400])  # Dependent variable (target)

# Divida los datos de las 10 observaciones en conjuntos de entrenamiento y de prueba.
# De forma predeterminada, el 25 por ciento de las muestras se asigna al conjunto de prueba
# - test_size=4, si cogemos 4 observaciones para el test, asignan las otras 6 observaciones para el entrenamiento.
# - random_state: El uso de un int producirá los mismos resultados en diferentes llamadas. Las semillas aleatorias enteras populares son 0 y 42.
# - estratify=y, Si desea (aproximadamente) mantener la proporción de los valores de y a través de los conjuntos de entrenamiento y prueba.
# - shuffle=False: Puedes desactivar la mezcla aleatoria de datos y la división aleatoria con 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=4, random_state=42)
print(f"x_train: The training part of the first array (x) \n{x_train}")
print(f"x_test: The test part of the first array (x)\n{x_test}")
# [[100]
#  [ 50]
#  [ 80]
#  [ 45]]
print(f"y_train: The training part of the second array (y)\n{y_train}")
print(f"y_test: The test part of the second array (y)\n{y_test}")
# [300 160 250 150]

# Create the linear regression model
model = LinearRegression()
# Train the linear regression model
model.fit(x_train, y_train)

# Make predictions
# x        y         y_pred
# ==========================
# 100      300       344
# 50       160       146.5   
# 80       250       265
# 45       150       126.75
y_pred = model.predict(x_test)
print(f"y_pred: \n{y_pred}")
# [344.   146.5  265.   126.75]

# Evaluate the model
# Las distancias entre los valores reales y predichos se conocen como residuos o errores.
# La línea de mejor ajuste debe tener la suma de cuadrados más baja de estos errores, también conocida como "e cuadrado".
# x_test     y_test     y_pred       y_test - y_pred    (y_test - y_pred)**2
# ==========================================================================
# 100        300        344          -44                1936
# 50         160        146.5        13.5               182.25
# 80         250        265          -15                225
# 45         150        126.75       23.25              540.5625
#                                                       SUM() = 2883,8125 / 4 = 720.95

# Hacer un pronóstico
x_future = np.array(range(150, 160)).reshape(-1, 1)
forecast = model.predict(x_future)
print(f"forecast: \n{forecast}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
# Mean Squared Error: 720.95

# Coeficientes
# y_pred = ax + b
# - a: Es la ordenada de la recta en el origen, es decir el valor de y para x = 0)
# - b: Es la pendiente de la recta
# Precio para un piso de 100m2 > y_pred = 3.95 * 100 + (-51) = 344K € 
# Precio para un piso de 200m2 > y_pred = 3.95 * 200 + (-51) = 739K €
print(f"coeficiente a (slope): {model.coef_}")
# [3.95]
print(f"coeficiente b (intercept): {model.intercept_}")
# -51.00000000000006

# The coefficient of determination: 1 is perfect prediction
# Una estimación imparcial del rendimiento predictivo de su modelo se basa en datos de prueba:
r2 = r2_score(y_test, y_pred)
print(f"Coefficient of determination: {r2:.2f}")
print(f"Coefficient of determination train set: {model.score(x_train, y_train):.2f}")
print(f"Coefficient of determination test set: {model.score(x_test, y_test):.2f}")

plt.scatter(x_train, y_train, color='red', label='Data points train')
plt.scatter(x_test, y_test, color='blue', label='Data points test')
plt.plot(x, model.predict(x), color='green', label='Regression line', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



