#!/usr/bin/env python3


"""
import Iterable, Sequence, List and Tuple from typing
define function element_lenght
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function ellement_length
    paramesters
        lst: list
    returns a list
    """

    return [(i, len(i)) for i in lst]
