"""Module describing the sorting key-functions"""
from random import random

lexicographical_order_key = lambda x: x

length_order_key = lambda x: len(str(x))

random_order_key = lambda x: random()
