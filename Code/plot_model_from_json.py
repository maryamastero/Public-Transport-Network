# -*- coding: utf-8 -*-
import json

import matplotlib.pyplot as plt

Number_of_steps = 200
Number_of_routes = 20
points = []
with open(f'../Results/model_lspace/model_{Number_of_steps}_{Number_of_routes}.json', 'r') as f:
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
plt.title('SAW of length ' + str(Number_of_steps) +' with \n '+str(Number_of_routes) +' routes', fontsize=14, fontweight='bold')

plt.show()