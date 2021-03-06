import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

a = int(input("render level = "))
b = int(input("animation level = "))
tmax = float(input("tmax = "))
xmax = float(input("xmax = "))
ymax = float(input("ymax = "))

X = np.linspace(0, xmax, a)
Y = np.linspace(0, ymax, a)

x, y = np.meshgrid(X, Y)

t = np.linspace(0, tmax, int(b*tmax))

def f(x, y, t):
    s = #your function
    return(s)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
plt.ion()

i = 0

while i<(a*tmax):
    plt.clf()
    ax = fig.add_subplot(111, projection = '3d')
    plt.title('Time = {} secondes'.format(t[i]))
    ax.plot_surface(x, y, f(x, y, t[i]), cmap = cm.plasma, linewidth=0, antialiased=True)
    ax.axes.set_xlim3d(left=0, right=xmax)
    ax.axes.set_ylim3d(bottom=0, top=ymax)
    ax.axes.set_zlim3d(bottom=-1.2, top=1.2)
    plt.pause(1/(a*tmax))
    i = i + 1
