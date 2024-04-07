"""
Part 1: Mini exercises
"""

# def test_average_2(l1, l2):
#     assert average(l1 + l2) == (average(l1) + average(l2)) / 2

# def test_average_3(l1, l2):
#     avg1 = average(l1)
#     avg2 = average(l2)
#     assert min(avg1, avg2) <= average(l1 + l2) <= max(avg1, avg2)

# def test_average_4(l1, l2):
#     assert average(l1 + l2) == (len(l1) * average(l1) + len(l2) * average(l2)) / (len(l1) + len(l2))

# Skip
def ncr(n, k):
    # Return the number of ways to choose k items from n items
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

# An example with a function argument



def repeated_square(x, n):
    # TODO: implement
    pass

# The same program may satisfy different specifications.
