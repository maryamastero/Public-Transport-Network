import networkx as nx
import pandas as pd
from collections import Counter
import json
from multiprocessing import Pool

#%% Transportation type

transport_type = {-1: 'walking',0: 'tram', 1: 'subway', 2: 'rail', 3: 'bus',
            4: 'ferry', 5: 'cablecar', 6: 'gondola', 7: 'funicular'}

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%% Load nodes from the path

def load_nodes(net, path):
    '''
    Load nodes from network_nodes.csv
    nodes are stops
    
    '''
    nodes_info = pd.read_csv(path, delimiter=";")
    df = pd.DataFrame(nodes_info, columns=['stop_I', 'lat', 'lon', 'name'])
    for index, row in df.iterrows():
        net.add_node(row['stop_I'], coords=(row['lat'], row['lon']), pos=(row['lon'], row['lat']))

#%% Load edges from the path 
def load_edges(net, path):
    '''
    Load edges from network_combined.csv
    edges are routes between two stops
    
    '''
    edges_info = pd.read_csv(path, delimiter=";")
    df = pd.DataFrame(edges_info, columns=['from_stop_I', 'to_stop_I', 'd', 'duration_avg', 'n_vehicles',
                                           'route_I_counts', 'route_type'])
    for index, row in df.iterrows():
        net.add_edge(row['from_stop_I'], row['to_stop_I'],  type=transport_type[row['route_type']])

#%% Creating network 
        
def create_network(city):
    '''
    Create network in L-space for each city
    (Stops are represented by nodes; they are linked if two consecutive stops have a share route.)
    
    '''
    nodes_path = '../data/'+ city +'/network_nodes.csv'
    edges_path = '../data/' + city + '/network_combined.csv'
    
    net = nx.Graph()
    load_nodes(net, nodes_path)
    load_edges(net, edges_path)

    return net

#%% Count transport types
    
def transport_count_type(net):
    '''
    Represents number of different transportation types
    
    '''
    print(Counter(nx.get_edge_attributes(net, 'type').values()))

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
    
    temp_file = open(f"../Results/lspace/{city}.json", "w")
    json.dump(output, temp_file)
    temp_file.close()
    
    return output

#%% lspace calculation for whole data set 

if __name__ == '__main__':
    
    cities = get_list_cities_names() 
    
# =============================================================================
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

    network_measures_file = open("../Results/network_measures_lspace.json", "w")
    json.dump(network_measures, network_measures_file)
    network_measures_file.close()