import subprocess
import keyboard
import json

# Load key paths from JSON file
with open('paths.json', 'r') as file:
    shortcuts = json.load(file)

# Create a dictionary from shortcuts for easy lookup
shortcut_dict = {item["shortcut"]: item["path"] for item in shortcuts}

def main():
    # Track pressed keys
    pressed_keys = ""

    def on_key_event(event):
        nonlocal pressed_keys

        if event.event_type == keyboard.KEY_DOWN:
            pressed_keys += event.name
        elif event.event_type == keyboard.KEY_UP:
            # Check if the pressed_keys combination matches any shortcut
            match = next((key for key in shortcut_dict if key in pressed_keys), None)
            # if pressed_keys in shortcut_dict:
            if match:
                print('The file is opening, please wait...')
                subprocess.run(["xdg-open", shortcut_dict[match]])
                pressed_keys = ""  # Clear keys after action
                print("Listening...")

    print("Listening...")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')  # Use 'esc' to exit the script

if __name__ == "__main__":
    main()
