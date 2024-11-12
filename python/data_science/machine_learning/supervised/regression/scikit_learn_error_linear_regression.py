from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score 
import numpy as np

y_true = np.array([3, 2.5, -2]) # Dependent variable (target)
y_pred = np.array([3.1, 2.5, -2.5])  # Prediction variable

################################ 
# Mean Absolute Error (MAE) is the average of absolute differences between actual and predicted values.

print(f"\nmae absolute difference: {abs(y_true - y_pred)}")
# mae absolute difference: [0.1 0.  0.5]
mae = np.sum(abs(y_true - y_pred)) / len(y_true)
print(f"Mean Absolute Error: {mae:.2f}")
# Mean Absolute Error: 0.20

mae = mean_absolute_error(
    y_true= y_true,
    y_pred = y_pred)
print(f"Mean Absolute Error: {mae:.2f}")
# Mean Absolute Error: 0.20

################################
# Mean Squared Error (MSE) is the average squared differences between actual and predicted values. 

print(f"\nmse squared difference: {(y_true - y_pred)**2}")
# mse squared difference: [0.01 0.   0.25]
mse = np.sum((y_true - y_pred)**2) / len(y_true)
print(f"Mean Squared Error: {mse:.2f}")
# Mean Squared Error: 0.09

mse = mean_squared_error(
    y_true= y_true,
    y_pred = y_pred)
print(f"Mean Squared Error: {mse:.2f}")
# Mean Squared Error: 0.09

################################
# Es particularmente útil para eliminar valores atípicos con grandes errores del modelo al elevarlos al cuadrado.

y_true_test = np.array([3, 2.5, -2, 2.3, 4, 5.1, 7.2]) # Dependent variable (target)
y_pred_test = np.array([3.1, 2.5, -2.5, 2.45, 4.1, 5.1, 20])  # Prediction variable

print(f"\nsquared difference: {(y_true_test - y_pred_test)}")
# squared difference: [ -0.1    0.     0.5   -0.15  -0.1    0.   -12.8 ]
mae = mean_absolute_error(
    y_true= y_true_test,
    y_pred = y_pred_test)
print(f"Mean Absolute Error: {mae:.2f}")
# Mean Absolute Error: 1.95

mse = mean_squared_error(
    y_true= y_true_test,
    y_pred = y_pred_test)
print(f"Mean Squared Error: {mse:.2f}")
# Mean Squared Error: 23.45

################################
# Root Mean Squared Error (RMSE) is the average squared differences between actual and predicted values. 

print(f"\nmse squared difference: {(y_true - y_pred)**2}")
# mse squared difference: [0.01 0.   0.25]
mse = np.sqrt(np.sum((y_true - y_pred)**2) / len(y_true)) 
print(f"Root Mean Squared Error: {mse:.2f}")
# Root Mean Squared Error: 0.29

mse = mean_squared_error(
    y_true= y_true,
    y_pred = y_pred)
print(f"Root Mean Squared Error: {np.sqrt(mse):.2f}")
# Root Mean Squared Error: 0.29

################################
# Coeficiente de determinacion R2

SSE = np.sum((y_true - y_pred) ** 2)  # Error cuadrático de las predicciones
print(f"\nSSE: {SSE:.2f}")
SST = np.sum((y_true - np.mean(y_true)) ** 2)  # Varianza total de los datos
print(f"SST: {SST:.2f}")
r2 = 1 - (SSE / SST)
print(f"Coefficient of determination (R2): {r2:.2f}")
# Coefficient of determination (R2): 0.98

r2 = r2_score(
    y_true=y_true,
    y_pred = y_pred)
print(f"Coefficient of determination (R2): {r2:.2f}")
# Coefficient of determination (R2): 0.98