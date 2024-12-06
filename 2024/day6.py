import numpy as np
import pandas as pd
import copy
import sys

sys.setrecursionlimit(17900)

file = open("day6.txt", "r")

puzzle = []
for l in file:
    if l[-1] == "\n":
        puzzle.append(list(l[:-1]))
    else:
        puzzle.append(list(l))

puzzle = np.array(puzzle)

inp = copy.deepcopy(puzzle)

x, y = np.where(inp == "^")
x, y = x[0], y[0]

def avance(x, y, max_iter = 16900):
    if max_iter < 0:
        return 1
    if 0 <= x < len(inp) and 0 <= y < len(inp[0]):
        if inp[x, y] == "v":
            if x + 1 >= len(inp):
                inp[x, y] = "X"
                return 0
            elif inp[x + 1, y] == "#":
                inp[x, y] = "<"
                return avance(x, y, max_iter - 1)
            else:
                inp[x, y] = "X"
                inp[x + 1, y] = "v"
                return avance(x + 1, y, max_iter - 1)
        elif inp[x, y] == "^":
            if x - 1 < 0:
                inp[x, y] = "X"
                return 0
            elif inp[x - 1, y] == "#":
                inp[x, y] = ">"
                return avance(x, y, max_iter - 1)
            else:
                inp[x, y] = "X"
                inp[x - 1, y] = "^"
                return avance(x - 1, y, max_iter - 1)
        elif inp[x, y] == ">":
            if y + 1 >= len(inp):
                inp[x, y] = "X"
                return 0
            elif inp[x, y + 1] == "#":
                inp[x, y] = "v"
                return avance(x, y, max_iter - 1)
            else:
                inp[x, y] = "X"
                inp[x, y + 1] = ">"
                return avance(x, y + 1, max_iter - 1)
        elif inp[x, y] == "<":
            if y - 1 < 0:
                inp[x, y] = "X"
                return 0
            elif inp[x, y - 1] == "#":
                inp[x, y] = "^"
                return avance(x, y, max_iter - 1)
            else:
                inp[x, y] = "X"
                inp[x, y - 1] = "<"
                return avance(x, y - 1, max_iter - 1)
        else:
            return 0
    else:
        return 0

avance(x, y)

print(np.unique(inp, return_counts = True)[1][2])

r = 0

for pos1 in range(len(puzzle)):
    for pos2 in range(len(puzzle[0])):
        inp = copy.deepcopy(puzzle)

        if inp[pos1, pos2] == "^":
            continue
        
        inp[pos1, pos2] = "#"

        x, y = np.where(inp == "^")
        x, y = x[0], y[0]
        
        r += avance(x, y)

print(r)
