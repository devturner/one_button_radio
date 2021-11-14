# RPi / Spotify one button player

Runs two services when the RPi is turned on, one to open a chromium browser to a Spotify playlist, another to monitor an arcade button for pressed events. 


## requirements:
- virtualenvwrapper - virtual env
- pip-tools - package managment 

On the Rpi:

`$pip install virtualenvwrapper`

Modify the bashrc:

`nano ~/.bashrc`
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
export PATH=/usr/local/bin:$PATH
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin
source ~/.local/bin/virtualenvwrapper.sh
```
`$source ~/.bashrc`


### make a virtualenv:

`$mkvirtualenv spotify_app`

`$workon spotify_app`


### Manage libraries:

`$pip-compile requirements.in`

`$pip install -r requirements.txt`

### Make sure the RPi has lbgpiod:

`$sudo apt-get install gpiod libgpiod-dev libgpiod-doc`

`export CFLAGS=-fcommon`

`pip3 install RPi.GPIO`



### running two systemd service units:

starts the spotify in browser:

`/etc/systemd/system/startupbrowser.service`

starts the python script listening for button presses

`/etc/systemd/system/spotify_button.service`

