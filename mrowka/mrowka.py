import matplotlib.pyplot as plt
import numpy as np
from random import choice, randrange as rr

dirs = {"N": [0, 1], "S": [0, -1], "W": [-1, 0], "E": [1, 0]}

L = {"N": "W", "W": "S", "S": "E", "E": "N"} # left
R = {"N": "E", "E": "S", "S": "W", "W": "N"} # right
N = {"N": "N", "W": "W", "S": "S", "E": "E"} # none
B = {"N": "S", "W": "E", "S": "N", "E": "W"} # back

colormaps = plt.colormaps()

for mainloop in range(1000):

    xsize, ysize = 200 + rr(300), 200+rr(300)
    steps, colours = 1000000 + rr(4000000), 20+rr(65515)
    x, y = xsize//2, ysize//2
    board = np.zeros(shape=(xsize, ysize), dtype=int)

    turns = []
    tt = ""
    trnum = 2+rr(20)
    for i in range(trnum):
        t = choice(("L", "R", "N", "B"))
        tt += t
        turns.append({"L": L, "R": R, "N": N, "B": B}[t])

    dir = "N"
    for X in range(steps):
        dir = turns[(board[x, y]) % len(turns)][dir]
        board[x, y] = (board[x, y] + 1) % colours
        dx, dy = dirs[dir]
        x, y = (x + dx) % xsize, (y + dy) % ysize
    plt.imshow(board, cmap=choice(colormaps))
    plt.xticks([])
    plt.yticks([])
    xlab = "{}x{}|{}|C:{}|S:{}".format(xsize, ysize, tt, colours, steps)
    plt.xlabel(xlab)
    filename = "langton-{}-{}-{}-{}-{}.png".format(
        xsize, ysize, tt, colours, steps)
    plt.savefig(filename)
    print(".", end="")
print()