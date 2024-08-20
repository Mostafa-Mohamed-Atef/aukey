import subprocess
import evdev

device_path = '/dev/input/event0'  

try:
    device = evdev.InputDevice(device_path) #device python will listen to
except FileNotFoundError:
    print(f"Device not found: {device_path}")
    exit(1)

path = "/home/mostafa/programming"
print("Listening...")
x= ""
for event in device.read_loop(): #for listening for event
    if event.type == evdev.ecodes.EV_KEY:
        key_event = evdev.categorize(event) # Only print on key press, not release
        if key_event.event.value == 0:
            x += str(key_event.event.code) #alt+f+f
            print(x)
        if x == '333356':
            subprocess.run(["xdg-open", path])
            break