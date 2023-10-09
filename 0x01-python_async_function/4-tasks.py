import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    async def collect_delay(index: int):
        task = await task_wait_random(max_delay)
        delay = await task
        delays.append((index, delay))

    coroutines = [collect_delay(i) for i in range(n)]
    await asyncio.gather(*coroutines)

    delays.sort(key=lambda x: x[0])
    return [delay for _, delay in delays]