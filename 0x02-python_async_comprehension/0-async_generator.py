#!/usr/bin/env python3
"""An async generator that yields a random number between 0 and 10"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)