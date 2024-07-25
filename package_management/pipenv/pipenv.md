# [Pipenv](https://pipenv.pypa.io/en/latest/index.html)

<!--TOC-->

- [LINKS](#links)
- [INSTALATION](#instalation)
- [VIRTUAL ENVIRONMENTS](#virtual-environments)
  - [pipenv run](#pipenv-run)
  - [pipenv shell](#pipenv-shell)
  - [pipenv graph](#pipenv-graph)
  - [pipenv requirements](#pipenv-requirements)
  - [Importing from requirements.txt](#importing-from-requirementstxt)
- [PACKAGES](#packages)
  - [pipenv install](#pipenv-install)
  - [pipenv uninstall](#pipenv-uninstall)
  - [pipenv update](#pipenv-update)
  - [pipenv upgrade](#pipenv-upgrade)
  - [pipenv sync](#pipenv-sync)
  - [pipenv lock](#pipenv-lock)

<!--TOC-->

---

Pipenv es un administrador de dependencias para proyectos Python y tiene como objetivo traer lo mejor de todos los mundos del empaquetado al mundo de Python.

Automáticamente crea y gestiona un entorno virtual para tus proyectos, así como añade/elimina paquetes de tu **Pipfile** a medida que instalas/desinstalas paquetes. Esto te permite reproducir fácilmente los entornos y también mejora la seguridad mediante la generación de un **Pipfile.lock**.

## LINKS

- [Official Website](https://pipenv.pypa.io/)
- [PyPI](https://pypi.org/project/pipenv/)
- [Commands](https://pipenv.pypa.io/en/latest/commands.html)
- [Releases](https://pipenv.pypa.io/en/latest/changelog.html)

## INSTALATION

- [Pipenv Installation](https://pipenv.pypa.io/en/latest/installation.html)

Asegúrate de tener python y pip

```bash
python --version
pip --version
```

La forma recomendada de instalar pipenv en la mayoría de las plataformas es instalar desde pypi usando **pip**:

```bash
pip install --user pipenv

# Para actualizar pipenv en cualquier momento
pip install --user --upgrade pipenv
```

## VIRTUAL ENVIRONMENTS

```bash
# Navigate to your project directory
mkdir my_project
cd my_project

# Initializing a Pipenv Environment > Esto creará un Pipfile en el directorio de tu proyecto si no existe ya y configurará un entorno virtual
pipenv install

# Installing Packages
# - Add the requests package to your Pipfile.
# - Install the package in your virtual environment.
# - Update the Pipfile.lock.
pipenv install requests
```

### pipenv run

Ejecutará un comando determinado desde virtualenv, con cualquier argumento reenviado

```bash
pipenv run python script.py
pipenv run pip freeze
```

### pipenv shell

Generará un shell con virtualenv activado. Este shell se puede desactivar usando exit.

```bash
pipenv shell
```

### pipenv graph

Muestra un gráfico de dependencias de sus dependencias instaladas donde cada nodo raíz es un especificador del **Pipfile**.

```bash
pipenv graph
```

### pipenv requirements

Genere un requirements.txt desde Pipfile.lock.

```bash
pipenv requirements
```
### Importing from requirements.txt

Para proyectos que utilizan un **requirements.txt**, pipenv puede importar el contenido de este archivo y crear un **Pipfile** y un **Pipfile.lock** para usted:

```bash
pipenv install -r path/to/requirements.txt
```

## PACKAGES

### pipenv install

Se utiliza para instalar paquetes en el entorno virtual pipenv y actualizar su Pipfile y Pipfile.lock.

```bash
pipenv install [package_name]
pipenv install requests
pipenv install requests==2.25.1
```

### pipenv uninstall

Se utiliza para desinstalar paquetes en el entorno virtual pipenv y actualizar su Pipfile y Pipfile.lock.

```bash
pipenv uninstall requests
```

### pipenv update

Actualizará el bloqueo de las dependencias y subdependencias especificadas únicamente e instalará las actualizaciones.

```bash
pipenv update [package_name]
```

### pipenv upgrade

Actualizará el bloqueo de la dependencia y subdependencias especificadas únicamente, pero no modificará el entorno


```bash
pipenv upgrade [package_name]
```

### pipenv sync

Instala las dependencias de **Pipfile.lock** sin ninguna alteración en el archivo de bloqueo.

### pipenv lock

se utiliza para actualizar todas las dependencias de **Pipfile.lock** a sus últimas versiones resueltas según su especificación de **Pipfile**.

