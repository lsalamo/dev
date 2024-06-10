# PYTHON TERMINAL

```bash
# Check the system Python version
python --version
> Python 3.11.7

# Check the Python 2 version
python2 --version
> Python 2.7.16

# Check the Python 3 version
python3 --version
> Python 3.11.7

# Location of python directory
which python
> /opt/anaconda3/bin/python

# Location of python3 directory
which python3
> /opt/anaconda3/bin/python3

# Check the pip version
python3 -m pip --version
> pip 23.3.1 from /opt/anaconda3/lib/python3.11/site-packages/pip (python 3.11)
```

## VIRTUAL ENVIRONMENTS

### [USING VENV](https://docs.python.org/3/library/venv.html)

```bash
# Create virtual environment
python3 -m venv [env_name]

# Activate virtual environment
source tutorial_env/bin/activate

# Desactivate virtual environment
deactivate
```

### [USING VIRTUALENV](https://virtualenv.pypa.io/en/stable/index.html)


Es una biblioteca que ofrece más funcionalidades que venv.Aunque puedes crear un entorno virtual usando venv con Python3, se recomienda que instales y use virtualenv en su lugar.

```bash
# Actualizar primero a pip3
python3 -m pip install --upgrade pip

# Install virtualenv package
pip3 install virtualenv  

# Create virtual environment
python3 -m virtualenv [env_name]

# Activate virtual environment
source [env_name]/bin/activate

# Desactivate virtual environment
deactivate

# Delete virtual environment
rm -rf venv
```

## VARIABLES

[Medium.com > Three Different Ways to Store Environment Variables](https://medium.com/@dataproducts/python-three-different-ways-to-store-environment-variables-15224952f31b)

```bash
# List any variables you may have
env

# Set environment variables
# 1. Use .env File to Store Environment Variables
# 2. Store Environment Variables in Virtual Environment
# 3. Storing Environment Variables in Dockerfile

# Unset the environment variable
conda env config vars unset my_var -n [env_name]
```

## UPDATE / INSTALL PACKAGES

The most common usage of pip is to install from the [Python Package Index (PyPI)](https://pypi.org/)

```bash
# Install package_name to latest version
python3 -m pip install [package_name]

# Install package_name to v5.0
python3 -m pip install [package_name]=5.0.0

# Upgrade an already installed SomeProject to the latest from PyPI.
python3 -m pip install --upgrade [package_name]

# List packages installed
pip list

# List packages installed "python"
pip list | grep python

# Show information about package
pip show [package_name]
```

## MANAGING PACKAGE DEPENDECIES

Pip es una excelente opción para proyectos pequeños y medianos. Pip se apoya en un archivo llamado **requirements.txt** que lo utiliza para registrar las dependencias del proyecto. Contiene una lista de los paquetes de Python necesarios, junto con sus versiones específicas o restricciones de versión.

```bash
# Install package_name to latest version
python3 -m pip install -r requirements.txt
```

Después de instalar las dependencias usando pip, ejecuta el siguiente comando en la terminal:

```bash
# Registrar nuestras dependencias en el archivo requirements.txt
pip freeze > requirements.txt
```

Este comando captura todas las dependencias instaladas y sus versiones exactas en un archivo **requirements.txt**. Puedes incluir este archivo en tu repositorio para que otros desarrolladores puedan replicar el entorno.

Es una buena práctica ejecutar el comando pip freeze para actualizar el archivo **requirements.txt** cada vez que instalas una nueva dependencia o actualizas una existente en tu entorno de desarrollo