import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal", adjustable='datalim', anchor='C'))
width = 640
height = 360
ax.set_xlim((0, width))
ax.set_ylim((0, height))

point = plt.Circle((0, 0), 20, color='red', alpha=1)
ax.add_patch(point)
x = 100
y = 100
xspeed = 1.0
yspeed = 3.3

def update(t):
    global x, y, xspeed, yspeed
    x += xspeed
    y += yspeed

    if x > width or x < 0:
        xspeed *= -1
    
    if y > height or y < 0:
        yspeed *= -1

    point.center = (x, y)
    return [point]

ani = animation.FuncAnimation(fig, update, frames=500, interval=40, blit=True)
plt.show()