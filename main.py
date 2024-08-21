import subprocess
import evdev
import json

#for listening to keyboard
with open('paths.json', 'r') as file:
    data = json.load(file)

device_path = data.get("keyboard")

def Linux():
    try:
        device = evdev.InputDevice(device_path) #device python will listen to
    except FileNotFoundError:
        print(f"Device not found: {device_path}")
        exit(1)

    print("Listening...")



    x= ""
    for event in device.read_loop(): #for listening for event
        if event.type == evdev.ecodes.EV_KEY:
            key_event = evdev.categorize(event) # Only print on key press, not release
            if key_event.event.value == 0:
                x += str(key_event.event.code) #alt+f+f , alt+e+e for Downloads
                print(x)
            match = next((key for key in data if key in x), None)
            if match:
                print('the file is opening please wait...')
                subprocess.run(["xdg-open", data[match]])
                x= ""
                print("Listening...")

Linux()