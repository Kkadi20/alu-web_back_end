#!/usr/bin/env python3


"""
define function make_multiplier
import Callable from typing
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier
    parameters
        multiplier: float
    returns a function that muliplies a float by multiplier
    """

    def multiplication(x: float) -> float:
        return (x * multiplier)

    return multiplication
