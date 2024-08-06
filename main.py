import os
import evdev
# import pyautogui 

device_path = '/dev/input/event0'  

try:
    device = evdev.InputDevice(device_path) #device python will listen to
except FileNotFoundError:
    print(f"Device not found: {device_path}")
    exit(1)

for event in device.read_loop(): #for listening for event
    if event.type == evdev.ecodes.EV_KEY:
        key_event = evdev.categorize(event) # Only print on key press, not release
        print(key_event.event.code)