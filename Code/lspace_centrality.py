import networkx as nx
import pandas as pd
import json
import numpy as np

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


#%%
def get_centrality_measures(city):
    network = create_network(city)
    betweenness = nx.betweenness_centrality(network, normalized=True)
    betweenness =np.array([v for k, v in  betweenness.items()])

    temp_file = open(f"../Results/lspace/betweenness_{city}.json", "w")
    json.dump(betweenness, temp_file)
    temp_file.close()
    
    return  betweenness

#%% lspace calculation for whole data set 

if __name__ == '__main__':
    
    cities = get_list_cities_names() 
    
    b_measures = {}
    for city in cities:
        b_measures[city] = get_centrality_measures(city)
  
#%% Making jon file for outputs:

    b_measures_file = open("../Results/network_centrality_measures_lspace.json", "w")
    json.dump(b_measures, b_measures_file)
    b_measures_file.close()