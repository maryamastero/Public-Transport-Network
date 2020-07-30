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
def plot_ccdfs(uniq_degs,datavecs,markers, labels):
    '''
    Plots in a single figure the complementary cumulative distributions
    
    '''
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for x_values, y_values, marker, label  in zip(uniq_degs,datavecs, markers, labels):    
        ax.loglog(x_values, y_values, marker, label = label) 

    ax.set_xlabel('Degree' ) 
    ax.set_ylabel('1-CDF degree') 
    ax.legend(loc=0)
    ax.set_title('Degree distribution in p_space')
    plt.savefig("Degree_distribution_p_space.pdf", dpi=150)


    plt.show()

    return fig

#%%
def plot_degree_clustering(degrees,clusteringvec, markers, labels):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for degree,clustering, marker, label  in zip(degrees,clusteringvec, markers, labels):    
        
        df = pd.DataFrame({"degree":degree,"clustering":clustering})
        df = df.sort_values(["degree"])
        mean_cluster = df.groupby("degree").mean()
        bins = np.array(mean_cluster.index.tolist())
        
        ax.plot(bins,mean_cluster,marker, label = label)
        
    ax.set_xlabel('Degree') 
    ax.set_ylabel('Clustering Coefficient (ci)') 
    ax.set_title('Clustering coefficient in p_space')

    ax.legend(loc=0)
    plt.savefig("Clustering_coefficient_p_space.pdf", dpi=150)

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
    
with open('../Results/network_measures_pspace.json', 'r') as f:
    network_measures = json.load(f)
    
degree_dist_cities = []
uniq_degs = []
normalized_deg_dists = []
cities_clustering = []
for i in range(len(network_measures)):
    degree_dist_cities.append(network_measures[i]['Degree distribution'])   
    uniq_deg, normalized_deg_dist = ccdf(network_measures[i]['Degree distribution'])
    uniq_degs.append(uniq_deg)
    normalized_deg_dists.append(normalized_deg_dist)
    cities_clustering.append(network_measures[i]['Clustering coeficient'])
    
    
#%%    
if __name__ == '__main__':   
    
    labels = get_list_cities_names()
    markers = [ '-', '-.','.', '--', '-o', '-+','-*','+','_','_-','*','-', '-.','.', '--', 
               '-o', '-+','-*','+','_','_-','*', '--', '-o', '-+','-*','+']
    plot_ccdfs(uniq_degs,normalized_deg_dists, markers,labels);
    
    plot_degree_clustering(degree_dist_cities,cities_clustering,markers, labels);