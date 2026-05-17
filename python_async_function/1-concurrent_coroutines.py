#!/usr/bin/env python3


"""
import function from 0-basic...
"""

import asyncio
from typing import List
from asyncio import gather
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous funct wait_n
    parameters
    n(int) the number of times to spawn wait_random
    max_delay (int) the maximum delay in seconds
    returnsthe list of all the delays in ascending oder
    """
    tasks = [wait_random(max_delay) for x in range(n)]
    data_list = await gather(*tasks)
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    return new_list


if __name__ == "__main__":
    asyncio.run(wait_n)
