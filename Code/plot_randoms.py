import matplotlib.pyplot as plt
import json
import numpy as np


#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%%
def plot_node_network_measures(number_of_nodes,network_measures,markers, labels, colors,space, measure_name, style = None ):
    '''
    Plots in a single figure network measures as function of node for each city 
    
    '''
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        
    for x_values, y_values, marker, label ,color  in zip(number_of_nodes,network_measures, markers, labels,colors):    
        ax.plot(x_values, float(y_values), marker, label = label, markersize=12, color = color) 

    ax.set_xlabel('Number Of Nodes' ) 
    if measure_name == 'ave_clustering':
        ax.set_ylabel('Average Clustering Coefficient') 
        ax.set_title(f'Clustering Coefficient as Function of Number of nodes  using configuration model in {space} ')
    if measure_name == 'ave_shortest_path':
        ax.set_ylabel('Average Shortest Path') 
        ax.set_title(f'Average Shortest Path as Function of Number of nodes using configuration model in {space}')
    if measure_name =='assortativity': 
        ax.set_ylabel('Assortativity') 
        ax.set_title(f'Assortativity as Function of Number of nodes using configuration model in {space}')  
    if measure_name == 'ave_degree':
        ax.set_ylabel('Average degree') 
        ax.set_title(f'Average degree as Function of Number of nodes using configuration model in {space}')   
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(f"../Results/graph/Random_{measure_name}_{space}.pdf", dpi=150)

    
    plt.show()


    return fig

#%%
if __name__ == '__main__':
    labels = get_list_cities_names()
    cities = get_list_cities_names()
    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    
    space = 'lspace'
    mean_number_of_nodes_random = []
    mean_ave_clustering_random = []
    mean_ave_shortest_path_random =[]
    mean_assortativity_random = []
    mean_ave_degree_random =[]
    mean_number_of_edges_random = []
    for city in cities:
        network_measures_random = []
        with open(f'../Results/random/lspace/{city}.json', 'r') as f:
            s = f.read()
            s = s.replace('\'','\"')
            data = json.loads(s)          
            network_measures_random.append(data)    
      
        number_of_nodes_random = []
        ave_clustering_random = []
        ave_shortest_path_random = []
        assortativity_random = []
        ave_degree_random = []
        number_of_edges_random = []
        for j in range(len(network_measures_random[0])):
            number_of_nodes_random.append(int(network_measures_random[0][j]['Number of nodes'])) 
            number_of_edges_random.append(int(network_measures_random[0][j]['Number of edges']))
            ave_clustering_random.append(float(network_measures_random[0][j]['Average clustering coefficient']))
            ave_shortest_path_random.append(float(network_measures_random[0][j]['Average shortest path']))
            ave_degree_random.append(float(network_measures_random[0][j]['Average degree']))
            assortativity_random.append(float(network_measures_random[0][j]['Assortativity']))
  
        mean_number_of_nodes_random.append(np.mean(number_of_nodes_random))
        mean_ave_clustering_random.append(np.mean(ave_clustering_random))
        mean_ave_shortest_path_random.append(float("%.2f"% np.mean(ave_shortest_path_random)))
        mean_assortativity_random.append(float("%.2f"% np.mean(assortativity_random)))
        mean_ave_degree_random.append(float("%.2f"% np.mean(ave_degree_random)))
        mean_number_of_edges_random.append(np.mean(number_of_edges_random))
  


    plot_node_network_measures(mean_number_of_nodes_random,mean_ave_shortest_path_random,markers, labels,  colors,space, 'ave_shortest_path')
    
    plot_node_network_measures(mean_number_of_nodes_random,mean_ave_clustering_random,markers, labels,  colors,space, 'ave_clustering')
    
    plot_node_network_measures(mean_number_of_nodes_random,mean_assortativity_random,markers, labels, colors,space, 'assortativity')
    
    plot_node_network_measures(mean_number_of_nodes_random,mean_ave_degree_random,markers, labels, colors,space, 'ave_degree')
          
  