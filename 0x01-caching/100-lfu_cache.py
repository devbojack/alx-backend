#!/usr/bin/env python3
""" LFUCache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the LFUCache instance """
        super().__init__()
        self.freq_count = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequency used item (LFU)
                discarded_key = min(self.freq_count, key=lambda k:
                                    (self.freq_count[k], self.cache_data[k]))
                del self.cache_data[discarded_key]
                del self.freq_count[discarded_key]
                print("DISCARD:", discarded_key)

            # Update the frequency count for the current key
            self.freq_count[key] = self.freq_count.get(key, 0) + 1
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            # Update the frequency count for the current key
            self.freq_count[key] = self.freq_count.get(key, 0) + 1
            return self.cache_data[key]
        return None
