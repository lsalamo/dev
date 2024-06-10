
# [CONDA TERMINAL](https://docs.conda.io/projects/conda/en/latest/commands/index.html)

```bash
# Check conda version
conda -V
conda --version
> conda 24.5.0

# Information about Conda Version
conda info

# Help commands
conda init -h
conda init  --help

# Location of python directory
which conda
> /opt/anaconda3/bin/conda
```

## UPDATE CONDA AND ANACONDA

```bash
# Update the conda package manager to the latest version in your base environment
conda update -n base conda
# Use conda to update Anaconda to the latest version in your base environment
conda update -n base anaconda
```

## VIRTUAL ENVIRONMENTS

```bash
# Locate the directory for the conda environment
echo $CONDA_PREFIX
> /opt/anaconda3/envs/python-env

# list environments
conda env list
conda info -e
conda info --envs
> base                     /opt/anaconda3
> python-env            *  /opt/anaconda3/envs/python-env

# list of the packages in an environment
conda list -n [env_name]

# Change environment
conda activate [env_name]
conda deactivate

# Delete environment and packages
conda remove --name [env_name] --all

# Create R environment > https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/
conda create --name [env_name] r-essentials r-base

# Create Python environment
conda create --name [env_name] python=3.8

# Clone environment
conda create --name myclone --clone [env_name]
conda info --envs
```

[Create the environment from the environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

```bash
# Exporting the environment.yml file
conda activate [env_name]
conda env export > environment.yml

# Create the environment from the environment.yml file:
conda env create -f environment.yml
conda activate [env_name]

# Restoring an environment
conda list --revisions
conda install --revision=REVNUM # To restore environment to a previous revision
conda install --rev 8 # restore your environment to revision 8

# Updating our project with new dependencies
conda env update --file environment.yml
```

Example file environment.yml
```json
name: python-env
channels:
  - defaults
dependencies:
  - openssl=3.0.13
  - pip=24.0
  - python=3.12.3
  - setuptools=69.5.1
  - sqlite=3.45.3
  - wheel=0.43.0
  - conda-forge::numpy=1.21.*
  - nodejs=16.13.*  
  - pip
  - pip:
    - Flask-Testing  
variables:
  var1: value1
```

## VARIABLES

```bash
# List any variables you may have
conda env config vars list

# Set environment variables
conda env config vars set my_var=value
conda activate [env_name] # reactivate your environment
echo $my_var

# Unset the environment variable
conda env config vars unset my_var -n [env_name]
```

[Saving environment variables for secret keys](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables)

```bash
# Enter that directory and create these subdirectories and files:
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh

# Edit ./etc/conda/activate.d/env_vars.sh as follows:
#!/bin/sh
export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/

# Edit ./etc/conda/deactivate.d/env_vars.sh as follows:
#!/bin/sh
unset MY_KEY
unset MY_FILE
```


## UPDATE / INSTALL PACKAGES

```bash
# Install package_name to latest version
conda install [package_name]

# Install package_name to v5.0
conda install [package_name]=5.0.0

# List packages installed
conda list

# List all packages installed into the environment
conda list -n [env_name]

# List packages installed "python"
conda list | grep ^python
```



