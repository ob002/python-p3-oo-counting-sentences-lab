#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return isinstance(self._value, str) and self._value.endswith('.')

    def is_question(self):
        return isinstance(self._value, str) and self._value.endswith('?')

    def is_exclamation(self):
        return isinstance(self._value, str) and self._value.endswith('!')

    def count_sentences(self):
        if not isinstance(self._value, str) or not self._value.strip():
            return 0
        
        sentences = re.split(r'[.!?]+', self._value)
        
        return len([s for s in sentences if s.strip()])