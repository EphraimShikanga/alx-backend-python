#!/usr/bin/env python3
"""takes an iterable lst and returns a list
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list"""
    return [(i, len(i)) for i in lst]
