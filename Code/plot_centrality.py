import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities


#%%
def plot_node_network_measures(number_of_nodes,network_measures,markers, labels, colors, measure_name ):
    '''
    Plots in a single figure network measures as function of node for each city 
    
    '''
    fig = plt.figure(figsize=(8,8)) 
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    
    for x_values, y_values, marker, label ,color  in zip(number_of_nodes,network_measures, markers, labels,colors):    
        ax.plot(x_values, float(y_values), marker, label = label, markersize=12, color = color) 

    ax.set_xlabel('Number Of Nodes' ) 
    
    if measure_name == 'ave_shortest_path':
        ax.set_ylabel('Average Shortest Path') 
        #ax.set_title(f'Average Shortest Path as Function of Number of nodes  in {space}')
    
    if measure_name == 'ave_degree':
        ax.set_ylabel('Average degree') 
       # ax.set_title(f'Average degree as Function of Number of nodes  in {space}')   
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True, linestyle='-.')
    ax.tick_params(labelcolor='k', labelsize='xx-large', width=5)
    plt.savefig(f"../Results/graph/pspace_{measure_name}.eps", format='eps')


    plt.show()


    return fig


#%%
if __name__ == '__main__':
    labels = get_list_cities_names()
    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    
    network_measures_pspace = []
    with open('../Results/All_cities/pspace.json', 'r') as f:
        network_measures_pspace.append(json.load(f))
            
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    
    degree_dist_pspace = []
    number_of_nodes_pspace = []
    ave_shortest_path_pspace = []
    ave_degree_pspace= []
    number_of_edges_pspace = []
    for j in range(len(network_measures_pspace)):
        number_of_nodes_pspace.append(int(network_measures_pspace[j]['Number of nodes'])) 
        number_of_edges_pspace.append(int(network_measures_pspace[j]['Number of edges']))
        ave_shortest_path_pspace.append(float(network_measures_pspace[j]['Average shortest path']))
        ave_degree_pspace.append(float(network_measures_pspace[j]['Average degree']))
        degree_dist_pspace.append(network_measures_pspace[j]['Degree distribution'])
    
    network_measures_lspace = []
    with open('../Results/lspace_centrality/network_centrality_measures_lspace.json', 'r') as f:
        network_measures_lspace.append(json.load(f))     
            
       
    