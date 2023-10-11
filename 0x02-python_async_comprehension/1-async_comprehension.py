#!/usr/bin/env python3
"""An async comprehension that returns a list of random numbers between 0 and 10"""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Return a list of random numbers between 0 and 10"""
    return [i async for i in async_generator()]

