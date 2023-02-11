#!/usr/bin/env python3
"""
BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache is a Caching Eviction Strategy
    """
    def __init__(self):
        """
        Initializes the class with the parent's init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a Key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.order[-1]}")
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
