#!/usr/bin/env python3
"""takes a tuple of floats and returns a tuple of floats"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...],
               factor: int = 2) -> Tuple[int, ...]:

    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: Tuple[int, int, int, int, int, int] = zoom_array(array)

zoom_3x: Tuple[int, int, int, int, int, int, int, int, int] = zoom_array(array, 3)
