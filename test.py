import numpy as np
import noise

map = lambda n, start1, stop1, start2, stop2: ((n-start1)/(stop1-start1))*(stop2-start2)+start2

for i in np.linspace(0, 1, 20):
    ns = noise.pnoise1(i)
    x = map(ns, 0, 1, 0, 320)
    print ('x={}'.format(x))