# aukey
**aukey** is a Python package designed to execute programs, files, and websites using customizable keyboard shortcuts. This package allows users to define shortcuts and associate them with specific actions, enabling quick and efficient access to frequently used resources.

## Features
 - Custom Shortcuts: Define custom keyboard shortcuts to execute programs, open files, or visit websites.
 - Flexible Configuration: Configure shortcuts using a dictionary or JSON file.
 - Multiple Action Types: Supports different action types, including executing programs, opening files, and launching URLs.
 - Cross-Platform Compatibility: Works on both Windows and Linux systems.
 - Installation
 - You can install aukey directly from PyPI using pip:

## Installation
You can install aukey directly from PyPI using pip:

```bash
pip install aukey
```
## Usage
Basic Setup
Import the package:

```python
import aukey
```
Create your shortcuts configuration:

You can define your shortcuts directly in the code or use an external JSON file.
Example configuration:

```python
shortcuts = [
    {"name": "Open Notepad", "shortcut": "ctrlaltn", "type": "program", "path": "notepad.exe"},
    {"name": "Open Google", "shortcut": "ctrlaltg", "type": "website", "path": "https://www.google.com"},
    {"name": "Open a Document", "shortcut": "ctrlaltd", "type": "file", "path": "C:/path/to/document.docx"},
]
```
Load the configuration:

```python
aukey.load_config(shortcuts)
```
Start listening for shortcuts:

```python
aukey.start_listening()
```
Using a JSON Configuration File
You can also load the configuration from a JSON file:

Create a JSON file with the following structure:

```json
[
    {"name": "Open Notepad", "shortcut": "ctrlaltn", "type": "program", "path": "notepad.exe"},
    {"name": "Open Google", "shortcut": "ctrlaltg", "type": "website", "path": "https://www.google.com"},
    {"name": "Open a Document", "shortcut": "ctrlaltd", "type": "file", "path": "C:/path/to/document.docx"}
]
```
Load the JSON file:

```python
aukey.load_config_from_file("shortcuts.json")
```
Start listening for shortcuts:

```python
aukey.start_listening()
```
Configuration Details
Each shortcut in the configuration must include the following keys:

name: A descriptive name for the action.
shortcut: The keyboard shortcut combination (e.g., ctrlaltg).
type: The type of action (program, file, or website).
path: The path to the program, file, or URL.
Example Configuration

```python
shortcuts = [
    {"name": "Open Notepad", "shortcut": "ctrlaltn", "type": "program", "path": "notepad.exe"},
    {"name": "Open Google", "shortcut": "ctrlaltg", "type": "website", "path": "https://www.google.com"},
    {"name": "Open a Document", "shortcut": "ctrlaltd", "type": "file", "path": "C:/path/to/document.docx"},
]
```
# Warnings
 - Configuration Format: When adding a dictionary or JSON file as the configuration, ensure it follows this format:
 
 ```json
 [
     {"name": "", "shortcut": "altff", "type": "", "path": ""},
     {"name": "", "shortcut": "altee", "type": "", "path": ""}
 ]
 ```
 - ### Avoid Common Shortcuts: Do not use shortcuts that are already widely used by the system or applications, such as Ctrl+C, Ctrl+V, Ctrl+Z, etc. Using these might interfere with standard operations and cause unexpected behavior.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

