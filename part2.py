"""
Part 2: Case study
"""

from hypothesis import given
from hypothesis import strategies as st
import pytest

"""
Below we have a basic Python class that is used to store user information.
The user is defined by a name, an age, and a list of friends.

In Python, the __init__ method is called when a new object is created.
For example, to create a new user, we would write:
    user = User("Alice", 25, ["Bob", "Charlie"])

The other two methods are for convenience:
- The __repr__ method is used to print the object in a readable way,
    which often helps with debugging.
- The __eq__ method is used to compare two objects for equality.
"""

class User:
    def __init__(self, name, age, friends=None):
        self.name = name
        self.age = age
        if friends is None:
            friends = []
        self.friends = friends

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name \
            and self.age == other.age \
            and self.friends == other.friends

"""
1. Write a complete specification for the __init__ class method using Hypothesis.
Your specification should check that every field is correctly initialized.

Hint: st.one_of may be useful:
https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.one_of

Remember to remove @pytest.mark.skip(reason="Unimplemented")
to enable the test when you are done.
"""

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
def test_user_init(name, age, friends):
    raise NotImplementedError

"""
2. The next few exercises are about serialization and deserialization.

After we have our User class, we are told that we need to serialize
users to a CSV file.
Ignore the friends field for now, and assume that the CSV file will have
only two fields:
    name,age

Write a to_csv function and from_csv function based on this idea.
The to_csv function should take a User object and return a string.
The from_csv function should take a string and return a User object.
"""

def to_csv(user):
    # TODO
    raise NotImplementedError

def from_csv(csv):
    # TODO
    raise NotImplementedError

"""
3. (Complete exerise 2 before doing this!)

Now that you have written both functions, unskip (enable) the following tests.
Which of them passes for your implementation?

===== ANSWER Q3 BELOW =====

===== END OF Q3 ANSWER =====

If they don't pass: add a @pytest.mark.xfail annotation to the test.

**Important:**
Don't modify the implementation yet, and don't modify either test.
"""

@pytest.mark.skip(reason="See exercise 3")
@given(st.text(), st.integers())
def test_serialize_deserialize(name, age):
    user = User(name, age)
    assert from_csv(to_csv(user)) == user

@pytest.mark.skip(reason="See exercise 3")
@given(st.text(), st.integers())
def test_deserialize_serialize(name, age):
    csv = f"{name},{age}"
    assert to_csv(from_csv(csv)) == csv

"""
If both tests passed (this is unlikely), you may skip 4-7.

If either test failed:

4. What went wrong?

===== ANSWER Q4 BELOW =====

===== END OF Q4 ANSWER =====

5. There are at least 4 ways we could modify our code:
- By changing the serialization function;
- By changing the deserialization function;
- By changing the precondition (for example, to require that st.text()
  does not contain commas);
- By changing the specification.

Which of the above solutions would succeed to get the tests passing?

===== ANSWER Q5 BELOW =====

===== END OF Q5 ANSWER =====

6. Do you have a preferred solution?
Imagine this were a real application and real users were entering their names in
production. Would one of the above solutions be more secure than the others?

===== ANSWER Q6 BELOW =====

===== END OF Q6 ANSWER =====

7. Pick one way and implement it below.
"""

# TODO: Implement the fix here

"""
8. The remaining exercises will explore some interesting limitations of Hypothesis.

The following function was added to print out information about the user.
Try writing a Hypothesis test for this function. Is what you wrote useful?

===== ANSWER Q8 BELOW =====

===== END OF Q8 ANSWER =====
"""

def print_user(self):
    friends_str = " ".join(self.friends)
    print(f"INFO: User {self.name} is {self.age} years old and has friends: {friends_str}")

@pytest.mark.skip(reason="Unimplemented")
@given(
    st.text(),
    st.integers(),
    st.lists(st.text()),
)
def test_print_user(name, age, friends):
    raise NotImplementedError

"""
9. Below we have a function to check whether a user is a friend of another user.
However, it was implemented incorrectly.

Uncomment the test. It runs for a long time before failing -- why?

===== ANSWER Q9 BELOW =====

===== END OF Q9 ANSWER =====

Fix the has_friend implementation so that the test passes.
"""

def has_friend(self, other):
    if has_friend(other, self):
        return True
    return other.name in self.friends

