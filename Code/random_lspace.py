import networkx as nx
import json

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%% Creating network 
        
def create_random_network(city):
    '''
    Create network a random network by configuration model method in  L-space for each city
    (Stops are represented by nodes; they are linked if two consecutive stops have a share route.)
    '''
    with open(f'../Results/lspace/{city}.json', 'r') as f:
        degree_sequence = json.load(f)['Degree distribution']

   
    G = nx.configuration_model(degree_sequence)
    G=nx.Graph(G)
    G.remove_edges_from(G.selfloop_edges())

    return G

#%% Calculate network measure for each city

def compute_measures(city):
    
    out = {}
    temp_file0 = open(f"../Results/random/lspace/{city}/temp_{city}.json", "w")
    json.dump(out, temp_file0)
    temp_file0.close()

    net = create_random_network(city)
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
    
    temp_file = open(f"../Results/random/lspace/{city}/{city}.json", "w")
    json.dump(output, temp_file)
    temp_file.close()
    
    return output


#%% lspace calculation for whole data set 

if __name__ == '__main__':
    
    cities = get_list_cities_names() 
    
    network_measures = {}
    for city in cities:
        network_measures[city] = compute_measures(city)