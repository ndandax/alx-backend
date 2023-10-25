#!/usr/bin/python3
""" module inherits from basecaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from base caching"""
    def __init__(self):
        """intializer"""
        super().__init__()

    def put(self, key, item):
        """assigning values and keys to dictionary"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """getting key"""
        if key is None:
            pass
        else:
            return self.cache_data.get(key)
