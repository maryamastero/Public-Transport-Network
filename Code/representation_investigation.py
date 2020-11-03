import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import itertools
import pandas as pd
#%%
def compute_measures(net):

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
#%%
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax.get_figure(), ax

#%%
def create_lspace_network(number_of_node):
    net = nx.random_tree(number_of_node)

    return net


#%%
def create_pspace_network(number_of_node):
    net = nx.complete_graph(number_of_node)
    return net
    
#%%
def create_cspace_network(net_l):
    edges = []
    nodes = list(nx.nodes(net_l))
    for node in nodes:
        neighbors = []
        for neighbor in list(nx.neighbors(net_l,node)): 
            neighbors.append(neighbor)
        if len(neighbors) > 1:
            for ktuple in itertools.combinations(neighbors,2):
                edges.append(ktuple)
    net = nx.Graph()
    net.add_edges_from(edges)
    return net

#%%    
if __name__ == "__main__":

    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    features = ['nodes','edges','clustering','degree','shortest path','assortativity', 'diameter']

    spaces = ['lspace','pspace','cspace']
    
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    

    number_of_nodes = [5,10,20,50,100,200,500,1000]
    measures_lspace = []
    measures_pspace = []
    measures_cspace = []
    for number_of_node in number_of_nodes:
        net_l = create_lspace_network(number_of_node)
        measures_lspace.append(compute_measures(net_l))
        
        
        net_p = create_pspace_network(number_of_node)
        measures_pspace.append(compute_measures(net_p))
        
        net_c = create_cspace_network(net_l)
        measures_cspace.append(compute_measures(net_c))
        
    all_space_ave_clustering = []
    all_space_ave_shortest_path = []
    all_space_assortativity = []
    all_space_ave_degree = []
    all_space_number_of_nodes = []
    all_space_number_of_edges = []    
    all_space_Network_diameter = []
    network_measures = [measures_lspace ,measures_pspace,measures_cspace]
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
        Network_diameter = []
        for j in range(len(network_measures[i])):
            number_of_nodes.append(int(network_measures[i][j]['Number of nodes'])) 
            number_of_edges.append(int(network_measures[i][j]['Number of edges']))
            ave_clustering.append(float(network_measures[i][j]['Average clustering coefficient']))
            ave_shortest_path.append(float(network_measures[i][j]['Average shortest path']))
            ave_degree.append(float(network_measures[i][j]['Average degree']))
            cities_assortativity.append(float(network_measures[i][j]['Assortativity']))
            Network_diameter.append(network_measures[i][j]['Network diameter'])

             
        all_space_ave_clustering.append(ave_clustering )
        all_space_ave_shortest_path.append(ave_shortest_path )
        all_space_assortativity.append(cities_assortativity )
        all_space_ave_degree.append(ave_degree )
        all_space_number_of_nodes.append(number_of_nodes)
        all_space_number_of_edges.append(number_of_edges)
        all_space_Network_diameter.append(Network_diameter)

    lspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][0],
                              all_space_number_of_edges[:][0],
                              all_space_ave_clustering[:][0],
                                  all_space_ave_degree[:][0],
                                  all_space_ave_shortest_path[:][0],
                                  all_space_assortativity[:][0],
                                  all_space_Network_diameter[:][0])),
                         columns=features)
    
    fig,ax = render_mpl_table(lspace_df, header_columns=0, col_width=2.0)
   
    
    pspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][1],
                              all_space_number_of_edges[:][1],
                              all_space_ave_clustering[:][1],
                                  all_space_ave_degree[:][1],
                                  all_space_ave_shortest_path[:][1],
                                  all_space_assortativity[:][1],
                                  all_space_Network_diameter[:][1])),
                         columns= features)
    fig,ax = render_mpl_table(pspace_df, header_columns=0, col_width=2.0)
    
    cspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][2],
                              all_space_number_of_edges[:][2],
                              all_space_ave_clustering[:][2],
                                  all_space_ave_degree[:][2],
                                  all_space_ave_shortest_path[:][2],
                                  all_space_assortativity[:][2],
                                  all_space_Network_diameter[:][2])),
                         columns= features)
    fig,ax = render_mpl_table(cspace_df, header_columns=0, col_width=2.0)
