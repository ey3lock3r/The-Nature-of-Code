import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal", adjustable='datalim', anchor='C'))
width = 640
height = 360
ax.set_xlim((0, width))
ax.set_ylim((0, height))

point = plt.Circle((0, 0), 20, color='red', alpha=1)
ax.add_patch(point)

class PVector():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def add(self, v):
        self.x += v.x
        self.y += v.y

location = PVector(100, 100)
velocity = PVector(2.5, 5)

def update(t):
    global location, velocity
    location.add(velocity)

    if location.x > width or location.x < 0:
        velocity.x *= -1
    
    if location.y > height or location.y < 0:
        velocity.y *= -1

    point.center = (location.x, location.y)
    return [point]



ani = animation.FuncAnimation(fig, update, frames=500, interval=40, blit=True)
plt.show()