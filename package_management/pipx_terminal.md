# [PIPX](https://pipx.pypa.io/stable/)

Es una herramienta para instalar y ejecutar aplicaciones Python en entornos aislados. 

Crea entornos virtuales para cada aplicación, evitando conflictos de dependencias y garantizando un entorno limpio para cada aplicación. Esto significa que no entran en conflicto con otros paquetes instalados en su sistema.

## INSTALLATION

```bash
# Install package
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
```

## [BASIC COMMANDS](https://pipx.pypa.io/stable/docs/)

```bash
# Instalar una Aplicación
pipx install [package_name]

# Ejecutar una Aplicación Temporalmente
pipx run [package_name]

# Listar Aplicaciones Instaladas
pipx list

# Desinstalar una Aplicación
pipx uninstall [package_name]

# Actualizar una Aplicación
pipx upgrade [package_name]

# Reinstalar todas las Aplicaciones
pipx reinstall-all
```

## EXAMPLE

```python
# Install package/app
pipx install pycowsay
pipx install black

# List programs installed > 2 venvs created   
pipx list
> venvs are in /Users/luis.salamo/.local/pipx/venvs
> apps are exposed on your $PATH at /Users/luis.salamo/.local/bin
> manual pages are exposed at /Users/luis.salamo/.local/share/man
>    package black 24.4.2, installed using Python 3.12.3
>     - black
>     - blackd
>    package pycowsay 0.0.0.2, installed using Python 3.12.3
>     - pycowsay
>     - man6/pycowsay.6

# Run package/app
pipx run pycowsay moo
>   ---
> < moo >
>   ---
>    \   ^__^
>     \  (oo)\_______
>        (__)\       )\/\
>            ||----w |
>            ||     ||

pipx run black --version
> black, 24.4.2 (compiled: yes)
> Python (CPython) 3.12.3
```