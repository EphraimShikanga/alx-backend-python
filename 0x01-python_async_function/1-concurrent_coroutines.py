#!/usr/bin/env python3
import asyncio
from typing import List
from functools import cmp_to_key

wait_random = __import__('0-basic_async_syntax.py').wait_random

async def wait_n(n, max_delay) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay ([type]): [description]

    Returns:
        List[float]: [description]
    """
    delays = []

    async def collect_delay(index: int):
        delay = await wait_random(max_delay)
        delays.append((index, delay))

    coroutines = [collect_delay(i) for i in range(n)]
    await asyncio.gather(*coroutines)

    delays.sort(key=cmp_to_key(lambda a, b: a[0] - b[0]))
    return [delay for _, delay in delays]
