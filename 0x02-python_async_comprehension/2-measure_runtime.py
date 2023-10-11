#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime"""
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = asyncio.get_running_loop().time()
    return end - start