import numpy as np
import matplotlib.pyplot as plt
from random import choice
from math import sin, cos, radians


nsteps = 100
nplotsx, nplotsy = 5, 10
fig, axs = plt.subplots(nplotsx, nplotsy)

for nx in range(nplotsx):
    for ny in range(nplotsy):
        angles = [radians(x) for x in [45, -45, 135, -135, 0]]
        x, y, dir = 0, 0, 0
        pathx = [x]
        pathy = [y]
        for step in range(nsteps):
            deltaDir = choice(angles)
            dir += deltaDir
            x, y = x + sin(dir), y + cos(dir)
            pathx.append(x)
            pathy.append(y)
        axs[nx, ny].plot(pathx, pathy, '-', linewidth=0.75)
        axs[nx, ny].axis('off')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()