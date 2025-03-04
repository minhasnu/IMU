import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

x = np.linspace(0,1,50)
t = np.linspace(0,1,20)

X, T = np.meshgrid(x,t)
Y = np.sin(2*np.pi*(X+T))

block = amp.blocks.Line(X,Y)
anim = amp.Animation([block])

plt.show()
