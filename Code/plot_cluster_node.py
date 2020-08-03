import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_degree_clustering(degrees,clusteringvec, markers, labels,space):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for degree,clustering, marker, label  in zip(degrees,clusteringvec, markers, labels):    
        #ax.plot(degree,clustering,marker, label = label, linestyle= "solid")
        df = pd.DataFrame({"degree":degree,"clustering":clustering})
        df = df.sort_values(["degree"])
        mean_cluster = df.groupby("degree").mean()
        bins = np.array(mean_cluster.index.tolist())
        bin_average = np.array(mean_cluster["clustering"].tolist())
        
        ax.plot(bins,bin_average,marker, label = label, linestyle= "solid")
        
    ax.set_xlabel('Degree') 
    ax.set_ylabel('Clustering Coefficient (ci)') 
    ax.set_title('Clustering coefficient in p_space')

    ax.legend(loc=0)
    plt.savefig(f"../Results/graph/Clustering_coefficient_degree_{space}.pdf", dpi=150)

    plt.show()
    return fig


def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities


if __name__ == '__main__':
    labels = get_list_cities_names()
    markers = ['o'	,'v'	,'^',
               	'<','>'	,'1'	,'2'	,'3'	,'4'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X']
    
    spaces = ['lspace.json','pspace.json','cspace.json']
    network_measures = []
    for space in spaces:   
        with open(f'../Results/All_cities/{space}', 'r') as f:
            network_measures.append(json.load(f))
            
    for i, space in enumerate(spaces):
        binned_degree = []
        degree_dist_cities = []
        cities_clustering = []
        for j in range(len(network_measures[i])):
            cities_clustering.append(network_measures[i][j]['Clustering coeficient'])
            degree_dist_cities.append(network_measures[i][j]['Degree distribution'])              
        
        plot_degree_clustering(degree_dist_cities,cities_clustering,markers, labels, space);