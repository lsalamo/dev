# GIT

## GITHUB

### View commits

- Navigate to the Repository

```bash
https://github.com/lsalamo/[repository]
```

- Click on the "**Commits**" link, which is usually found under the "Code" tab. This will take you to the list of commits in that repository.

```bash
https://github.com/lsalamo/[repository]/commits/master/
```

### View commit with ID

- Navigate to the Repository
- Click on the "**Commits**" link and locate specific commit.
- You can directly append /commit/ followed by the commit ID. For example:

```bash
https://github.com/lsalamo/[repository]/commit/277002b7a4149bff96250b32823a88c43f4ed0a4
```

### View history file

- Navigate to the Repository
- Locate the File. Then, click on the "**History**" button or link, usually found at the top of the file view page.
- You can directly append /commits/brand followed by the path to file. For example:

```bash
https://github.com/lsalamo/dev-training/commits/master/src/libs/adobe/adobe_analytics_api.py
```

### View the contents of a file before specific commit

- Navigate to the Repository
- Click on the "**Commits**" link and locate specific commit.

```bash
https://github.com/lsalamo/[repository]/commit/277002b7a4149bff96250b32823a88c43f4ed0a4
```
- Copy the Parent Commit ID, the parent commit ID is usually displayed near the top of the commit details.
- Navigate to the File View

```bash
https://github.com/lsalamo/[repository]/blob/parent_commit_id/path/to/file

https://github.com/lsalamo/dev-training/blob/dc1e3df4806b257868edd02254ebdbcd76dbed42/libraries/api_adobe_analytics2_0.py
```

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

