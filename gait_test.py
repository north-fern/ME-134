
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

num_steps = 10
r = 2
y = np.linspace(-2, 2, num_steps)
x = np.linspace(r, r, num_steps)
def gait_trajectory(y, height):
    z = np.zeros(num_steps)
    for i in range(len(y)):
        z[i] = math.sqrt((height)**2 - (y[i])**2)
    return z


fig = plt.figure()
ax = fig.gca(projection='3d')
z = gait_trajectory(y, 2)

print(x)
print(y)
print(z)
ax.plot(x, y, z)
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')

ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax.set_yticks([0, 1, 2, 3])
ax.set_zticks([ 0, 1, 2, 3])
plt.show()
