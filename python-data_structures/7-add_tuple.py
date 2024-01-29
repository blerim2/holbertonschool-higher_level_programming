#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if all(isinstance(element, (int, float)) for element in tuple_a):
        if all(isinstance(element, (int, float)) for element in tuple_b):
            if len(tuple_a) < 2:
                tuple_a += (0,) * (2 - len(tuple_a))
            if len(tuple_b) < 2:
                tuple_b += (0,) * (2 - len(tuple_b))
            sum_tuple = tuple(a + b for a, b in zip(tuple_a[:2], tuple_b[:2]))
            return sum_tuple
