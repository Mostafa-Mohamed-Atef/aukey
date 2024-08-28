import json
import platform
import subprocess
from typing import Dict, Callable

class ShortcutsManager:
    def __init__(self, config_file: str):
        self.shortcuts = self.load_shortcuts(config_file)
        self.shortcut_dict = self.create_shortcut_dict(self.shortcuts)
        self.pressed_keys = ""
        self.os_function = self.get_os_function()

    def load_shortcuts(self, config_file: str) -> Dict:
        """Load key paths from JSON file."""
        with open(config_file, 'r') as file:
            return json.load(file)

    def create_shortcut_dict(self, shortcuts: Dict) -> Dict:
        """Create a dictionary from shortcuts for easy lookup."""
        return {item["shortcut"]: item for item in shortcuts}

    def get_os_function(self) -> Callable:
        """Return the appropriate function based on the OS."""
        os_handlers = {
            'Linux': self.linux,
            'Windows': self.windows,
            'Darwin': self.mac  # macOS
        }
        return os_handlers.get(platform.system(), self.unsupported_os)

    def handle_key_event(self, event):
        """Handle keyboard events and execute shortcuts."""
        if event.event_type == 'down':
            self.pressed_keys += event.name
        elif event.event_type == 'up':
            self.check_shortcut()

    def check_shortcut(self):
        """Check if the pressed keys combination matches any shortcut."""
        for shortcut, details in self.shortcut_dict.items():
            if self.pressed_keys.endswith(shortcut):
                print(f'\nThe {details["name"]} is opening, please wait...')
                self.os_function(details)
                self.pressed_keys = ""  # Clear keys after action
                print("Listening... To exit press 'esc'")
                return  # Exit after handling one shortcut

    def linux(self, details):
        subprocess.run(["xdg-open", details["path"]])

    def windows(self, details):
        subprocess.run(["start", details["path"]])

    def mac(self, details):
        subprocess.run(["open", details["path"]])

    def unsupported_os(self, details):
        print(f"{platform.system()} is unsupported")
