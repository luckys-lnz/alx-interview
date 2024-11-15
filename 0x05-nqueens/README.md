```
# N-Queens Problem Solver

The N-Queens problem is a classic algorithmic problem in which the goal is to place `N` non-attacking queens on an `N×N` chessboard. This program solves the N-Queens problem using backtracking and prints all possible solutions.

## Usage

```bash
$ ./0-nqueens.py N
```

Where N is the size of the chessboard and the number of queens to place.

Input Validation

If the program is run with the wrong number of arguments, it will print:

```
Usage: nqueens N
```

and exit with status 1.

If N is not an integer, it will print:

```
N must be a number
```

