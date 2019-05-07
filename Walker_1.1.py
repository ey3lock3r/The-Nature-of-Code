import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import noise

map = lambda n, start1, stop1, start2, stop2: ((n-start1)/(stop1-start1))*(stop2-start2)+start2

class PVector():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def add(self, v):
        self.x += v.x
        self.y += v.y

class Walker():
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal", adjustable='datalim', anchor='C'))
        self.fig.set_dpi(100)
        self.w = 320
        self.h = 180
        self.ax.set_xlim((-self.w,self.w))
        self.ax.set_ylim((-self.h,self.h))
        self.n = PVector(0, 10000)
    
    def step(self, data):
        v_noice = PVector(noise.pnoise1(self.n.x), noise.pnoise1(self.n.y))
        location = PVector(map(v_noice.x, 0, 1, 0, self.w), map(v_noice.y, 0, 1, 0, self.h))

        self.point.center = (location.x, location.y)
        self.n.add(PVector(0.01, 0.01))
        return [self.point]
    
    def display(self):
        self.point = plt.Circle((None,None), 10, color='red', alpha=1)
        self.ax.add_patch(self.point)
        ani = animation.FuncAnimation(self.fig, self.step, frames=500, interval=40, blit=True)
        plt.show()

agent = Walker()
agent.display()