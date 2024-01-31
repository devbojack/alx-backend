#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the LRUCache instance """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Update the order list with the current key
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            # Update the order list with the most recently used key
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
