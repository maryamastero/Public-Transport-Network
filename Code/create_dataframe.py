import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities
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
if __name__ == '__main__':
    
    spaces = ['lspace','pspace','cspace']
    cities = get_list_cities_names()
    network_measures = []
    for space in spaces:   
        with open(f'../Results/All_cities/{space}.json', 'r') as f:
            network_measures.append(json.load(f))
            
    all_space_ave_clustering = []
    all_space_ave_shortest_path = []
    all_space_assortativity = []
    all_space_ave_degree = []
    all_space_number_of_nodes = []
    all_space_number_of_edges = []
    
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
        for j in range(len(network_measures[i])):
            number_of_nodes.append(int(network_measures[i][j]['Number of nodes'])) 
            number_of_edges.append(int(network_measures[i][j]['Number of edges']))
            ave_clustering.append(float(network_measures[i][j]['Average clustering coefficient']))
            ave_shortest_path.append(float(network_measures[i][j]['Average shortest path']))
            ave_degree.append(float(network_measures[i][j]['Average degree']))
            cities_assortativity.append(float(network_measures[i][j]['Assortativity']))
             
        all_space_ave_clustering.append(ave_clustering )
        all_space_ave_shortest_path.append(ave_shortest_path )
        all_space_assortativity.append(cities_assortativity )
        all_space_ave_degree.append(ave_degree )
        all_space_number_of_nodes.append(number_of_nodes)
        all_space_number_of_edges.append(number_of_edges)
    
    
    mean_number_of_nodes_random = []
    mean_ave_clustering_random = []
    mean_ave_shortest_path_random =[]
    mean_assortativity_random = []
    mean_ave_degree_random =[]
    mean_number_of_edges_random = []
    for city in cities:
        network_measures_random = []
        with open(f'../Results/random/lspace/{city}.json', 'r') as f:
            s = f.read()
            s = s.replace('\'','\"')
            data = json.loads(s)          
            network_measures_random.append(data)           
        number_of_nodes_random = []
        ave_clustering_random = []
        ave_shortest_path_random = []
        assortativity_random = []
        ave_degree_random = []
        number_of_edges_random = []
        for j in range(len(network_measures_random[0])):
            number_of_nodes_random.append(int(network_measures_random[0][j]['Number of nodes'])) 
            number_of_edges_random.append(int(network_measures_random[0][j]['Number of edges']))
            ave_clustering_random.append(float(network_measures_random[0][j]['Average clustering coefficient']))
            ave_shortest_path_random.append(float(network_measures_random[0][j]['Average shortest path']))
            ave_degree_random.append(float(network_measures_random[0][j]['Average degree']))
            assortativity_random.append(float(network_measures_random[0][j]['Assortativity']))
      
        mean_number_of_nodes_random.append(np.mean(number_of_nodes_random))
        mean_ave_clustering_random.append(np.mean(ave_clustering_random))
        mean_ave_shortest_path_random.append(float("%.2f"% np.mean(ave_shortest_path_random)))
        mean_assortativity_random.append(float("%.2f"% np.mean(assortativity_random)))
        mean_ave_degree_random.append(float("%.2f"% np.mean(ave_degree_random)))
        mean_number_of_edges_random.append(np.mean(number_of_edges_random))
        
    
    features = ['nodes','edges','clustering','degree','shortest path','assortativity']

    random_df = pd.DataFrame(list(zip(mean_number_of_nodes_random,
                                      mean_number_of_edges_random,
                                      mean_ave_clustering_random,
                                       mean_ave_degree_random,
                                          mean_ave_shortest_path_random,
                                          mean_assortativity_random)),
                                 columns= features)
    random_df.to_csv('../Results/random_df.csv',encoding='utf-8', index=False)
    fig,ax = render_mpl_table(random_df, header_columns=0, col_width=2.0)
    fig.savefig("../Results/graph/random_datafram.png")   
    
    lspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][0],
                                      all_space_number_of_edges[:][0],
                                      all_space_ave_clustering[:][0],
                                          all_space_ave_degree[:][0],
                                          all_space_ave_shortest_path[:][0],
                                          all_space_assortativity[:][0])),
                                 columns=features)
    
    fig,ax = render_mpl_table(lspace_df, header_columns=0, col_width=2.0)
    fig.savefig("../Results/graph/lspace_datafram.png")   
    lspace_df.to_csv('../Results/lspace_df.csv',encoding='utf-8', index=False)

    
    pspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][1],
                                      all_space_number_of_edges[:][1],
                                      all_space_ave_clustering[:][1],
                                          all_space_ave_degree[:][1],
                                          all_space_ave_shortest_path[:][1],
                                          all_space_assortativity[:][1])),
                                 columns= features)
    pspace_df.to_csv('../Results/pspace_df.csv',encoding='utf-8', index=False)
    fig,ax = render_mpl_table(pspace_df, header_columns=0, col_width=2.0)
    fig.savefig("../Results/graph/pspace_datafram.png")   
    
    cspace_df = pd.DataFrame(list(zip(all_space_number_of_nodes[:][2],
                                      all_space_number_of_edges[:][2],
                                      all_space_ave_clustering[:][2],
                                          all_space_ave_degree[:][2],
                                          all_space_ave_shortest_path[:][2],
                                          all_space_assortativity[:][2])),
                                 columns= features)
    cspace_df.to_csv('../Results/cspace_df.csv',encoding='utf-8', index=False)
    fig,ax = render_mpl_table(cspace_df, header_columns=0, col_width=2.0)
    fig.savefig("../Results/graph/cspace_datafram.png")   
