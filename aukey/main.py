import keyboard
import json
import platform
import subprocess
from typing import Dict, Callable

pressed_keys = []

def load_shortcuts(config_file: str) -> Dict:
    """Load key paths from JSON file."""
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except:
        return config_file

def create_shortcut_dict(shortcuts: Dict) -> Dict:
    """Create a dictionary from shortcuts for easy lookup."""
    return {item["shortcut"]: item for item in shortcuts}

def get_os_function() -> Callable:
    """Return the appropriate function based on the OS."""
    os_handlers = {
        'Linux': linux,
        'Windows': windows,
        'Darwin': mac
    }
    return os_handlers.get(platform.system(), unsupported_os)

def handle_key_event(event, shortcut_dict, os_function):
    """Handle keyboard events and execute shortcuts."""
    global pressed_keys
    if event.event_type == 'down':
        pressed_keys.append(event.name)
        if len(pressed_keys)>10:
            pressed_keys.pop(0)
    elif event.event_type == 'up':
        check_shortcut(shortcut_dict, os_function)

def check_shortcut(shortcut_dict: Dict, os_function: Callable):
    """Check if the pressed keys combination matches any shortcut."""
    global pressed_keys
    keys_joined = ''.join(pressed_keys)
    for shortcut, details in shortcut_dict.items():
        if keys_joined.endswith(shortcut):
            print(f'\nThe {details["name"]} is opening, please wait...')
            os_function(details)
            pressed_keys = []  
            print("Listening... To exit press 'esc'")
            return  

def linux(details):
    subprocess.run(["xdg-open", details["path"]])

def windows(details):
    subprocess.run(f'start "" "{details["path"]}"', shell=True)

def mac(details):
    subprocess.run(["open", details["path"]])

def unsupported_os(details):
    print(f"{platform.system()} is unsupported")

def start_listening(config_file: str):
    """Start listening for keyboard shortcuts using the specified config file."""
    shortcuts = load_shortcuts(config_file)
    shortcut_dict = create_shortcut_dict(shortcuts)
    os_function = get_os_function()

    def on_key_event(event):
        handle_key_event(event, shortcut_dict, os_function)

    print("Listening....")
    keyboard.hook(on_key_event)
    keyboard.wait('esc') 
