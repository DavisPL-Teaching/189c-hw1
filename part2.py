"""
Part 2: Bug-finding

This file contains an implementation of a rock-paper-scissors game
against a finite-state-machine opponent.
There are 5 bugs in the code, your goal is to find all of them.

=== Your task ===

For each bug, you should write a test using Hypothesis that
demonstrates the bug.
During testing, you can modify the code to fix the bugs.
However, at the bottom of the file, you should fill in the functions
test_bug1, test_bug2, test_bug3, test_bug4, and test_bug5.
Each function should fail on the original implementation and
pass on the fixed implementation.

=== Running the code ===

You can try out the game by running `python3 part2.py`.
You can run your tests by running `pytest part2.py`.

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
- A move function, which is a map from the current state to the computer's move.
- An initial state.

This file contains an implementation that lets you play rock paper scissors against finite state machines.

This file contains an implementation of rock-paper-scissors f


"""

ROCK = 0
PAPER = 1
SCISSORS = 2
MOVES = [ROCK, PAPER, SCISSORS]

WIN = 1
TIE = 0
LOSS = -1
RESULTS = [WIN, TIE, LOSS]

def play_round(move1, move2):
    if move1 == move2:
        return TIE
    if move1 == ROCK:
        return WIN if move2 == SCISSORS else LOSS
    if move1 == PAPER:
        return WIN if move2 == ROCK else LOSS
    if move1 == SCISSORS:
        return WIN if move2 == PAPER else LOSS



if __name__ == "__main__":
