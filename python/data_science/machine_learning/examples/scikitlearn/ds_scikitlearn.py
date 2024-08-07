from sklearn.linear_model import LinearRegression
import numpy as np

# Crear datos de ejemplo
X = np.array(range(100)).reshape(-1, 1)
y = np.array(range(100))

print(X)
print(y)

# Ajustar el modelo
model = LinearRegression()
# Entrenar el modelo
model.fit(X, y)

# Hacer un pronóstico
X_future = np.array(range(100, 110)).reshape(-1, 1)
forecast = model.predict(X_future)
print(forecast)