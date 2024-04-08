"""
Part 4 (Extra Credit)

Rock paper scissors game

This part of the assignment is extra credit.
It asks you to implement a rock paper scissors game where
you can play against a finite-state-machine opponent.

=== Game explanation ===

- The basic game of rock paper scissors (RPS) works by having two
players. Each player picks one of rock, paper, or scissors
simultaneously, and the two choices are revealed. The winner is
determined by the rules that Rock beats Scissors, Scissors beats Paper,
and Paper beats Rock.

The game is repeated some given number of rounds (e.g., 10)
and the winner overall is the one who won the most rounds.

Finite state machines playing rock paper scissors are a fun way
to play against a computer. The computer has:
- A state, which is a number between 0 and (num_states - 1)
- A transition function, which is a map from the current state and the opponent's move to the next state.
  This can be stored as a list of lists, e.g.
    [[0, 1, 3], [1, 2, 0], [2, 0, 1], [1, 1, 1]].
  The index transition[i][j] is the next state if the current state is i and the opponent's move is j.
- A move function, which is a map from the current state to the computer's move. This can be stored as a list, e.g.
    [ROCK, PAPER, SCISSORS, PAPER]
    The index move[i] is the computer's move if the current state is i.
- An initial state. This is a number between 0 and (num_states - 1).

When the computer plays a round, it:
- Looks up its move based on its current state
- Plays that move
- Checks the opponent's move -- the player's move -- and updates its state based
  on the transition function to a new state (between 0 and num_states - 1).

=== Part 1: Game Logic ===

- Begin by defining some constants for
ROCK, PAPER, SCISSORS,
WIN, TIE, and LOSS.
(like this: ROCK = 0, PAPER = 1, etc.)
Write a function that determines the winner in a single round of the game:

    get_result(move1, move2)
    # returns: WIN, TIE, or LOSS

Use Hypothesis to test that the output is always one of WIN, TIE, LOSS.
Use Hypothesis to test at least one other property.

- Next, write a function that plays a single round of the game,
and updates an abstract game state.
The function should following signature:

    play_round(move1, move2, state, update)

Here, state is some state, and
update is a function that takes in (state, move1, move2, result) and returns the next state.

play_round should return two things:
- The result of the round
- The next state (result of update_function).

(The reason for writing this function in a generic way, with the
update_function argument, is that it could be useful for the next part.)

Use Hypothesis to test that the update_function is being called correctly.
This is a bit tricky --
You should use a function argument for update_function
and a st.functions generator to instantiate it.
You can assume that the state is an integer.
Use pure=True to make sure that the update_function is deterministic.

=== Part 2: Finite State Machines ===

Define a class for your finite state machine. It should look, for example,
something like this:
class FiniteStateMachine:
    def __init__(self, num_states, transitions, moves, initial_state):
        self.num_states = num_states
        self.transitions = transitions
        self.moves = moves
        self.state = initial_state

We will also need a way to generate state machines to test with Hypothesis.

We can do this by writing a function that generates a random finite state machine with N states.
You will need to add
import random
to the top of your file.
Then fill in this function:

def random_state_machine(N):
    # fill in
    # return FiniteStateMachine

To test that your funciton is working correctly, write a Hypothesis test.
What properties should your test check about the output state machine
(for example, to ensure that all the transitions are within bounds)?

=== Part 3: Add Methods ===

Add methods to the state machine.
Your state machine should support the following methods:

    - get_move(self) -- get the current move

    - update(self, player_move) -- update the state based on the player's move.
    You should use the transitions to determine the next state.

    - play_round(self) -- play a round of the game, with user input.

    - play_game(self, num_rounds) -- play num_rounds rounds of the game.
      This should return a list of results (WIN, TIE, LOSS).

    - tally_results(self) -- Total up the number of wins, ties, and losses.

Use Hypothesis to test that the state machine is playing correctly.
Note that you will be unable to test the methods that use user input.
Use the random_state_machine function to generate state machines to test with.
(This means that your Hypothesis input will just be an integer, N.)

You may add additional data fields and methods to the class if you wish.

=== Part 4: Wrong implementation ===

Write a "wrong" implementation for at least one of the functions
and methods we have tested so far.
Check the same wrong implementation against the same Hypothesis test you wrote
before. Does it catch the bug?

=== Part 5: Game Entrypoint ===

Add an entrypoint.
Your game entrypoint should allow the user to put in a number of rounds to play,
and a number of states for the state machine.
Then it should generate a random state machine and play the game,
and at the end, report on a winner.

=== Part 6: A more interesting property ===

Finally, here is a more interesting property you can test,
if you have time.
Suppose we keep playing the same move against the state machine.
What happens?
Does the state machine eventually loop?

You should be able to show that in at most 2 * N rounds (where N is the number of states),
the state machine will loop.
Note that it won't necessarily go back to the original state,
but it should repeat some state, one of the states from round 0 to N-1.

Write a Hypothesis test to check that this is true.
"""

if __name__ == '__main__':
    # Your entrypoint here
    pass
