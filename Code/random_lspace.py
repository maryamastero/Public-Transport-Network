import networkx as nx
import json
import sys
#%% Creating network 
        
def create_random_network(city):
    '''
    Create network a random network by configuration model method in  L-space for each city
    (Stops are represented by nodes; they are linked if two consecutive stops have a share route.)
    '''
    with open(f'../Results/lspace/{city}.json', 'r') as f:
        degree_sequence = json.load(f)['Degree distribution']

   
    net = nx.configuration_model(degree_sequence)
    net=nx.Graph(net)
    net.remove_edges_from(nx.selfloop_edges(net))

    return net

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
    
    return output


#%% lspace calculation for whole data set 

if __name__ == '__main__':
    
    city = sys.argv[1]
    network_measures = compute_measures(city)
    print(network_measures)
    temp_file = open(f"../Results/random/lspace/{city}/{city}.json", "w")
    json.dump(network_measures, temp_file)
    temp_file.close()
           