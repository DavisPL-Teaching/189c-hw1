# Homework 1: Writing Specifications with Hypothesis

## Due date: Friday, April 19 at 11:59pm

There are three required parts to this homework.
Part 4 (`part4.py`) is extra credit.

- The first part is a series of small, mini-exercises.
The exercises are designed to help you get used to the Hypothesis syntax, as well as core concepts (specifications, correctness, preconditions).

- The second part is a slightly more real-world-ish case study,
using Python classes. It also discusses some of the limitations
of testing with Hypothesis.

- The third part gives you a small Python program with a bug, and asks you to find the bug, using Hypothesis.
You should commit a change for the bug, and also the test(s) you used to help find it.

## Getting started

To get started, [make sure you have completed Homework 0](https://github.com/DavisPL-Teaching/189c-hw0);
in particular, you should have Python, Hypothesis, and Pytest installed.

You will submit the homework through [GitHub Classroom](https://classroom.github.com/classrooms/165522706-ecs-189c-sq-2024).
GitHub classroom should have a user account set up for your name,
you will need to select that user account and associate it with your
GitHub handle.
If you have trouble creating an account, or with this step
in general, please let us know on Piazza.

To start the assignment, you will get your own fork of the repository to work with.
Clone the repository with `git clone`.

Then open and edit the files `part1.py`, `part2.py`, and `part3.py`.
To run the code, you can use
```shell
pytest part1.py
pytest part2.py
pytest part3.py
```

## Extra credit

There is also a fourth part, that is optional extra credit.
This is a more open-ended task to implement your own program, and to write tests for it, for a rock paper scissors game.
In addition, you will be asked to write a "wrong" version of one of the functions and show that it fails the Hypothesis tests.
```shell
pytest part4.py
```

## Grading

**Important:**

- We won't be able to grade code that doesn't run, so please make sure that your code runs before submitting. You should be able to run `pytest <yourfile>.py` and see a list of successful, failing, and skipped test cases.
(We will be running `pytest` on our end during grading.)

- If you have some broken code, please remember to comment out the broken parts (or use `@pytest.mark.skip` to the unit tests) to ensure you receive some partial credit.

- Please do not modify the file names or the list of `test_` functions in parts 1 and 2, as your results will be compared with the official rubric. If you want to add other tests, remember to comment them out after. On parts 3 and 4, you can have any number of tests.

- If your code is correct, **there should be no failures (shown in red)** -- instead, we will be using the annotation `pytest.mark.xfail` to mark tests that are expected to fail. These will show up in yellow.

## Rubric

Remember that your code will be graded both for correctness, and for code style.
From the syllabus: a rough rubric you can expect is 50 points for each of the following criteria:

- **Correctness:** Does you program work? That is, does it have the right output on each input and run within a reasonable amount of time? Does it do everything that's it's supposed to, are there bugs? Missing features? etc.

- **Code quality:** Does you program exhibit high code quality standards? That is, modular code, readable, not overly complex, well documents, commented, logically separated modules and functions, reasonably efficient, etc.

## Misc credits

Thanks to Benjamin Stanford for the problem considered in part 3.
