# crazy-cat-caretaker-iot
University of Iowa IOT Project, Spring 2023


## Using pipenv to manage your virtual environment (instructions written for mac)

Note: You can link your pipenv environment with an ide like Pycharm  
The pipenv Python interpreter is stored in `~/.local/share/virtualenvs`  
Never install packages through the IDE, still use the pipenv command in the terminal (fact check this)
###Link with more information
https://realpython.com/pipenv-guide/#pipenv-introduction

### Install pipenv locally

In your source code root directory:

    $ pip install pipenv

### Activating the virtual environment

In your source code root directory:

    $ pipenv shell

### lock environment (do this before committing)

    $ pipenv lock

### Deactivating the virtual environment

Do this when you woul dlike to leave the virtual environment:

    $ deactivate

### Updating the virtual environment

This will download any new dependancies added in version controll.

    $ pipenv install

### Install a new package

Use this to install new packages. This will update the Pipenv file for version control.

    $ pipenv install <package_name>
