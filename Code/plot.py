import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd

    
#%% Calculate normalized distribution
    
def ccdf(degree_dist):
    degree_dist = np.array(degree_dist)
    unique_degree_dist = np.unique(degree_dist) 
    ccdf = []
    normalizer=float(degree_dist.size) 

    for x in unique_degree_dist:
        ccdf.append((degree_dist[np.where(degree_dist >= x)].size)/normalizer)   

    return (unique_degree_dist.tolist(), ccdf)

#%%    
def plot_ccdfs(uniq_degs,datavecs,markers, labels, space):
    '''
    Plots in a single figure the complementary cumulative distributions
    
    '''
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for x_values, y_values, marker, label  in zip(uniq_degs,datavecs, markers, labels):    
        ax.semilogy(x_values, y_values, marker, label = label, linestyle="solid") 

    ax.set_xlabel('Degree' ) 
    ax.set_ylabel('1-CDF degree') 
    ax.legend(loc='best')
    ax.set_title(f'Degree distribution in {space}')
    plt.savefig(f"../Results/graph/Degree_distribution_semilogy_{space}.pdf", dpi=150)


    plt.show()

    return fig


#%%    
def all_space_plot_ccdfs(uniq_degs,datavecs,markers, labels, spaces,colors):
    '''
    Plots in a single figure the complementary cumulative distributions
    
    '''
    fig, ax = plt.subplots(1, 3, figsize=(25, 10))  
    for i, space in enumerate(spaces):
        for x_values, y_values, marker, label ,color in zip(uniq_degs[i],datavecs[i], markers, labels,colors):    
            ax[i].semilogy(x_values, y_values, marker, label = label, linestyle="solid", color = color) 

        ax[i].set_xlabel('Degree' ) 
        ax[i].set_ylabel('1-CDF degree') 
        ax[i].set_title(f'Complementary cumulative degree distribution in {space}')
   
    box = ax[2].get_position() 
    ax[2].set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(f"../Results/graph/Degree_distribution_semilog.pdf", dpi=150)


    plt.show()

    return fig
#%%
def plot_degree_clustering(degrees,clusteringvec, markers, labels,space):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for degree,clustering, marker, label  in zip(degrees,clusteringvec, markers, labels):    
        
        df = pd.DataFrame({"degree":degree,"clustering":clustering})
        df = df.sort_values(["degree"])
        mean_cluster = df.groupby("degree").mean()
        bins = np.array(mean_cluster.index.tolist())
        
        ax.plot(bins,mean_cluster,marker, label = label, linestyle= "solid")
        
    ax.set_xlabel('Degree') 
    ax.set_ylabel('Clustering Coefficient (ci)') 
    ax.set_title(f'Clustering coefficient in {space}')

    ax.legend(loc='best')
    plt.savefig(f"../Results/graph/Clustering_coefficient_degree_{space}.pdf", dpi=150)

    plt.show()
    return fig

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%%
def plot_node_network_measures(number_of_nodes,network_measures,markers, labels, colors,space, measure_name ):
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
        ax.set_title(f'Clustering Coefficient as Function of Number of nodes  in {space}')
    if measure_name == 'ave_shortest_path':
        ax.set_ylabel('Average Shortest Path') 
        ax.set_title(f'Average Shortest Path as Function of Number of nodes  in {space}')
    if measure_name =='assortativity': 
        ax.set_ylabel('Assortativity') 
        ax.set_title(f'Assortativity as Function of Number of nodes  in {space}')  
    if measure_name == 'ave_degree':
        ax.set_ylabel('Average degree') 
        ax.set_title(f'Average degree as Function of Number of nodes  in {space}')   
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(f"../Results/graph/{measure_name}_{space}.pdf", dpi=150)


    plt.show()


    return fig
