import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

n = 10

def get_possible_directions(point):
    
    """Point is in form (x, y)"""
    directions = []

    if point[0]>= 0 and point[1] >= 0 and point[0]<= n and point[1] <= n:  
      
      if point[0]+1 <= n-1  :
          directions.append((point[0]+1, point[1])) # right
          
      if point[0]-1 >= 0:
          directions.append((point[0]-1, point[1]))  # left

      if point[1]+1 <= n-1:
          directions.append((point[0], point[1]+1))  # up

      if point[1]-1 >= 0:
          directions.append((point[0], point[1]-1))  # down
      
    
    return directions


def get_degree_dict(n):
  net =nx.grid_2d_graph(n, n)
  return dict(net.degree)

def get_starting_node(degree_dict):
   all_possilbe_starting_nodes = [k for k, v in degree_dict.items() if v == max(degree_dict.values())]
   if len(all_possilbe_starting_nodes) > 1:
      s = random.choice(all_possilbe_starting_nodes) 
   else:
       s = all_possilbe_starting_nodes[0]
   return s


def get_highest_degree_neighbor(degree_dict,visited_points,all_directions):
  highest_degree_neighbors = []
  updated_degree_dict = {k:v for k,v in degree_dict.items() if k in all_directions}

  for point in all_directions:
    if point not in visited_points:
      if updated_degree_dict[point] == max(updated_degree_dict.values()):
                highest_degree_neighbors.append(point)

  if len(highest_degree_neighbors) > 1:
     n = random.choice(highest_degree_neighbors)

  else:
    n =  highest_degree_neighbors[0]
  return n

N = 10
Nsteps = range(N)
# Need to be in a for for m routes
flag = 1
degree_dict = get_degree_dict(n)
while flag:
  flag = 0
  current_position = get_starting_node(degree_dict) 
  visited_points = []
  for i in Nsteps:
      visited_points.append(current_position)
      all_directions = get_possible_directions(current_position)
      not_visited_directions = [direction for direction in all_directions if direction not in visited_points]
      if not_visited_directions:
        current_position = get_highest_degree_neighbor(degree_dict,visited_points,not_visited_directions)
      else:
          flag = 1
          break
          
xp, yp = zip(*visited_points)


