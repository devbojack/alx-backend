#!/usr/bin/env python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the LIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None:
            return self.cache_data.get(key)
        return None
