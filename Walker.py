import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import noise

map = lambda n, start1, stop1, start2, stop2: ((n-start1)/(stop1-start1))*(stop2-start2)+start2

class Walker():
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal", adjustable='datalim', anchor='C'))
        self.fig.set_dpi(100)
        self.w = 320
        self.h = 180
        self.ax.set_xlim((-self.w,self.w))
        self.ax.set_ylim((-self.h,self.h))
        self.n1 = 0
        self.n2 = 10000
    
    def step(self, time):
        n1 = noise.pnoise1(self.n1)
        n2 = noise.pnoise1(self.n2)
        x = map(n1, 0, 1, 0, self.w)
        y = map(n2, 0, 1, 0, self.h)
        # print('x={} y={}'.format(x,y))

        self.point.center = (x, y)
        self.n1 += 0.01
        self.n2 += 0.01
        return [self.point]
    
    def display(self):
        self.point = plt.Circle((0, 0), 10, color='red', alpha=1)
        self.ax.add_patch(self.point)
        ani = animation.FuncAnimation(self.fig, self.step, frames=500, interval=40, blit=True)
        plt.show()

agent = Walker()
agent.display()