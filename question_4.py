from typing import List, Dict, Optional


def find(list_of_dictionaries: List) -> Optional[Dict]:
    element = dict()
    while element is not None:
        element = next(list_of_dictionaries, None)
        if element is None:
            return dict()
        if element.get("x", 0) == 5:
            return element
    return element


case_one = iter([{"x": n, "y": n * 2} for n in range(5)])
result_one = find(case_one)


case_two = iter([{"x": n, "y": n * 2} for n in range(12)])
result_two = find(case_two)
