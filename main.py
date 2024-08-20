import subprocess
import evdev


#for listening to keyboard
device_path = '/dev/input/event0'  
try:
    device = evdev.InputDevice(device_path) #device python will listen to
except FileNotFoundError:
    print(f"Device not found: {device_path}")
    exit(1)

print("Listening...")
path = {'333356':'/home/mostafa/programming', '181856':'/home/mostafa/Downloads'}



x= ""
# path = "/home/mostafa/programming"
for event in device.read_loop(): #for listening for event
    if event.type == evdev.ecodes.EV_KEY:
        key_event = evdev.categorize(event) # Only print on key press, not release
        if key_event.event.value == 0:
            x += str(key_event.event.code) #alt+f+f
            print(x)
        match = next((key for key in path if key in x), None)
        if match:
            print('the file is opening please wait...')
            subprocess.run(["xdg-open", path[match]])
            break