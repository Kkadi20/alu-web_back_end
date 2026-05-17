#!/usr/bin/env python3


"""
imported asyncio and random
function wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function wait_random
    parameters
        max_delay: integer 10
    returns float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
