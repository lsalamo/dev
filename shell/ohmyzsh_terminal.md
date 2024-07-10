# [OH MY ZSH](https://ohmyz.sh/)

```bash
# shell por defecto, existen diferentes interpretes, como bash, csh, zsh, fish, etc.
echo $SHELL
which zsh
> /bin/zsh

echo $ZSH
> /Users/luis.salamo/.oh-my-zsh

# shell version
zsh --version
> zsh 5.8 (x86_64-apple-darwin21.0)

# add plugin autocomplete 
# añadir al fichero config ~/.zshrc > plugins=(git zsh-autosuggestions)
> git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

## establecer como predeterminado

```bash
# Abre el archivo .zshrc 
nano ~/.zshrc

# Cambia el valor a tu tema preferido. Por ejemplo, para usar el tema "agnoster"
ZSH_THEME="agnoster"

# Guarda el archivo y recarga la configuración de Zsh:
source ~/.zshrc
```

## LINKS

### PLUGINS
#### GIT

#### TREE


```bash
brew install tree
tree -L 2
> .
> ├── docker_terminal.md
> ├── example
> │   ├── Dockerfile
> │   ├── app
> │   ├── compose.yaml
> │   └── requirements.txt
> ├── img
> │   ├── architecture.png
> │   ├── docker_swarm_architecture.png
> │   └── vscode.png
> └── index.md
```

### [THEMES](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)
* [agnoster/agnoster-zsh-theme](https://github.com/agnoster/agnoster-zsh-theme)
    * [Powerline Fonts](https://github.com/powerline/fonts)
    * [VS Code Patch](https://gist.github.com/480/3b41f449686a089f34edb45d00672f28?permalink_comment_id=3445724)