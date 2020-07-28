import networkx as nx
import pandas as pd
import itertools
import json
from multiprocessing import Pool

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities



#%% Load edges from the path
    
def get_edges_cspace(path):
    '''
    Calculate edges from network_temporal_day.csv
    (Each route is represented by a node; each link corresponds to a common stop shared by the route.)
    '''
    data = pd.read_csv(path, delimiter=";")
    data_df = pd.DataFrame(data, columns=['from_stop_I', 'to_stop_I', 'dep_time_ut','arr_time_ut',
                                                 'route_type','trip_I','seq','route_I'])
    routs = {}
    rout_number = 0
    routs[rout_number] = [data_df.from_stop_I[rout_number], data_df.to_stop_I[rout_number]]
    
    for i in range(1,data_df.shape[0]):
        
        if(data_df.trip_I[i] == data_df.trip_I[i-1]):  
            routs[rout_number].append(data_df.to_stop_I[i])

        else:
            rout_number += 1 
            temp = [data_df.from_stop_I[i], data_df.to_stop_I[i]]
            routs[rout_number]=temp

    unique_routs = {}
    for k,v in routs.items():
        if v not in unique_routs.values():
            unique_routs[k]= v  
    routs = unique_routs
    
    edges = []
    for ktuple in itertools.combinations(routs,2):
            if [value for value in routs[ktuple[0]] if value in routs[ktuple[1]]] != []:
                edges.append(ktuple)
    return edges


#%% Creating network 
        
def create_network(city):
    '''
    Create network in c-space for each city
    (Each route is represented by a node; each link corresponds to a common stop shared by the route.)
    
    '''
    edges_path = '../data/' + city + '/network_temporal_day.csv'
    
    net = nx.Graph()
    edges = get_edges_cspace(edges_path)
    net.add_edges_from(edges)

    return net


 
#%% Calculate network measure for each city

def compute_measures(city):
    
    net = create_network(city)
    output = {}
    GCC = max((net.subgraph(c) for c in nx.connected_components(net)), key=len) # Giant component 
    output['Number of nodes'] = nx.number_of_nodes(net) #Number of nodes
    output['Number of edges'] = nx.number_of_edges(net) #Number of edges
    output['Network density'] = "%.2f"% nx.density(net) #Network density
    output['Network diameter'] = nx.diameter(GCC) #Network diameter
    output['Average shortest path'] = "%.2f"% nx.average_shortest_path_length(GCC) #Average shortest path
    output['Average clustering coefficient'] = "%.2f"% nx.average_clustering(net, count_zeros=True) #Average clustering coefficient
    output['Average degree'] = "%.2f"% (2*net.number_of_edges() / float(net.number_of_nodes())) #Average degree
    output['Number of components in the network'] = len(list(net.subgraph(c) for c in nx.connected_components(net))) # Number of component in the network
    output['Assortativity'] = "%.2f"% nx.degree_assortativity_coefficient(net) #Assortativity
    output['Degree distribution'] = [net.degree(node) for node in nx.nodes(net)]
    output['Clustering coeficient'] = list(nx.clustering(net).values())
    
    temp_file = open(f"../logcspace/{city}.json", "w")
    json.dump(output, temp_file)
    temp_file.close()
    
    return output


#%% Cspace calculation for whole data set 

if __name__ == '__main__':
    
    cities = get_list_cities_names() 
# =============================================================================
#     
#     network_measures = {}
#     for city in cities:
#         network_measures[city] = compute_measures(city)
#     
# =============================================================================
    pool = Pool(4)       
    network_measures = pool.map(compute_measures,cities)
    pool.close()
    pool.join()
    
    
#%% Making jon file for outputs:

    network_measures_file = open("../Results/network_measures_cspace.json", "w")
    json.dump(network_measures, network_measures_file)
    network_measures_file.close()