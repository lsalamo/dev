# DATA SCIENCE

<!--TOC-->

- [DATA MANIPULATION AND ANALYSIS](#data-manipulation-and-analysis)
  - [1. Pandas](#1-pandas)
  - [2. Scrapy](#2-scrapy)
  - [3. Datatable](#3-datatable)
- [MATHEMATICS AND STATISTICS](#mathematics-and-statistics)
  - [1. SciPy](#1-scipy)
  - [2. NumPy](#2-numpy)
  - [3. Natural Language Tookit (NLTK)](#3-natural-language-tookit-nltk)
  - [4. Statsmodels (SM)](#4-statsmodels-sm)
  - [5. Math](#5-math)
- [MACHINE LEARNING](#machine-learning)
  - [1. Supervisado (Supervised)](#1-supervisado-supervised)
    - [Regression](#regression)
      - [Simple linear regression](#simple-linear-regression)
      - [Multiple linear regression](#multiple-linear-regression)
      - [Polynomial linear regression](#polynomial-linear-regression)
    - [Classification](#classification)
  - [2. Sin supervisión (Unsupervised)](#2-sin-supervisión-unsupervised)
  - [3. Refuerzo (Reinforcement)](#3-refuerzo-reinforcement)
  - [Tools:](#tools)
    - [1. TensorFlow](#1-tensorflow)
    - [2. Scikit-Learn](#2-scikit-learn)
    - [3. PyTorch](#3-pytorch)
    - [4. Keras](#4-keras)
    - [5. XGBoost](#5-xgboost)
- [FORECASTING](#forecasting)
  - [Tensorflow](#tensorflow)
  - [StatsModels (SM)](#statsmodels-sm)
  - [Facebook - Prophet](#facebook---prophet)
- [Database Operations](#database-operations)
  - [PySpark](#pyspark)
  - [Hadoop](#hadoop)

<!--TOC-->

---

## DATA MANIPULATION AND ANALYSIS

### 1. Pandas

Pandas es una poderosa biblioteca Python de código abierto para análisis y visualización de datos. 

Proporciona potentes estructuras de datos, como DataFrame, y funciones integradas que facilitan el trabajo y la manipulación de datos.

Pandas también se puede utilizar para crear visualizaciones de datos, como diagramas y tablas, para ayudar a visualizar y explorar sus datos.

Example: [Glassdoor](https://www.glassdoor.com/Award/index.htm) ha creado una lista de los 50 mejores empleos en Estados Unidos, considerando factores como el salario medio, la satisfacción laboral y las ofertas de trabajo

### 2. Scrapy

### 3. Datatable

## MATHEMATICS AND STATISTICS

### 1. SciPy
Biblioteca utilizada para la computación científica y técnica.
- [freecodecamp > Guía de cálculo científico en Python. Matemáticas en SciPy y NumPy explicadas con ejemplos](https://www.freecodecamp.org/espanol/news/funciones-en-python-introduccion/)

### 2. NumPy
[NumPy](https://numpy.org/) es una de las bibliotecas de Python de código abierto más utilizadas y se utiliza principalmente para computación científica.

- Está diseñada específicamente para la manipulación de datos numéricos

### 3. Natural Language Tookit (NLTK)
[NLTK](https://www.nltk.org/) is a leading platform for building Python programs to work with human language data
Librería de matemática simbólica.

### 4. Statsmodels (SM)
Como se mencionó anteriormente, también se utiliza para el modelado estadístico.

### 5. Math

[Math](https://docs.python.org/es/3.10/library/math.html) proporciona acceso a las funciones matemáticas definidas en el estándar de C.

## MACHINE LEARNING

Los algoritmos de aprendizaje automático se dividen en tres áreas:

### 1. Supervisado (Supervised)

Es un paradigma del aprendizaje automático en el que los objetos de entrada (por ejemplo, un vector de variables predictivas) y un valor de salida deseado entrenan un modelo.

Supervised machine learning consiste en crear modelos que asignan con precisión las entradas dadas a las salidas dadas. Las entradas también se denominan variables independientes o predictores, mientras que las salidas pueden denominarse variables dependientes o respuestas.

#### Regression 

El análisis de regresión es uno de los campos más importantes de la estadística y el aprendizaje automático (machine learning).

La regresión busca relaciones entre **variables (variables)**. Por ejemplo, puede observar a varios empleados de alguna empresa e intentar comprender cómo sus salarios dependen de sus **características (features)**, como experiencia, nivel educativo, puesto, ciudad de empleo, etc.

Este es un problema de regresión donde los datos relacionados con cada empleado representan una **observación (observation)**.

La regresión también es útil cuando se desea **pronosticar (forecast)** una respuesta utilizando un nuevo conjunto de predictores.

**Example**

- Dependent variables: Variable objetivo o de respuesta que intentamos predecir o explicar
    - x = precios de la vivienda
- Independent variables: Variables / caracteristicas utilizadas para hacer las predicciones
    - y = precios de la vivienda  | x = superficie, el número de habitaciones, la distancia al centro de la ciudad, etc.

##### Simple linear regression 

##### Multiple linear regression

##### Polynomial linear regression 

#### Classification 

### 2. Sin supervisión (Unsupervised)

### 3. Refuerzo (Reinforcement)

### Tools:

#### 1. TensorFlow

[TensorFlow](https://www.tensorflow.org/) es una plataforma de código abierto de extremo a extremo para el aprendizaje automático.

#### 2. Scikit-Learn

[Scikit-learn](https://scikit-learn.org/stable/) es una de las bibliotecas de machine learning más utilizadas en Python. 
- Construido sobre NumPy, SciPy y Matplotlib
- Es una herramienta sencilla y eficiente para tareas de análisis de datos predictivos.
- Links
    - [Datacamp > Python Machine Learning: Scikit-Learn Tutorial](https://www.datacamp.com/tutorial/machine-learning-python)

```bash
# Install package
pip install scikit-learn
```

#### 3. PyTorch

Marco de aprendizaje profundo.

#### 4. Keras

[Keras](https://keras.io/) es una API de redes neuronales de alto nivel, que se ejecuta sobre TensorFlow.

Tus modelos se ejecutan más rápido gracias a la compilación XLA con JAX y TensorFlow, y son más fáciles de implementar en todas las superficies gracias a los componentes de servicio de los ecosistemas TensorFlow y PyTorch

#### 5. XGBoost
Librería optimizada de gradient boosting distribuido.

## FORECASTING

### Tensorflow

[TensorFlow](https://www.tensorflow.org/) y Keras son bibliotecas de aprendizaje profundo que pueden ser utilizadas para construir modelos de redes neuronales para pronósticos más complejos.

```bash
# Install package
pip install tensorflow
```

Ejemplo básico de uso

```python
import tensorflow as tf
import numpy as np

# Crear datos de ejemplo
X = np.array(range(100)).reshape(-1, 1)
y = np.array(range(100))

# Crear un modelo secuencial
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
model.fit(X, y, epochs=10)

# Hacer un pronóstico
X_future = np.array(range(100, 110)).reshape(-1, 1)
forecast = model.predict(X_future)
print(forecast)
```

```python
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)
data = np.random.rand(100) * 100  # 100 días de datos de demanda eléctrica
dias = np.arange(1, 101)
data = np.column_stack((dias, data))

# Normalizar los datos
data_norm = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Preparar datos para LSTM
X, y = data_norm[:-1], data_norm[1:, 1]

X = X.reshape((X.shape[0], 1, X.shape[1]))

# Definir modelo LSTM
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(1, 2)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Entrenar modelo
model.fit(X, y, epochs=300, verbose=0)

# Predicción
yhat = model.predict(X, verbose=0)

# Desnormalizar los datos
yhat_desnorm = (yhat * np.std(data[:, 1])) + np.mean(data[:, 1])

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(dias, data[:, 1], label='Datos Reales de Demanda Eléctrica')
plt.plot(dias, yhat_desnorm, label='Predicción LSTM', color='red')
plt.title('Predicción de Demanda Eléctrica con LSTM')
plt.xlabel('Días')
plt.ylabel('Demanda Eléctrica')
plt.legend()
plt.show()
```

### StatsModels (SM)

[Statsmodels](https://www.statsmodels.org/stable/index.html) es una biblioteca para la estimación de modelos estadísticos y la realización de pruebas estadísticas. Es muy útil para el análisis de series temporales y el pronóstico.

```bash
# Install package
pip install statsmodels
```

Ejemplo básico de uso

```python
import statsmodels.api as sm

# Cargar datos de ejemplo
data = sm.datasets.co2.load_pandas().data

# Ajustar un modelo ARIMA
model = sm.tsa.ARIMA(data, order=(1, 1, 1))
results = model.fit()

# Hacer un pronóstico
forecast = results.forecast(steps=10)
print(forecast)
```

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)
data = np.random.rand(100) * 200  # 100 meses de datos de ventas
meses = pd.date_range('2020-01-01', periods=100, freq='M')
df = pd.DataFrame(data, index=meses, columns=['Ventas'])

# Dividir en train y test
train = df.iloc[:-10]
test = df.iloc[-10:]

# Modelo ARIMA
model = ARIMA(train, order=(5,1,0))  # Ejemplo: ARIMA(5,1,0)
model_fit = model.fit()

# Predicción
forecast = model_fit.forecast(steps=10)

# Métricas de error
mae = np.mean(np.abs(forecast - test['Ventas']))
rmse = np.sqrt(np.mean((forecast - test['Ventas'])**2))

print(f'MAE: {mae}')
print(f'RMSE: {rmse}')

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Ventas'], label='Datos de Entrenamiento')
plt.plot(test.index, test['Ventas'], label='Datos Reales')
plt.plot(test.index, forecast, label='Predicción ARIMA', color='red')
plt.title('Predicción de Ventas con ARIMA')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()
plt.show()
```

### Facebook - Prophet

[Prophet](https://facebook.github.io/prophet/) es una herramienta desarrollada por Facebook para realizar pronósticos en series temporales. 
- Es especialmente útil para datos con tendencias y estacionalidades fuertes.
- Links
    * [Medium.com > Forecasting in Python with Facebook Prophet](https://towardsdatascience.com/forecasting-in-python-with-facebook-prophet-29810eb57e66)
    * [Medium.com > Forecasting con Prophet](https://medium.com/@angel.r.chicote/forecasting-con-prophet-7fb36b25eb4b)


```bash
# Install package
pip install prophet
```

Ejemplo básico de uso

```python
from prophet import Prophet
import pandas as pd

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'ds': pd.date_range(start='2020-01-01', periods=100, freq='D'),
    'y': range(100)
})

# Ajustar el modelo
model = Prophet()
model.fit(df)

# Hacer un pronóstico
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```

```python
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)
fechas = pd.date_range(start='2020-01-01', periods=100, freq='D')
ventas = np.random.rand(100) * 200
df = pd.DataFrame({'ds': fechas, 'y': ventas})

# Ajustar modelo Prophet
model = Prophet()
model.fit(df)

# Crear dataframe futuro y predecir
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Gráfica
fig1 = model.plot(forecast)
plt.title('Predicción de Ventas con Prophet')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.show()

# Componentes de la predicción
fig2 = model.plot_components(forecast)
```

## Database Operations

### PySpark

### Hadoop

