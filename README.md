# Homework 1: Writing Specifications with Hypothesis

## Due date: Friday, January 23 at 11:59pm

This homework is about writing specifications and testing with Hypothesis.
There are three parts to this homework.
Part 1 is a series of mini-exercises.
Part 2 is a more extended case study,
and Part 3 asks you to use Hypothesis to find a bug in a program.

## Getting started

To get started, make sure you have completed Homework 0.
in particular, you should have Python, Hypothesis, Pytest, and Z3 installed.
Then clone the repository with `git clone`,
and open and edit the files `part1.py`, `part2.py`, `part3.py`.

To run the code, you can use
```shell
pytest part1.py
pytest part2.py
pytest part3.py
```

We will submit the homework through Gradescope.

## Grading notes

- Don't change the function signatures unless you are asked to do so. This ensures that our gradings scripts will work correctly.

- Please do not use any external libraries. All problems are solvable without external libraries.

- Please do not modify the file names or the list of `test_` functions in parts 1, 2, and 3, as your results will be compared with the official rubric. If you want to add other tests, remember to comment them out after.

- If your code is correct, **there should be no pytest failures (shown in red)** -- instead, you should be using the annotation `pytest.mark.xfail` to mark tests that are expected to fail. These will show up in yellow.

- Make sure your answers to free response questions are between the `===== ANSWER HERE =====` and `===== END ANSWER =====` markers, and don't remove the markers.

- We won't be able to give credit to code that doesn't run, so please double check that your code runs before submitting. You should be able to run `pytest <yourfile>.py` and see a list of successful, skipped, and expected failing test cases. If you have some broken code, please remember to comment out the broken parts of each function (or use `@pytest.mark.skip` to skip the unit tests) to ensure you receive some partial credit.
