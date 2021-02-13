# -*- coding: utf-8 -*-
"""
Exploring ways to use mapping with python 2.7's version of the
multiprocessing package
"""
from multiprocessing import Pool
from functools import partial

def append(word, times=2, separator=','):
    """Return the given word times number of times separated by the separator."""
    return separator.join([word for x in range(times)])

def append_star(args):
    """Call the append function using the given tuple of arguments."""
    return append(*args)

def append_star_star(args):
    """Call the append function using the given dictionary of arguments."""
    return append(**args)

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        res = pool.map(append, ['c', 'd', 'eg'])
        print(res)

        lambda_replace = partial(append, times=3, separator="|")
        res = pool.map(lambda_replace, ['c', 'd', 'eg', 'de', 'e'])
        print(res)

        values = [('c', 2), ('d', 3), ('eg', 1), ('ge', 4)]
        res = pool.map(append_star, values)
        print(res)

        values = [{'word': 'c', 'times': 2}, {'word': 'd', 'times': 3}, \
                  {'word': 'eg', 'times': 5, 'separator': '|'}]
        res = pool.map(append_star_star, values)
        print(res)
