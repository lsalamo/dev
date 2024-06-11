# [HOMEBREW](https://brew.sh/)

Homebrew es quizás el gestor de paquetes más popular para macOS. Facilita la instalación, actualización y eliminación de software desde la línea de comandos.

## BREW HELP

```bash
# Check the system Homebrew version
brew --version
> Homebrew 3.6.21

# Print Help Information
brew help

# Print Help Info for a brew command
brew help [sub-command]

# Check system for potential problems.
brew doctor

# Brew configuration
brew config
```
## BREW SEARCH

```bash
# List all the installed formulae.
brew list

# Display all locally available formulae for brewing.
brew search

# Perform a substring search of formulae names for brewing.
brew search [text]

# Display information about the formula.
brew info [package_name]
```

## BREW UPDATE

```bash
# Este comando descarga la base de datos las últimas versiones de las fórmulas y casks disponibles desde el repositorio oficial de Homebrew (No cambia nada en tu sistema más allá de la base de datos de Homebrew.)
brew update

# Ver la base de datos
brew outdated

awscli (2.9.21) < 2.16.5
ca-certificates (2023-01-10) < 2024-03-11
docutils (0.19_1) < 0.21.2
mpdecimal (2.5.1) < 4.0.0
openssl@1.1 (1.1.1t) < 1.1.1w
python@3.11 (3.11.1) < 3.11.9
readline (8.2.1) < 8.2.10
six (1.16.0_3) < 1.16.0_4
sqlite (3.40.1) < 3.46.0
xz (5.4.1) < 5.4.6

# Actualiza los paquetes instalados a las versiones más recientes disponibles en la base de datos de Homebrew
brew upgrade

# Upgrade only the specified formulae
brew upgrade [package_name]
brew upgrade python@3.11

# Prevent the specified formulae from being upgraded
brew pin [package_name]

# Allow the specified formulae to be upgraded.
brew unpin [package_name]
```

## BREW INSTALL

```bash
# Install the formulae.
brew install [package_name]

# Uninstall the formulae.
brew uninstall [package_name]
brew uninstall python@3.11
```

## BREW CLEANUP

```bash
# Remove older versions of installed formulae.
brew cleanup

# Remove older versions of specified formula.
brew cleanup <formula>

# Display all formula that will be removed (dry run)
brew cleanup -n
```
