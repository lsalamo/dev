# [POETRY](https://python-poetry.org/)

<!--TOC-->

- [LINKS](#links)
- [INSTALLATION](#installation)
- [BASIC COMMANDS](#basic-commands)
  - [init](#init)
  - [new](#new)
  - [install](#install)
  - [update](#update)
  - [configuration](#configuration)
  - [environments](#environments)
  - [show](#show)
  - [add](#add)
  - [remove](#remove)
  - [run](#run)
  - [shell](#shell)
  - [build](#build)
  - [publish](#publish)

<!--TOC-->

---

Poetry es una herramienta de gestión de dependencias y empaquetado para proyectos de Python. Está diseñada para simplificar el proceso de configuración, instalación y actualización de dependencias, así como para facilitar la creación y publicación de paquetes Python.

## LINKS
- [Official Website](https://python-poetry.org/)
- [Documentation](https://python-poetry.org/docs/)
- [Commands](https://python-poetry.org/docs/cli/)
- [Releases](https://pypi.org/project/poetry/#history)
- [GitHub](https://github.com/python-poetry/poetry)

## INSTALLATION

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## BASIC COMMANDS

### init

Inicia un nuevo proyecto de Poetry en el directorio actual. Esto crea un archivo **pyproject.toml**, donde se definirán todas las dependencias y configuraciones del proyecto.

```bash
poetry init
> .
> └── pyproject.toml
```

output

```bash
This command will guide you through creating your pyproject.toml config.

Package name [example]:  poetry_package_example
Version [0.1.0]:  0.1.0
Description []:  poetry example
Author [luis-salamo <luis.salamo@adevinta.com>, n to skip]:  luis salamo <lsalamo@gmail.com>
License []:
Compatible Python versions [^3.12]:

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
You can specify a package in the following forms:
  - A single name (requests): this will search for matches on PyPI
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] requests
 [ 1] requests2
 [ 2] requests3
 [ 3] requests5
 [ 4] browser2requests
 [ 5] bw-requests
 [ 6] careful-requests
 [ 7] chibi-requests
 [ 8] cloud-requests
 [ 9] crawl-requests
 [ 10]
 > 0
Enter the version constraint to require (or leave blank to use the latest version):
Using version ^2.32.3 for requests

Add a package (leave blank to skip):

Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "poetry-package-example"
version = "0.1.0"
description = "poetry example"
authors = ["luis salamo <lsalamo@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

Do you confirm generation? (yes/no) [yes] yes
```
### new

Crea un nuevo proyecto en un directorio específico, configurando automáticamente el archivo pyproject.toml.

```bash
poetry new [project_name]
poetry new example
> example
> ├── example
> │   └── __init__.py
> ├── tests
> │   └── __init__.py
> ├── pyproject.toml
> └── README.md

# Si desea nombrar su proyecto de manera diferente a la carpeta, puede pasar la opción --name:
poetry new example --name poetry_src
> example
> ├── poetry_src
> │   └── __init__.py
> ├── tests
> │   └── __init__.py
> ├── pyproject.toml
> └── README.md
```
### install

Lee el archivo **pyproject.toml** del proyecto actual, resuelve las dependencias y las instala.

Si no hay ningún archivo **poetry.lock**, Poetry creará uno después de la resolución de la dependencia

```bash
poetry install
> example
> ├── poetry_src
> │   └── __init__.py
> ├── tests
> │   └── __init__.py
> ├── poetry.lock
> ├── pyproject.toml
> └── README.md
```

output

```text
Creating virtualenv dev-MfLEv65x-py3.12 in /Users/luis.salamo/Library/Caches/pypoetry/virtualenvs
Installing dependencies from lock file

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2024.7.4)
  - Installing charset-normalizer (3.3.2)
  - Installing idna (3.7)
  - Installing urllib3 (2.2.2)
  - Installing requests (2.32.3)

Installing the current project: dev (0.1.0)
```

### update

Para obtener las últimas versiones de las dependencias y actualizar el archivo **poetry.lock**, debe usar el comando de actualización

```bash
poetry update
```

### configuration

El comando config le permite editar repositorios y configuraciones de poetry.

```bash
# Poetry configuration
poetry config --list
```

output

![alt text](img/poetry_config.png)

### environments

```bash
poetry env info
# Si solo desea conocer la ruta al entorno virtual, puede pasar --path
poetry env info --path
poetry env list
```

output

```text
Virtualenv
Python:         3.12.3
Implementation: CPython
Path:           /Users/luis.salamo/Library/Caches/pypoetry/virtualenvs/dev-MfLEv65x-py3.12
Executable:     /Users/luis.salamo/Library/Caches/pypoetry/virtualenvs/dev-MfLEv65x-py3.12/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.3
Path:       /opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12
Executable: /opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/bin/python3.12
```

```bash
# deleting environments
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7
# Utilice la opción --all para eliminar todos los entornos virtuales a la vez.
poetry env remove --all
```

```bash
# add virtual environment in project
poetry config virtualenvs.in-project true
poetry install
> example
> ├── .venv
> ├── poetry_src
> │   └── __init__.py
> ├── tests
> │   └── __init__.py
> ├── poetry.lock
> ├── pyproject.toml
> └── README.md
```

output

```text
Creating virtualenv dev in /Users/luis.salamo/Documents/github/dev/package_management/poetry/example/.venv
```

![alt text](img/poetry_env.png)

### show

Lista todas las dependencias del proyecto, junto con sus versiones.

```bash
poetry show
```

output

```txt
certifi            2024.7.4 Python package for providing Mozilla's CA Bundle.
charset-normalizer 3.3.2    The Real First Universal Charset Detector. Open, modern an...
idna               3.7      Internationalized Domain Names in Applications (IDNA)
requests           2.32.3   Python HTTP for Humans.
urllib3            2.2.2    HTTP library with thread-safe connection pooling, file pos...
```

### add

Añade una nueva dependencia al proyecto y la instala. También actualiza pyproject.toml automáticamente.

```bash
poetry add [package_name]
poetry add requests
> Using version ^2.32.3 for requests
> Package operations: 5 installs, 0 updates, 0 removals
>  - Installing certifi (2024.6.2)
>  - Installing charset-normalizer (3.3.2)
>  - Installing idna (3.7)
>  - Installing urllib3 (2.2.1)
>  - Installing requests (2.32.3)
```

### remove

Elimina una dependencia del proyecto y actualiza pyproject.toml.

```bash
poetry remove [package_name]
poetry remove requests
```

### run

```bash
# Ejecutar un Comando en un Entorno Virtual
poetry run [package_name] [args]
poetry run python package_management/poetry/test_hola_mundo.py
```

### shell

```bash
# Abre una nueva shell en el entorno virtual del proyecto.
poetry shell
```
![](img/poetry_shell.png)

### build

Construye un package del proyecto. La carpeta por defecto es "dist"

```bash
poetry build
> example
> ├── .venv
> ├── poetry_src
> │   └── __init__.py
> ├── dist
> │   ├── poetry_src-0.1.0-py3-none-any.whl
> │   └── poetry_src-0.1.0.tar.gz
> ├── tests
> │   └── __init__.py
> ├── poetry.lock
> ├── pyproject.toml
> └── README.md
```

output

```text
Building poetry_src (0.1.0)
  - Building sdist
  - Built poetry_src-0.1.0.tar.gz
  - Building wheel
  - Built poetry_src-0.1.0-py3-none-any.whl
```

### publish

Para publicar su biblioteca, deberá [configurar correctamente sus credenciales de PyPI](https://python-poetry.org/docs/repositories/#configuring-credentials), ya que Poetry publicará la biblioteca en PyPI de forma predeterminada.

```bash
# Add new token (Perfil > Configuración de cuenta > Fichas de API > Añadir Ficha de API )
poetry config pypi-token.pypi [my-token]
poetry config pypi-token.pypi pypi-AgEIcHlwaS5vcmcCJDIyZWJiNmZjLTVkN2ItNDVkNy05M2Y3LTAxZmY2NzY3OTk2ZAACKlszLCIwMTg2YTc3YS0yYzMzLTQyY2EtYmM0MC1mYTk5NDU0NDdmYzYiXQAABiBKbN77OWoy8RXtDFomq2vDGWn8MC99Ld-NSKd_WWDIHQ

# Publica el paquete, previamente creado con el comando build, en el repositorio remoto.
poetry publish
```

output

```text
Publishing poetry_src (0.1.0) to PyPI
 - Uploading poetry_src-0.1.0-py3-none-any.whl 100%
 - Uploading poetry_src-0.1.0.tar.gz 100%
```

![alt text](img/poetry_publish.png)
