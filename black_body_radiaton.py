from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import *

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

h = 6.62607015*(10**(-34))
k = 1.380649*(10**(-23))
c = 299978548

def f(x,y):
    a = ((2*h*(y**3))/(c**2)) * (1/(np.exp((h*y)/(k*x))-1))
    return(a)

T = np.linspace(1, 10000, 10000)
lambda_ = np.linspace(10**(-6), 4*10**(-6), 10000)

def F(lambda_):
    s = 1/lambda_
    return s

F = F(lambda_)
F = np.linspace(10**14, 2*(10**15), 10000)
x, y = np.meshgrid(T, F)
Z = f(x,y)

ax.plot_surface(x, y, Z, cmap = cm.plasma, linewidth=0, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.legend()

plt.show()

t = int(input("temperature (K) = "))

plt.plot(F, f(t, F), color = 'red')
plt.show()
