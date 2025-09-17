from typing import List, Optional

def chunk(values: List[int], size: int) -> List[List[int]]:
    if size <= 0: raise ValueError("size must be > 0")
    return [values[i:i+size] for i in range(0, len(values), size)]

def running_total(start: int, changes: List[int]) -> List[int]:
    res, cur = [], start
    for c in changes:
        cur += c; res.append(cur)
    return res

def index_of_first_at_least(values: List[int], threshold: int) -> Optional[int]:
    for i, v in enumerate(values):
        if v >= threshold: return i
    return None