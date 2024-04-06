# Trådfri Hue Workaround
Workaround Script for fixing brightness issue with IKEA Trådfri lights on Philips Hue Bridge. It
works by continuously polling the Hue Bridge to detect change in brightness, then resed the brightness command
to the Trådfri light after a short period.

## Requirements
You'll need a PC or server where the script can run in the background. 
Install python requirements with
```
pip3 install phue
```
or
```
pip3 install -r requirements.txt
```
 
## Usage
Simply start the script with Hue Bridge IP and Trådfri light ID's as argument. Press the
bridge button before running it the first time.
```
python3 tradfri_hue_workaround.py <bridge_ip> <light_id_1> <light_id_2> ...    
```

You can also list available lights and ID's:
```
python3 tradfri_hue_workaround.py <bridge_ip> -l
```


## Background
There's a compatibility issue with IKEA Trådfri lights and Philips Hue Bridge where the brightness
is not set correctly when changing scenes. The Hue Bridge will frist send a command for color change,
then brightness. The Trådfri light will not accept any commands while it is busy changing the
color and discards the commant to change its brightness. This results in a missmatch where the
Hue Bridge thinks the brightness has changed, while it has actually not changed. 

 
