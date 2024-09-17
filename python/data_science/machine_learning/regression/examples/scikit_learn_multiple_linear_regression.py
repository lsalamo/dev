import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data x = "square meters" and y  = "price"
data = {
    'square_meters': [45, 50, 60, 60, 70, 80, 90, 90, 100, 110],
    'bedrooms': [1, 1, 1, 2, 2, 2, 2, 3, 4, 4],
    'Sales': [150, 160, 200, 180, 230, 250, 300, 280, 300, 400]
}
df = pd.DataFrame(data)
x = df[['square_meters', 'bedrooms']]  # Independent variable (features)
y = df['Sales']  # Dependent variable (target)

# Divida los datos de las 5 observaciones en conjuntos de entrenamiento y de prueba.
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(x, y)

# Get the coefficients and intercept
intercept = model.intercept_ 
coefficients = model.coef_ 
print("Coefficient β0 (Intercept):", intercept)
# -30.04105571847498
print("Coefficients β1 and β2 (slopes):", coefficients)
# [  3.96832845 -11.16715543]

# Hacer predicciones
y_pred = intercept + (x['square_meters'].values * coefficients[0]) + (x['bedrooms'].values * coefficients[1])
y_pred = model.predict(x)
print(f"y_pred:\n{y_pred}")
# [137.36656891 157.20821114 196.8914956  185.72434018 225.40762463 265.09090909 304.77419355 293.60703812 322.12316716 361.80645161]

# Evaluar el modelo
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
r2 = r2_score(y, y_pred)
print(f"Coefficient of determination: {r2:.2f}")

# Gráfico de predicciones vs reales
plt.scatter(y, y_pred, color='red', label='Predicciones vs Reales')
plt.plot([min(y), max(y)], [min(y), max(y)], color='green', linewidth=2, label=f'Regresión Lineal (R2 = {r2:.2f}, MSE = {mse:.2f})')
plt.title('Regresión Lineal Multiple')
plt.xlabel('x(venta real)')
plt.ylabel('y(venta predicha)')
plt.legend()
plt.show()

plt.scatter(df.index, y, color='red', label='Actual values')
plt.scatter(df.index, y_pred, color='blue', label='Predicted values')
plt.plot(df.index, y_pred, color='green', linewidth=2, label=f'Regresión Lineal (R2 = {r2:.2f}, MSE = {mse:.2f})')
plt.title('Regresión Lineal Multiple')
plt.xlabel('x(observaciones)')
plt.ylabel('y(venta)')
plt.legend()
plt.show()
