# https://www.w3schools.com/python/python_ml_linear_regression.asp

import matplotlib.pyplot as plt
from scipy import stats

# Sample data
x = [45, 50, 60, 60, 70, 80, 90, 90, 100, 110]  # Independent variable (features)
y = [150, 160, 200, 180, 230, 250, 300, 280, 300, 400]  # Dependent variable (target)

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(std_err)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

