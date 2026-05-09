#!/usr/bin/env python3


"""
imported List and Union from typing
define a function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list sum list arguments
    parameters:
        mxd_lst: list of integers and floats
    returns arguments sum as a float
    """

    total = 0.0
    for num in mxd_lst:
        total += num
    return total
