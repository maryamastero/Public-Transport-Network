import random
import matplotlib.pyplot as plt
import networkx as nx
import random
import json


n = 300

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


def get_highest_degree_neighbor(degree_dict,not_visited_directions,all_directions):
  updated_degree_dict0 = {k:v for k,v in degree_dict.items() if k in all_directions}
  updated_degree_dict = {k:v for k,v in updated_degree_dict0.items() if k in not_visited_directions}
  probaility_dic = {k:v/sum(updated_degree_dict.values()) for k,v in updated_degree_dict.items()}
  point_pr = probaility_dic.values()
  points = probaility_dic.keys()
  next_point = random.choices( list(points), weights= list(point_pr), k=1)
                              
  return next_point[0]


def saw_prefrentional(Number_of_steps , Number_of_routes):
    Nsteps = range(Number_of_steps)
    all_visited_points = []
    
    for route in range(Number_of_routes):
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
                current_position = get_highest_degree_neighbor(degree_dict,not_visited_directions,all_directions)
              else:
                  flag = 1
                  break
                  
        all_visited_points.append(visited_points)
       
        
    temp_file = open(f"../Results/model_{Number_of_steps}_{Number_of_routes}.json", "w")
    json.dump(all_visited_points, temp_file)
    temp_file.close()
    
    return all_visited_points


if __name__ == "__main__":
    
    Number_of_steps = 300
    Number_of_routes = 27
    saw_prefrentional(Number_of_steps , Number_of_routes)