import keyboard
from shortcuts_manager import ShortcutsManager

def main():
    manager = ShortcutsManager('paths.json')

    def on_key_event(event):
        manager.handle_key_event(event)

    print("Listening...")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')  # Use 'esc' to exit the script

if __name__ == "__main__":
    main()
