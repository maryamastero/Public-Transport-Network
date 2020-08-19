import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd
import seaborn as sns

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities


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
       
    # =============================================================================
    #     network_measures = []
    #     with open(f'../Results/lspace/{city}.json', 'r') as f:
    #         s = f.read()
    #         s = s.replace('\'','\"')
    #         data = json.loads(s)          
    #         network_measures.append(data) 
    # 
    # =============================================================================
            
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
        
    # =============================================================================
    #     number_of_nodes_real = network_measures[0]['Number of nodes']
    #     ave_clustering_real = float(network_measures[0]['Average clustering coefficient'])
    #     ave_shortest_path_real = float(network_measures[0]['Average shortest path'])
    #     assortativity_real = float(network_measures[0]['Assortativity'])
    #     ave_degree_real = float(network_measures[0]['Average degree'])
    #     number_of_edges_real =network_measures[0]['Number of edges']
    #     
    # =============================================================================
        mean_number_of_nodes_random.append(np.mean(number_of_nodes_random))
        mean_ave_clustering_random.append(np.mean(ave_clustering_random))
        mean_ave_shortest_path_random.append(float("%.2f"% np.mean(ave_shortest_path_random)))
        mean_assortativity_random.append(float("%.2f"% np.mean(assortativity_random)))
        mean_ave_degree_random.append(float("%.2f"% np.mean(ave_degree_random)))
        mean_number_of_edges_random.append(np.mean(number_of_edges_random))
        
    
# =============================================================================
#     sns.kdeplot(number_of_edges_random, label = 'Random edges distribution')
#     plt.axvline(number_of_edges_real, 0, color = 'r',label = 'Real value of number of edges',  linestyle = '--',linewidth=4)
#     plt.legend()
#     plt.title('edges dist')
#     plt.show()
#     sns.kdeplot(assortativity_random, label = 'RAndom ass')
#     plt.axvline(assortativity_real, 0, color = 'r',label = 'Real value of ass',  marker = '*',linewidth=4)
#     plt.legend()
#     plt.title('Assortativity')
#     plt.show()
#     sns.kdeplot(ave_clustering_random, label = 've_clustering_random')
#     plt.axvline(ave_clustering_real, 0, color = 'r',label = 'Real value of ass',  marker = '*',linewidth=4)
#     plt.legend()
#     plt.title('Average clustering coefficient')
#     plt.show()
#     sns.kdeplot(ave_shortest_path_random, label = 've_shortest_path_random')
#     plt.axvline(ave_shortest_path_real, 0, color = 'r',label = 'Real value of ass',  marker = '*',linewidth=4)
#     plt.legend()
#     plt.title('Average shortest path')
#     plt.show()
#     sns.kdeplot(ave_degree_random, label = 'ave_degree_random')
#     plt.axvline(ave_degree_real, 0, color = 'r',label = 'Real value of ass',  marker = '*',linewidth=4)
#     plt.legend()
#     plt.title('Average degree')
#     plt.show()
# =============================================================================
    
# =============================================================================
       
#     plot_ccdfs(uniq_degs,normalized_deg_dists, markers,labels,space)
#     plot_degree_clustering(degree_dist_cities,cities_clustering,markers, labels,space)
#         
#     plot_node_network_measures(number_of_nodes,ave_shortest_path,markers, labels, colors, space, 'ave_shortest_path' ,style = 'semilog')
#     plot_node_network_measures(number_of_nodes,ave_shortest_path,markers, labels,  colors,space, 'ave_shortest_path')
#     
#     
#     plot_node_network_measures(number_of_nodes,ave_clustering,markers, labels, colors, space, 'ave_clustering', style = 'semilog')
#     plot_node_network_measures(number_of_nodes,ave_clustering,markers, labels,  colors,space, 'ave_clustering')
#     
#     plot_node_network_measures(number_of_nodes,cities_assortativity ,markers, labels, colors,space,'assortativity', style = 'semilog')
#     plot_node_network_measures(number_of_nodes,cities_assortativity ,markers, labels, colors,space, 'assortativity')
#     
#     plot_node_network_measures(number_of_nodes,ave_degree  ,markers, labels, colors,space,'ave_degree', style = 'semilog')
#     plot_node_network_measures(number_of_nodes,ave_degree  ,markers, labels, colors,space, 'ave_degree')
#         
#     all_space_plot_ccdfs(all_space_uniq_degs,all_space_normalized_deg_dists,markers, labels, spaces,colors)     
#     measure_names = ['ave_clustering', 'ave_shortest_path', 'assortativity', 'ave_degree']
#     measures = [all_space_ave_clustering,all_space_ave_shortest_path, all_space_cities_assortativity, all_space_ave_degree ]
#     for measure , measure_name in zip(measures,measure_names):
#         all_space_plot_node_network_measures(number_of_nodes,measure,markers, labels, colors,spaces, measure_name)
#         
# 
# =============================================================================
