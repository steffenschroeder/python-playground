from typing import List, Tuple, Generator
from hypothesis import given, assume
from hypothesis.strategies import lists, integers

import pytest


def listrange(l_input: List[int]) -> Generator[Tuple[int, int], None, None]:
    if not l_input:
        return []
    l_input = list(sorted(set(l_input)))
    low = high = l_input[0]
    for l in l_input[1:]:
        if l - 1 == high:
            high = l
        else:
            yield low, high+1
            low = high = l
    else:
        yield low, high+1



@pytest.mark.parametrize(
    "inp, out",
    [
        ([], []),
        ([1], [(1, 2)]),
        ([1, 1], [(1, 2)]),
        ([-1, 0, 1], [(-1, 2)]),
        ([2, 1], [(1, 3)]),
        ([1, 2], [(1, 3)]),
        ([1, 3], [(1, 2), (3,4)]),
        ([1, 2, 4,5], [(1, 3), (4, 6)]),
    ],
)
def test_simple(inp, out):
    assert list(listrange(inp)) == out

def test_foo():
    for a in listrange([1,2,3,5,4]):
        x,y = a
        print(x,y)



@given(lists(integers()))
def test_h(l):
    result = listrange(l)
    print(result)

    all_results = []
    for r_low, r_high in result:
        all_results.extend(range(r_low, r_high))

    assert all_results == sorted(set(l))

# @given(l=integers(), h=integers())
# def test_h_l(l, h):
#     # assume(l<=h)
#     print(l, h)
#     inp = list(range(l, h))
#     res = listrange(inp)
#     assert len(res) == 1
#     assert (l, h) == res[0]