@pytest.mark.skip(reason="Unskip for exercise 9")
@pytest.mark.xfail
@given(
    st.text(),
    st.integers(),
    st.lists(st.text()),
    st.text(),
    st.integers(),
    st.lists(st.text()),
)
def test_has_friend(name1, age1, friends1, name2, age2, friends2):
    user1 = User(name1, age1, friends1)
    user2 = User(name2, age2, friends2)
    assert has_friend(user1, user2) == has_friend(user2, user1)

"""
10. Is there any "assertion" that you could write to directly test for this behavior?
(That is, that fails quickly / in a reasonable amount of time?)

Why or why not?

===== ANSWER Q10 BELOW =====

===== END OF Q10 ANSWER =====

"""

"""
11. Here is another example similar to the above.
Here we have a from_server function that contacts a server
and waits to get a user. For the purposes of this exercise,
let's assume that the server is not available.

What happens when you uncomment the test?

===== ANSWER Q11 BELOW =====

===== END OF Q11 ANSWER =====

**Important:** Make sure you mark the test as skipped again afterwards, so that your pytest still runs!
"""

def server_response():
    # Return the user data if the server is available,
    # otherwise return None.
    # This is a placeholder -- we assume the server is not available
    # for this exercise.
    return None

def user_from_server():
    # Wait for the server to respond
    response = None
    while response is None:
        response = server_response()

    # Parse the response
    name, age, friends = response.split(",")
    return User(name, int(age), friends.split(","))

@pytest.mark.skip(reason="Unskip for exercise 11")
# Make sure you mark it skipped again afterwards!
def test_user_from_server():
    user = user_from_server()
    assert user is not None

"""
12. Is there any "assertion" that you could write to reasonably test for this behavior?
(Even given an arbitrary amount of time?)
Why or why not?

===== ANSWER Q12 BELOW =====

===== END OF Q12 ANSWER =====
"""

"""
13. Below we have a function for adding a friend to a user.
However, it was again implemented incorrectly.
The function overwrites any existing friends with the new friend.

Unskip the test. What happens?
Explain what might have gone wrong here.

===== ANSWER Q13 BELOW =====

===== END OF Q13 ANSWER =====
"""

def add_friend(self, other):
    self.friends = [other.name]

@pytest.mark.skip(reason="Unskip for exercise 13")
@given(
    st.text(),
    st.integers(),
    st.text(),
    st.integers(),
)
def test_add_friend(name1, age1, name2, age2):
    user1 = User(name1, age1)
    user2 = User(name2, age2)
    add_friend(user1, user2)
    assert user1.friends == [user2.name]

"""
14. Using the above, what can we conclude more generally
about specifications?

===== ANSWER Q14 BELOW =====

===== END OF Q14 ANSWER =====

"""

"""
15. Mutability can pose a serious problem when writing specifications.

Mutability is the ability of an object or function to change its state after
it has been created.

Let's add one last function to the User class, which applies a function to the age.
The function below (given to you) takes a function f as argument, and
returns a new User object.
Write a specification for the new function using Hypothesis.
Your specification should:
- create a user from name and age
- apply the function f to the age
- check that the new user's age matches the result of applying f to the original age.

Remember that you can use Hypothesis to generate functions.
We did an example of this in the lecture1.py file.
For this part, for the function argument, please use this:
    st.functions(like=lambda x: x,returns=st.integers())

The test should fail.
"""

def update_age_with(self, f):
    return User(self.name, f(self.age), self.friends)

@pytest.mark.skip(reason="Unimplemented")
@pytest.mark.xfail
# @given(..)
def test_update_age_with_1(name, age, f):
    raise NotImplementedError

"""
16. A function is called "pure" if it does not modify its state when called,
and it does not have any other side effects (like printing to the console).
That is, the outcome of calling the function is
solely defined by its input-output behavior.

Write a version of test_update_age_with that passes
by adding pure=True to the st.functions strategy.
The test should pass.
"""

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
def test_update_age_with_2(name, age, f):
    raise NotImplementedError

"""
17. Bonus question (Extra credit):

The problem with the specification in exercise 16 is that it assumes f is pure,
but in the real world, this is not very realistic.
Many functions do have state, and f might be mutable or even mutate the user
object itself.

Is there any way to test that the function behaves correctly without assuming f is pure?

Answer in words only. Hint: Python is a highly dynamic language!

===== ANSWER Q17 BELOW =====

===== END OF Q17 ANSWER =====
"""
