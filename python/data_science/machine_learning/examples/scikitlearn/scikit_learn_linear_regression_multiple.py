import numpy as np
from sklearn.linear_model import LinearRegression

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

# Create and train the linear regression model
model = LinearRegression().fit(x, y)

# y_pred = model.intercept_ + model.coef_ * x
score = model.score(x, y)
print(f"coefficient of determination: {score}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")
# [5.77760476  8.012953   12.73867497 17.9744479  23.97529728 29.4660957 38.78227633 41.27265006]

# La respuesta prevista se obtiene con .predict(), que equivale a lo siguiente:
# y_pred = ax + b
y_pred =  np.sum(model.coef_ * x, axis=1) + model.intercept_
print(f"predicted response:\n{y_pred}")
# [5.77760476  8.012953   12.73867497 17.9744479  23.97529728 29.4660957 38.78227633 41.27265006]
