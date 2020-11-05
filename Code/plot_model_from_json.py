# -*- coding: utf-8 -*-
import json

import matplotlib.pyplot as plt


points = []
with open('../Results/model_50.json', 'r') as f:
     points.append(json.load(f))
     
plt.figure(figsize = (8, 8))    
xs = []
ys = []
for route in points[0]:
        x_r,y_r = zip(*route)
        xs.append(x_r)
        ys.append(y_r)

for x, y in zip(xs,ys):    
    plt.plot(x, y)

plt.axis('equal')
plt.title('hi you')

plt.show()