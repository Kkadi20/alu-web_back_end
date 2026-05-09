#!/usr/bin/env python3


"""
import Union and Tuple from typing
Define a function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv
    parameters
        k: string
        v: an int or float
    returns a tuple
    """

    return (k, float(v ** 2))
