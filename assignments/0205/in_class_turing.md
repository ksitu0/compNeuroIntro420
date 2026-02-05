A Turing machine has n "operational" states plus a Halt state, where n is a positive integer, and one of the n states is distinguished as the starting state.

The machine uses a single two-way infinite (or unbounded) tape.

The tape alphabet is {0, 1}, with 0 serving as the blank symbol.

The machine's transition function takes two inputs:
- the current non-Halt state,
- the symbol in the current tape cell,
- and produces three outputs:
    - a symbol to write over the symbol in the current tape cell (it may be the same symbol as the symbol overwritten),
    - a direction to move (left or right@";" that is, shift to the tape cell one place to the left or right of the current cell), and
    - a state to transition into (which may be the Halt state).

```
Input: Initial state S, state transitions T

currentState <- S
position <- 0

loop:
    currentValue <- read(position) (0, 1, or blank)

    newState, valueToWrite, direction (left, right, or none) <- T.lookup(currentState, currentValue)

    write(valueToWrite, position)
    currentState <- newState
    position <- move(position, direction)

    if currentState == Halt:
        exit

```