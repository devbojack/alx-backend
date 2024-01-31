#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the MRUCache instance """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            # Move the most recently used key to the end of the dictionary
            self.cache_data[key] = self.cache_data.pop(key)
            return self.cache_data[key]
        return None
