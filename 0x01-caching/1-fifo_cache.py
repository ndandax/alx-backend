#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal method when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}\n")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