#%%
def all_space_plot_node_network_measures(number_of_nodes,measure,markers, labels, colors,spaces, measure_name):
    '''
    Plots in a single figure network measures as function of node for each city 
    
    '''
    fig, ax = plt.subplots(1, 3, figsize=(25, 10))  
    for i, space in enumerate(spaces):
        for x_values, y_values, marker, label ,color  in zip(number_of_nodes,measure[i], markers, labels,colors):    
            ax[i].plot(x_values, y_values, marker, label = label, markersize=12, color = color) 
        ax[i].set_xlabel('Number Of Nodes' )         
        
        if measure_name == 'ave_clustering':
            ax[i].set_ylabel('Average Clustering Coefficient') 
            ax[i].set_title(f'Clustering Coefficient as Function of \n Number of nodes  in {space}')
        if measure_name == 'ave_shortest_path':
            ax[i].set_ylabel('Average Shortest Path') 
            ax[i].set_title(f'Average Shortest Path as Function of \n Number of nodes  in {space}')
        if measure_name =='assortativity': 
            ax[i].set_ylabel('Assortativity') 
            ax[i].set_title(f'Assortativity as Function of \n Number of nodes  in {space}')  
        if measure_name == 'ave_degree':
            ax[i].set_ylabel('Average degree') 
            ax[i].set_title(f'Average degree as Function of \n Number of nodes  in {space}')   
    box = ax[2].get_position() 
    ax[2].set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(f"../Results/graph/all_space_{measure_name}.pdf", dpi=150)
    
    plt.show()


    return fig


#%%
if __name__ == '__main__':
    labels = get_list_cities_names()
    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    
    spaces = ['lspace','pspace','cspace']
    network_measures = []
    for space in spaces:   
        with open(f'../Results/All_cities/{space}.json', 'r') as f:
            network_measures.append(json.load(f))
            
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    
    all_space_uniq_degs = []
    all_space_normalized_deg_dists = []
    
    
    all_space_ave_clustering = []
    all_space_ave_shortest_path = []
    all_space_cities_assortativity = []
    all_space_ave_degree = []
    for i, space in enumerate(spaces):
        number_of_nodes = []
        ave_clustering = []
        ave_shortest_path = []
        degree_dist_cities = []
        uniq_degs = []
        normalized_deg_dists = []
        cities_clustering = []
        cities_assortativity = []
        ave_degree = []
        number_of_edges = []
        for j in range(len(network_measures[i])):
            number_of_nodes.append(int(network_measures[i][j]['Number of nodes'])) 
            number_of_edges.append(int(network_measures[i][j]['Number of edges']))
            ave_clustering.append(float(network_measures[i][j]['Average clustering coefficient']))
            degree_dist_cities.append(network_measures[i][j]['Degree distribution'])
            uniq_deg, normalized_deg_dist = ccdf(network_measures[i][j]['Degree distribution'])
            uniq_degs.append(uniq_deg)
            normalized_deg_dists.append(normalized_deg_dist)
            cities_clustering.append(network_measures[i][j]['Clustering coeficient'])
            ave_shortest_path.append(float(network_measures[i][j]['Average shortest path']))
            ave_degree.append(float(network_measures[i][j]['Average degree']))
            cities_assortativity.append(float(network_measures[i][j]['Assortativity']))
        
        all_space_uniq_degs.append(uniq_degs )
        all_space_normalized_deg_dists.append(normalized_deg_dists )
        all_space_ave_clustering.append(ave_clustering )
        all_space_ave_shortest_path.append(ave_shortest_path )
        all_space_cities_assortativity.append(cities_assortativity )
        all_space_ave_degree.append(ave_degree )
            
        plot_ccdfs(uniq_degs,normalized_deg_dists, markers,labels,space)
        plot_degree_clustering(degree_dist_cities,cities_clustering,markers, labels,space)
            
        plot_node_network_measures(number_of_nodes,ave_shortest_path,markers, labels,  colors,space, 'ave_shortest_path')       
        
        plot_node_network_measures(number_of_nodes,ave_clustering,markers, labels,  colors,space, 'ave_clustering')
        
        plot_node_network_measures(number_of_nodes,cities_assortativity ,markers, labels, colors,space, 'assortativity')
        
        plot_node_network_measures(number_of_nodes,ave_degree  ,markers, labels, colors,space, 'ave_degree')
        
    all_space_plot_ccdfs(all_space_uniq_degs,all_space_normalized_deg_dists,markers, labels, spaces,colors)     
    measure_names = ['ave_clustering', 'ave_shortest_path', 'assortativity', 'ave_degree']
    measures = [all_space_ave_clustering,all_space_ave_shortest_path, all_space_cities_assortativity, all_space_ave_degree ]
    for measure , measure_name in zip(measures,measure_names):
        all_space_plot_node_network_measures(number_of_nodes,measure,markers, labels, colors,spaces, measure_name)
        