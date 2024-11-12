# GIT

LINKS

-  [20 Git Command-Line Tricks Every Developer Should Know](https://dev.to/jagroop2001/20-git-command-line-tricks-every-developer-should-know-1i21?context=digest)

# PACKAGES

## pre-commit

Los scripts de Git Hook son útiles para identificar problemas simples antes de enviarlos a la revisión del código.

Ejecutamos nuestros enlaces en cada confirmación para señalar automáticamente problemas en el código, como puntos y coma faltantes, espacios en blanco al final y declaraciones de depuración. hola

LINKS

- [Official Website](https://pre-commit.com/)
- [PyPI](https://pypi.org/project/pre-commit/)


```bash
# Check version
pre-commit --version
> pre-commit 3.7.1

# you can generate a very basic configuration
pre-commit sample-config

# Install the git hook scripts
pre-commit install

# (optional) Run against all the files
pre-commit run --all-files
```

