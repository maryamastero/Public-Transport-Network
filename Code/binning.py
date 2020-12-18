import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd
from scipy.stats import binned_statistic

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities



#%%
def plot_degree_betweenness_one_city(n_city,degrees,betweennesses,closeness,degree_l):
   
    fig = plt.figure(figsize=(20,10)) 
    cities = get_list_cities_names()
    x = degrees[n_city]
    y = betweennesses[n_city]
    z = closeness[n_city]
    w = degree_l[n_city]
    n_bins = len(np.unique(degree_dist_lspace[n_city]))
    bin_centers, _, _ = binned_statistic(x, x,
    statistic='mean',
    bins=n_bins)
    bin_averages, _, _ = binned_statistic(x, y,
    statistic='mean',
    bins=n_bins)
    
    bin_centers0, _, _ = binned_statistic(w, w,
    statistic='mean',
    bins=n_bins)
    bin_averages0, _, _ = binned_statistic(w, y,
    statistic='mean',
    bins=n_bins)
    
    
    ax3 = fig.add_subplot(141)
    ax3.scatter(w,y, alpha=0.5, label="Real values", color = 'skyblue')
    ax3.plot(bin_centers0, bin_averages0, "o-", label= 'Binned data' ,color ='r')
    ax3.legend(loc='best')
    ax3.set_xlabel("Degree in Lspace",fontsize=14, fontweight='bold')
    ax3.set_ylabel('Betweenness in Lspace',fontsize=14, fontweight='bold') 
    ax3.set_title('Betweenness ' + str(cities[n_city]))

    ax1 = fig.add_subplot(142)
    ax1.scatter(x,y, alpha=0.5, label="Real values", color = 'skyblue')
    ax1.plot(bin_centers, bin_averages, "bo-", label= 'Binned data' )
    ax1.legend(loc='best')
    ax1.set_xlabel("Degree in Pspace",fontsize=14, fontweight='bold')
    ax1.set_ylabel("Betweenness in Lspace",fontsize=14, fontweight='bold')
    ax1.set_title('Betweenness '+ str(cities[n_city]))
    
    bin_centers3, _, _ = binned_statistic(w, w,
    statistic='mean',
    bins=n_bins)
    bin_averages3, _, _ = binned_statistic(w, x,
    statistic='mean',
    bins=n_bins)
    
    ax4 = fig.add_subplot(143)
    ax4.scatter(w,y, alpha=0.5, label="Real values", color = 'skyblue')
    ax4.plot(bin_centers3, bin_averages3, "o-", label= 'Binned data' ,color ='m')
    ax4.legend(loc='best')
    ax4.set_xlabel("Degree in Lspace",fontsize=14, fontweight='bold')
    ax4.set_ylabel('Degree in Lspace',fontsize=14, fontweight='bold') 
    ax4.set_title('Degree - Degree ' + str(cities[n_city]))

    bin_averages2, _, _ = binned_statistic(x, z,
    statistic='mean',
    bins=n_bins)

    ax2 = fig.add_subplot(144)
    ax2.scatter(x,z, alpha=0.5, label="Real values", color = 'skyblue')
    ax2.plot(bin_centers, bin_averages2, "o-", label= 'Binned data' ,color ='darkblue')
    ax2.legend(loc='best')
    ax2.set_xlabel("Degree in Pspace",fontsize=14, fontweight='bold')
    ax2.set_ylabel('closeness in Lspace',fontsize=14, fontweight='bold') 
    ax2.set_title('Closeness ' + str(cities[n_city]))
    
    
    
    #.savefig(f"../Results/graph4/{cities[n_city]}_Lspace_betweeneess_Pspace_degree.pdf", format='pdf')
    plt.savefig(f"../Results/graph4/{cities[n_city]}.pdf", format='pdf')


    plt.show()

    return fig


#%%
if __name__ == '__main__':
    cities = get_list_cities_names()
    labels = get_list_cities_names()
    
    network_measures_pspace = []
    with open('../Results/All_cities/pspace.json', 'r') as f:
        network_measures_pspace.append(json.load(f))
            
        
    all_data_lspace = []
    with open('../Results/All_cities/lspace.json', 'r') as f:
        all_data_lspace.append(json.load(f))
        
    degree_dist_pspace = []
    ave_shortest_path_pspace = []
    for j in range(len(network_measures_pspace[0])):
        ave_shortest_path_pspace.append(float(network_measures_pspace[0][j]['Average shortest path']))
        degree_dist_pspace.append(network_measures_pspace[0][j]['Degree distribution'])
        
    degree_dist_lspace = []
    for j in range(len(all_data_lspace[0])):
        degree_dist_lspace.append(all_data_lspace[0][j]['Degree distribution'])
    
    network_measures_lspace = []
    with open('../Results/lspace_centrality/network_centrality_measures_lspace.json', 'r') as f:
        network_measures_lspace.append(json.load(f))     
            
    betweenness_lspace = []
    closeness_lspace = []
    
    
    for city in cities:
        betweenness_lspace.append(list(network_measures_lspace[0][city]['betweenness'].values()))
        closeness_lspace.append(list(network_measures_lspace[0][city]['closeness'].values()))
    
    
    for n_city in range(len(cities)):
        #plot_degree_betweenness_one_city(n_city,degree_dist_pspace,closeness_lspace)
        plot_degree_betweenness_one_city(n_city,degree_dist_pspace,betweenness_lspace,closeness_lspace,degree_dist_lspace)
