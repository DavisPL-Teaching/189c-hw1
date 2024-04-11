"""
Part 3: Bug finding

This file contains a short program that calculates the "score" of a set
of currency denominations.
Unfortunately, it contains a bug -- your goal is to find and fix it.

=== Your task ===

Write at least one test using Hypothesis to identify for the bug.
Your test(s) don't have to cover all behaviors on all inputs, but they should
test a more interesting behavior than just a single input.

During testing, you can modify the code to fix the bug,
however, at the bottom of the file, fill in the function

    test_bug

with the test that was able to demonstrate the bug.
This function should fail on the original implementation and
pass on the fixed implementation.

=== Running the code ===

You can try out the code by running `python3 part3.py <list of integers>`.
For example:
```
    python3 part3.py 1 5 10 20 100
```
You can run your tests by running `pytest part3.py`.

=== Problem description ===

This program is about paper currency denominations.
For example, US currency is defined by the denominations
[1, 5, 10, 20, 50].

What is a good way to choose a set of currency denominations?

Let's define the "score" of a set of denominations as the product of:
    1. The average number of bills required to make a number from 1 to 100.
        For example, if the denominations are 1, 5, 10, 20, and 50, the number
        of bills required to make 47 is 5, 1 + 1 + 5 + 20 + 20. The average
        over all numbers from 1 to 100 turns out to be 4.22.
    2. The number of bills. For our example, this is 5, so the score would be 5 * 4.22 = 21.1.
(A lower score is better.)

The program is given as input a list of integers,
where at least one of the integers is 1.
The program outputs the score of the denominations.

=== Notes ===

You should think of this program as "someone else's code" -- you don't
necessarily want to rewrite it yourself, and it may have some conventions
you are not familiar with (for example, it is using type annotations).
So you shouldn't try to modify it directly.

Instead, try to understand what it's doing without reading every line.
Are there simple properties you can test about each method's behavior?
You don't have to write a test for every possible input -- pick
some interesting cases where you can easily predict what the output should be?

There is a constant N = 100 in the code. If it helps, you can modify
this constant to help with testing.
"""

import pytest

from typing import List

N = 100

# score function (in general, anything increasing
# in avg and numdenominations makes sense here)
def get_score(avg: float, numdenominations: int) -> int:
    return avg * numdenominations

# minimum number of bills to create the value i,
# given the list of denominations and the minimum number of bills
# to create values from 0 to i-1.
def min_next(i: int, demons: List[int], bills_for: List[int]) -> int:
    return min([
        1 + bills_for[i - d]
        for d in denoms
        if i - d >= 0
    ])

# avg # of bills to create a random value from 1 to N
def get_avg(denoms: List[int]) -> float:
    if 1 not in denoms:
        print("Warning: first denomination should be 1")
        # return infinity
        return float('inf')

    bills_for = [0]
    for i in range(1, N+1):
        best = min_next(i, denoms, bills_for)
        bills_for.append(best)

    # return sum of all costs over the total number of costs
    return sum(bills_for) / len(bills_for)

"""
Test demonstrating the bug

Unskip the test when it is ready.
"""

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
def test_bug():
    # TODO
    raise NotImplementedError

"""
Simple command-line interface

Don't modify this part -- it doesn't contain the bug.
"""

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', type=int, nargs='+',
        help='list of denominations'
    )
    denoms = parser.parse_args().integers
    print(f"Denominations provided: {denoms}")
    avg = get_avg(denoms)
    score = get_score(avg, len(denoms))
    print(f"avg: {round(avg, 2)}; number: {len(denoms)}")
    print(f"score: {round(score, 2)}")
