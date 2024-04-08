# Homework 1: Writing Specifications with Hypothesis

There are three parts to this homework.

- The first part is a series of small, mini-exercises. The exercises are designed to help you get used to the Hypothesis syntax, and are organized by concept (assertions, safety properties, preconditions, etc.).
<!-- TODO update -->

- The second part gives you a medium-size Python program and asks you to find all the bugs in it, using Hypothesis. There are 5 bugs for you to find. You should commit changes for all the 5 bugs, but you should also commit all tests you used to help find them.

- The third part is an open-ended task to implement your own program, and to write tests for it. In addition, you will be asked to write "wrong" versions of every function and show that they fail the unit tests.

## Getting started

To get started, [make sure you have completed Homework 0](https://github.com/DavisPL-Teaching/189c-hw0);
in particular, you should have Python, Hypothesis, and Pytest installed.
Then open and edit the files `part1.py`, `part2.py`, and `part3.py`.
To run the code, you can use
```
pytest part1.py
pytest part2.py
pytest part3.py
```

## Grading

**Important:**

- To make sure you get credit for your work, please make sure that your code runs! You should be able to run `pytest <yourfile>.py` and see a list of successful, failing, and skipped test cases.

- Just to reiterate: we won't be able to give credit if your code doesn't run! Unfortunately, we (the instructor and TA) only have limited time and it often takes a large investment to debug student submissions. If you have some broken code, please comment out the broken parts (or add `@pytest.mark.skip` to the unit tests) to ensure you receive some partial credit.

- Please do not modify the file names or the list of `test_` functions in parts 1 and 2, as your results will be compared with the official rubric. If you want to add other tests, remember to comment them out after. On part 3, you can have any number of tests.

- If your code is correct, **there should be no failures (shown in red)** -- instead, we will be using the annotation `pytest.mark.xfail` to mark tests that are expected to fail. These will show up in yellow.

## Rubric

Remember that your code will be graded both for correctness, and for code style!
From the syllabus: a rough rubric you can expect is 50 points for each of the following criteria:

- **Correctness:** Does you program work? That is, does it have the right output on each input and run within a reasonable amount of time? Does it do everything that's it's supposed to, are there bugs? Missing features? etc.

- **Code quality:** Does you program exhibit high code quality standards? That is, modular code, readable, not overly complex, well documents, commented, logically separated modules and functions, reasonably efficient, etc.
