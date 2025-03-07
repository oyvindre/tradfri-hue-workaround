from phue import Bridge
from time import sleep, time
import argparse

class TradfriLight():
    def __init__(self, light, brightness_delay = 1.0):
        self._light = light
        self._last_brightness = light.brightness
        self._brightness_delay = brightness_delay
        self._has_changed = False
        self._t0 = time()

    def check_and_update(self):
        brightness = self._light.brightness
        if self._last_brightness != brightness:
            self._has_changed = True
            self._t0 = time()

        if self._has_changed and self._t0 + self._brightness_delay < time():
            self._light.brightness = brightness
            self._has_changed = False

        self._last_brightness = brightness

def main(bridge, args):
    tradfri_ids = args.light_ids
    light_list = bridge.get_light_objects()
    tradfri_lights = [TradfriLight(l, brightness_delay=args.brightness_delay) for l in light_list if l.light_id in tradfri_ids]

    while True:
        for light in tradfri_lights:
            light.check_and_update()
        
        sleep(args.poll_time)

def list_lights(b: Bridge):
    light_list = b.get_light_objects()
    print('Available lights:')
    for light in light_list:
        print(f'{light.light_id}: {light.name}')

if __name__ == '__main__':
    poll_default = 0.2
    delay_default = 1.2
    parser = argparse.ArgumentParser(description='Workaround script for IKEA Trådfri brightness issue on Philips Hue Bridge. Simply run the script with bridge IP and Trådfrid light ID\'s as argument. Remember to push the bridge button before starting the script the first time')
    parser.add_argument('bridge_ip')
    parser.add_argument('light_ids', nargs='*', type=float)
    parser.add_argument('-t', '--poll_time', default=poll_default, type=float, help=f'Set how often the lights are checked for brightness change. Value in seconds ({poll_default})')
    parser.add_argument('-d', '--brightness_delay',type = float, help=f'How long to wait after brightness is attempted changed before actually updating the brightness. Value in seconds ({delay_default})', default=delay_default)
    parser.add_argument('-l', '--list', action='store_true', required=False, default=False,help='List available lights')
    args = parser.parse_args()

    b = Bridge(args.bridge_ip)
    b.connect()
    b.get_api()

    if args.list:
        list_lights(b)
    elif len(args.light_ids) > 0:
        main(b, args)
    else:
        print('No light IDs provided')