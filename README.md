# Trådfri Hue Workaround
Workaround Script for fixing brightness issue with IKEA Trådfri lights on Philips Hue Bridge. It
works by continuously polling the Hue Bridge to detect change in brightness, then resend the brightness command
to the Trådfri light after a short period.

## Why this project?
There's a compatibility issue with IKEA Trådfri lights and Philips Hue Bridge where the brightness
is not set correctly when changing scenes. The Hue Bridge will first send a command for color change,
then brightness. The Trådfri light will not accept any commands while it is busy changing the
color and discards the command to change its brightness. This results in a mismatch where the
Hue Bridge thinks the brightness has changed, while it has actually not changed. 

## Requirements
You'll need a PC or server where the script can run in the background. 

It's recommended to use a Python3 virtual environment to install the required module for this
script:

1. `python3 -m venv venv`
2. `. venv/bin/activate`
3. `python3 -m pip install --upgrade -r requirements.txt`

Afterwards, if you need to active the environment again, just run:

    . venv/bin/activate


## Usage
Simply start the script with Hue Bridge IP and Trådfri light ID's as argument. Press the
bridge button before running it the first time.

    ./tradfri_hue_workaround.py <bridge_ip> <light_id_1> <light_id_2> ...    

You can also list available lights and ID's:

    ./tradfri_hue_workaround.py <bridge_ip> -l

## Authentication against Philips Hue Bridge

The first time you run the script you need to press the button on the Philips Hue Bridge.
This is necessary to authenticate your client-software to send commands to the bridge. However,
this is just required once, since the "token" is saved locally on the client. 

The location of this token is `$HOME/.python_hue` and contains the IP of the bridge and your
username.

In other words, if you need to move this script to a new client (PC, server or container), this
file must be present to avoid pressing the button again.
