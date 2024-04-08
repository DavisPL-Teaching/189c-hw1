"""
Part 1: Mini exercises
"""

from hypothesis import given
from hypothesis import strategies as st
import pytest

"""
A. Writing specifications, part 1

Consider the average function that we discussed in lecture.
Write a specification for the following properties,
and use Hypothesis to check which of them hold.

For each property, you should use floating point numbers
between -10000 and 10000 (to avoid overflow).
If needed, you can also bound the list size (e.g., to size 100)

- To run the test after implementing it, remove the skip annotation:
@pytest.mark.skip(reason="Unimplemented")

- If the property does not hold, add the annotation
@pytest.mark.xfail(reason="The property is not true")
to tell pytest that the test is expected to fail.
We will use this during grading to check if you have correctly identified the properties!

The @given annotation is written for you for the first one.

1. The average of a list of nonnegative numbers is nonnegative.

2. The average of x and -x is 0.

3. The average of a list of numbers that are all the same number x is equal to x.

4. The average of a concatenation of two lists l1 and l2 is equal to the average of
the two averages of l1 and l2.

5. The average of a concatenation of two lists l1 and l2 is between the averages of
l1 and l2, up to a small error (say, .000001).
(Hint: you may need to use the min and max function)

6. The average of a concatenation of two lists l1 and l2 is equal to
(len(l1) * average(l1) + len(l2) * average(l2)) / (len(l1) + len(l2)),
up to a small error (say, .000001).
(Hint: you may need to use the abs function)
"""

def average(l):
    return sum(l) / len(l)

@given(
    st.lists(
        st.floats(min_value=0,max_value=10000),
        min_size=1,
    )
)
def test_average_1(l):
    assert average(l) >= 0
    pass

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_average_2(x):
    # TODO
    pass

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_average_3(x, n):
    # TODO
    pass

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_average_4(l1, l2):
    # TODO
    pass

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_average_5(l1, l2):
    # TODO
    pass

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_average_6(l1, l2):
    # TODO
    pass

"""
Now answer these questions:
7. For each property that failed, why did it fail?

8. Which property was the most surprising to you and why?
"""

"""
B. Writing specifications, part 2
"""



"""
C. Fast Fahrenheit-Celsius conversion

This exercise is about playing with preconditions!
We will use Hypothesis to determine the largest possible
set of inputs for which a given specification holds.

Here is a popular "mental math" trick to convert Fahrenheit to Celsius:
Subtract 30 from the Fahrenheit temperature and divide by 2.
Example: 70 degrees Fahrenheit is approx. (70 - 30) / 2 = 20 degrees Celsius.
(You can also do the reverse to convert Celsius to Fahrenheit.)

Below, we provide a conversion function both ways that uses this trick.
For simplicity, we round the input/output of both functions to the nearest
integer, using the built-in `round` function.
(It rounds to the nearest even number in case of a tie -- e.g. round(2.5) = 2.)

We also provide the "true" conversion functions that use the exact formula,
and these also round to the nearest integer.
"""

def f_to_c_v1(f):
    return round((f - 30) / 2)

def c_to_f_v1(c):
    return round(c * 2 + 30)

def true_f_to_c(f):
    return round((f - 32) * 5/9)

def true_c_to_f(c):
    return round(c * 9/5 + 32)

"""
9. Use Hypothesis to determine for which inputs the conversion above
(the _v1 functions) is close to correct: within an error of 5 degrees.

The interesting part here is the @given annotation --
you should play with the minimum and maximum values
    min_value=...
    max_value=...
to see for which values the test passes.
Your final answer should have a @given annotation with the minimum as small
as possible and the maximum as large as possible, such that the test passes.

Note: you may need to change max_examples to get some tests to fail reliably.
You can do that by adding:
from hypothesis import settings
@settings(max_examples=500)
which we have added for the tests below.
By default, only 100 examples are tested.

Remember to remove @pytest.mark.skip(reason="Unimplemented")
once you have implemented each test.
"""

from hypothesis import settings

@pytest.mark.skip(reason="Unimplemented")
# @given(st.integers(..))
@settings(max_examples=500)
def test_f_to_c_v1(f):
    # In Python, a better style than using 'pass' to indicate unimplemented
    # functions is to raise a NotImplementedError exception.
    # We will use this style in the rest of the file.
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(st.integers(..))
@settings(max_examples=500)
def test_c_to_f_v1(c):
    # TODO
    raise NotImplementedError

"""
11. Here is a more precise trick:
For F to C, subtract 32, then divide by two, and let that result be x.
Then compute x / 10 (float division) and add it to x.
Round the result to the nearest integer.
Example:
68 F -> 68 - 32 = 36 -> 36 / 2 = 18 -> 18 / 10 = 1.8 -> 18 + 1.8 = 19.8 -> 20 C.

For C to F, multiply by 2, and let that result by x.
Then compute x / 10 (integer division) and subtract it from x.
Finally, add 32, and round to the nearest integer.
Example:
20 C -> 20 * 2 = 40 -> 40 / 10 = 4 -> 40 - 4 + 32 = 68 F.

Implement both functions, then use Hypothesis to check for which inputs
the conversion is close to correct: within 1 degree of the true conversion.
"""

def f_to_c_v2(f):
    # TODO
    raise NotImplementedError

def c_to_f_v2(c):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
# @settings(max_examples=500)
def test_f_to_c_v2(f):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
# @settings(max_examples=500)
def test_c_to_f_v2(c):
    # TODO
    raise NotImplementedError

"""
12. We would like it to be true that converting from C to F and then back,
followed by converting back to C and then to F, gives the original value.
x -> convert to F -> convert to C -> x
Similarly:
x -> convert to C -> convert to F -> x

Write a test that checks both properties using Hypothesis,
and find the smallest and largest values for which the property holds.
"""

# @given(..)
# @settings(max_examples=500)
@pytest.mark.skip(reason="Unimplemented")
def test_f_to_c_to_f(x):
    # TODO
    raise NotImplementedError

# @given(..)
# @settings(max_examples=500)
@pytest.mark.skip(reason="Unimplemented")
def test_c_to_f_to_c(x):
    # TODO
    raise NotImplementedError

"""
C. TODO

For this part, we will ask you to write the *strongest possible*
specification for the function.
The input precondition (@given) is given to you.
You should write an assertion on the output that checks
exactly what it should be equal to.

Trivia: Specifications of this form are called "functional correctness"
specifications because they specify exactly what the function should do.
They are also known as "strongest postcondition" specifications.
We will learn more about these in the program verification
part of the course.
"""

# Preconditions


# Example with assume in hypothesis

# Example with a loop invariant

def repeated_square(x, n):
    # TODO: implement
    pass
