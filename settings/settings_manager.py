import json
import os


class Settings:
    """Custom class to store settings in a JSON file"""
    def __init__(self):
        self_path = os.path.dirname(__file__)
        settings_path = os.path.join(self_path, 'settings.json')
        self.settings_file:str = os.path.normpath(settings_path)
        
        # If the settings file doesn't exist, create it
        if not os.path.exists(self.settings_file):
            with open(self.settings_file, 'w') as settings:
                json.dump({'out_dir': './out', 'language_amount': 15}, settings, indent = 4)


    def read(self, key) -> str:
        """Retrieve the value associated with the given key from the JSON settings"""
        # Load the data from the settings file
        with open(self.settings_file, 'r') as settings:
            data:dict = json.load(settings)
        
        # Return the value associated with the given key
        return data.get(key, None)


    def write(self, key, value) -> None:
        """Write a value associated with the given key to the JSON settings"""
        # Load the data from the settings file
        with open(self.settings_file, 'r') as settings:
            data:dict = json.load(settings)
        
        # Update the given key/value pair
        data[key] = value

        # Update the settings file and indent for readability
        with open(self.settings_file, 'w') as settings:
            json.dump(data, settings, indent = 4)