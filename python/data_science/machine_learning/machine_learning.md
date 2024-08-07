# MACHINE LEARNING

<!--TOC-->

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

<!--TOC-->

---

Los algoritmos de aprendizaje automático se dividen en tres áreas:

## 1. Supervisado (Supervised)

Es un paradigma del aprendizaje automático en el que los objetos de entrada (por ejemplo, un vector de variables predictivas) y un valor de salida deseado entrenan un modelo.

Supervised machine learning consiste en crear modelos que asignan con precisión las entradas dadas a las salidas dadas. Las entradas también se denominan variables independientes o predictores, mientras que las salidas pueden denominarse variables dependientes o respuestas.

### Regression 

El análisis de regresión es uno de los campos más importantes de la estadística y el aprendizaje automático (machine learning).

La regresión busca relaciones entre **variables (variables)**. Por ejemplo, puede observar a varios empleados de alguna empresa e intentar comprender cómo sus salarios dependen de sus **características (features)**, como experiencia, nivel educativo, puesto, ciudad de empleo, etc.

Este es un problema de regresión donde los datos relacionados con cada empleado representan una **observación (observation)**.

La regresión también es útil cuando se desea **pronosticar (forecast)** una respuesta utilizando un nuevo conjunto de predictores.

**Example**

- Dependent variables: Variable objetivo o de respuesta que intentamos predecir o explicar
    - x = precios de la vivienda
- Independent variables: Variables / caracteristicas utilizadas para hacer las predicciones
    - y = precios de la vivienda  | x = superficie, el número de habitaciones, la distancia al centro de la ciudad, etc.

#### Simple linear regression 

#### Multiple linear regression

#### Polynomial linear regression 

### Classification 

## 2. Sin supervisión (Unsupervised)

## 3. Refuerzo (Reinforcement)

## Tools:

### 1. TensorFlow

[TensorFlow](https://www.tensorflow.org/) es una plataforma de código abierto de extremo a extremo para el aprendizaje automático.

### 2. Scikit-Learn

[Scikit-learn](https://scikit-learn.org/stable/) es una de las bibliotecas de machine learning más utilizadas en Python. 
- Construido sobre NumPy, SciPy y Matplotlib
- Es una herramienta sencilla y eficiente para tareas de análisis de datos predictivos.
- Links
    - [Datacamp > Python Machine Learning: Scikit-Learn Tutorial](https://www.datacamp.com/tutorial/machine-learning-python)

```bash
# Install package
pip install scikit-learn
```

### 3. PyTorch

Marco de aprendizaje profundo.

### 4. Keras

[Keras](https://keras.io/) es una API de redes neuronales de alto nivel, que se ejecuta sobre TensorFlow.

Tus modelos se ejecutan más rápido gracias a la compilación XLA con JAX y TensorFlow, y son más fáciles de implementar en todas las superficies gracias a los componentes de servicio de los ecosistemas TensorFlow y PyTorch

### 5. XGBoost

Librería optimizada de gradient boosting distribuido
