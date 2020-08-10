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
        ax.loglog(x_values, y_values, marker, label = label, linestyle="solid") 

    ax.set_xlabel('Degree' ) 
    ax.set_ylabel('1-CDF degree') 
    ax.legend(loc='best')
    ax.set_title('Degree distribution in p_space')
    plt.savefig(f"../Results/graph/Degree_distribution_{space}.pdf", dpi=150)


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
    ax.set_title('Clustering coefficient in p_space')

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
def plot_node_cluster(number_of_nodes,ave_clustering,markers, labels, colors,space, style = None):
    '''
    Plots in a single figure average clustering as function of node for each city 
    
    '''
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    if style == 'semilog':
        for x_values, y_values, marker, label,color  in zip(number_of_nodes,ave_clustering, markers, labels,colors):    
            ax.semilogx(x_values, float(y_values), marker, label = label, markersize=12,color =color) 
        
        ax.set_xlabel('Number Of Nodes' ) 
        ax.set_ylabel('Average Clustering Coefficient') 
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        ax.set_title(f'Clustering Coefficient as Function of Number of nodes  in {space}')
        plt.savefig(f"../Results/graph/semilog_node_cluster_{space}.pdf", dpi=150)
    else:
        for x_values, y_values, marker, label ,color  in zip(number_of_nodes,ave_clustering, markers, labels,colors):    
            ax.plot(x_values, float(y_values), marker, label = label, markersize=12, color = color) 
    
            ax.set_xlabel('Number Of Nodes' ) 
            ax.set_ylabel('Average Clustering Coefficient') 
            
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            ax.set_title(f'Clustering Coefficient as Function of Number of nodes  in {space}')
            plt.savefig(f"../Results/graph/node_cluster_{space}.pdf", dpi=150)
    
    
    plt.show()

# =============================================================================
#     for i, txt in enumerate(labels):
#              ax.annotate(txt, (number_of_nodes[i], ave_clustering[i]))
# =============================================================================
    return fig
#%%
def plot_node_ave_shortest_path(number_of_nodes,ave_shortest_path ,markers, labels,color, space, style = None):
    '''
    Plots in a single figure average clustering as function of node for each city 
    
    '''
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    if style == 'semilog':
        for x_values, y_values, marker, label,color  in zip(number_of_nodes,ave_shortest_path, markers, labels, colors):    
            ax.semilogx(x_values, float(y_values), marker, label = label, markersize=12 ,color = color) 
        
        ax.set_xlabel('Number Of Nodes' ) 
        ax.set_ylabel('Average Shortest Path') 
        ax.set_title(f'Average Shortest Path as Function of Number of nodes  in {space}')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig(f"../Results/graph/semilog_ave_shortest_path_{space}.pdf", dpi=150)
    else:
        for x_values, y_values, marker, label,color  in zip(number_of_nodes,ave_shortest_path, markers, labels, colors):    
            ax.plot(x_values, float(y_values), marker, label = label, markersize=12, color = color) 
    
            ax.set_xlabel('Number Of Nodes' ) 
            ax.set_ylabel('Average Shortest Path') 
            ax.set_title(f'Average Shortest Path as Function of Number of nodes in {space}')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.savefig(f"../Results/graph/ave_shortest_path_{space}.pdf", dpi=150)
    
    
    
    
    plt.show()


    return fig 
#%%
def plot_assortativity(number_of_nodes,assortativity ,markers, labels, colors,space, style = None):
    '''
    Plots in a single figure assortativity as function of node for each city 
    
    '''
    
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    if style == 'semilog':
        for x_values, y_values, marker, label, color  in zip(number_of_nodes,assortativity, markers, labels,colors):    
            ax.semilogx(x_values, float(y_values), marker, label = label, markersize=12, color = color) 
        
        ax.set_xlabel('Number Of Nodes' ) 
        ax.set_ylabel('Assortativity') 
        ax.set_title(f'Assortativity as Function of Number of nodes  in {space}')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig(f"../Results/graph/semilog_assortativity_{space}.pdf", dpi=150)
    else:
        for x_values, y_values, marker, label, color  in zip(number_of_nodes,assortativity, markers, labels ,colors):    
            ax.plot(x_values, float(y_values), marker, label = label, markersize=12, color = color) 
    
            ax.set_xlabel('Number Of Nodes' ) 
            ax.set_ylabel('Assortativity') 
            ax.set_title(f'Assortativity as Function of Number of nodes  in {space}')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.savefig(f"../Results/graph/assortativity_{space}.pdf", dpi=150)
   
    
    
    
    
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
    
    for i, space in enumerate(spaces):
        number_of_nodes = []
        ave_clustering = []
        ave_shortest_path = []
        degree_dist_cities = []
        uniq_degs = []
        normalized_deg_dists = []
        cities_clustering = []
        cities_assortativity = []
        efficiency = []
        for j in range(len(network_measures[i])):
            number_of_nodes.append(float(network_measures[i][j]['Number of nodes'])) 
            ave_clustering.append(float(network_measures[i][j]['Average clustering coefficient']))
            degree_dist_cities.append(network_measures[i][j]['Degree distribution'])
            uniq_deg, normalized_deg_dist = ccdf(network_measures[i][j]['Degree distribution'])
            uniq_degs.append(uniq_deg)
            normalized_deg_dists.append(normalized_deg_dist)
            cities_clustering.append(network_measures[i][j]['Clustering coeficient'])
            ave_shortest_path.append(float(network_measures[i][j]['Average shortest path']))
            efficiency.append(np.divide(1,float(network_measures[i][j]['Average shortest path'])))
            cities_assortativity.append(float(network_measures[i][j]['Assortativity']))
            
        plot_node_ave_shortest_path(number_of_nodes,ave_shortest_path,markers, labels, colors, space, style = 'semilog')
        plot_node_ave_shortest_path(number_of_nodes,ave_shortest_path,markers, labels,  colors,space)
        
        
        plot_node_cluster(number_of_nodes,ave_clustering,markers, labels, colors, space, style = 'semilog')
        plot_node_cluster(number_of_nodes,ave_clustering,markers, labels,  colors,space)
        
        plot_ccdfs(uniq_degs,normalized_deg_dists, markers,labels,space)
        plot_degree_clustering(degree_dist_cities,cities_clustering,markers, labels,space)
        
        plot_assortativity(number_of_nodes,cities_assortativity ,markers, labels, colors,space, style = 'semilog')
        plot_assortativity(number_of_nodes,cities_assortativity ,markers, labels, colors,space, style = None)