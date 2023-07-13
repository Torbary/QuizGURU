#!/usr/bin/python3
class Singleton:
    _instance = None
    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance
