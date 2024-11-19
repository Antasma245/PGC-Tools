import json
import os


class Cache:
    """Custom cache class to store session-specific data in a JSON file"""
    def __init__(self):
        self.cache_file:str = 'cache/cache.json'
        
        # If the cache file doesn't exist, create it
        if not os.path.exists(self.cache_file):
            with open(self.cache_file, 'w') as cache:
                json.dump({}, cache, indent = 4)


    def read(self, key) -> str:
        """Retrieve the value associated with the given key from the JSON cache"""
        # Load the data from the cache file
        with open(self.cache_file, 'r') as cache:
            data:dict = json.load(cache)
        
        # Return the value associated with the given key
        return data.get(key, None)


    def write(self, key, value) -> None:
        """Write a value associated with the given key to the JSON cache"""
        # Load the data from the cache file
        with open(self.cache_file, 'r') as cache:
            data:dict = json.load(cache)
        
        # Update the given key/value pair
        data[key] = value

        # Update the cache file and indent for readability
        with open(self.cache_file, 'w') as cache:
            json.dump(data, cache, indent = 4)