import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def​ traj(start,end,const):
    num_steps = 10
    y = np.linspace(start, end, num_steps)
    x = np.linsapce(const,const,num_steps)
    def gait_trajectory(y, height):
        z = np.zeros(num_steps)
        for i in range(len(y)):
            z[i] = math.sqrt((height)**2 - (y[i])**2)
        return z
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    z = gait_trajectory(y, 2)


def gait(set):
    if set=='ace':
        path_a=traj(-30,25,3)
        path_c=traj(5,-5,3)
        path_e=traj(25,15,3)
        path_b= #move theta1
        path_d =  # move theta1
        path_f =  # move theta1
    elif set=='bdf':
        path_a= # move theta1
        path_c= # move theta1
        path_e= # move theta1
        path_b= traj(
        path_d =  # move theta1
        path_f =  # move theta1

print(x)
print(y)
print(z)
ax.plot(x, y, z)
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')
plt.show()
