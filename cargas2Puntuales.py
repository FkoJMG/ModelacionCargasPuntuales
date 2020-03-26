import numpy as np
import matplotlib.pyplot as plt
plt.axis("equal")

space = np.linspace(0,10,100)
print(space)
plt.plot(space)

N = 9

grid_min = -2
grid_max = 2

x, y = np.linspace(grid_min,10,grid_max)

X,Y = np.meshgrid(x,y)

K = 9E9
print(K)






plt.show() 