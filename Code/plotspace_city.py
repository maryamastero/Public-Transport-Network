import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import itertools
from matplotlib.lines import Line2D

city = 'berlin'
transport_type = {-1: 'walking',0: 'tram', 1: 'subway', 2: 'rail',
                  3: 'bus', 4: 'ferry', 5: 'cablecar', 6: 'gondola', 7: 'funicular'}

transport_id_color = {0: 'g', 1: 'skyblue', 2: 'r', 3: 'b', 4: 'magenta', 5: 'y', 6: 'm', 7: 'maroon'}

def make_proxy(clr, **kwargs):
    return Line2D([0, 1], [0, 1], color=clr, **kwargs)

path = '../data/'+ city +'/network_nodes.csv'
nodes_info = pd.read_csv(path, delimiter=";")
nodes_df = pd.DataFrame(nodes_info, columns=['stop_I', 'lat', 'lon', 'name'])
path = '../data/' + city + '/network_combined.csv'
edges_info = pd.read_csv(path, delimiter=";")
edges_df = pd.DataFrame(edges_info, columns=['from_stop_I', 'to_stop_I', 'd', 'duration_avg', 'n_vehicles',
                                             'route_I_counts', 'route_type'])
    
path ='../data/' + city + '/network_temporal_day.csv'
data = pd.read_csv(path, delimiter=";")
data_df = pd.DataFrame(data, columns=['from_stop_I', 'to_stop_I', 'dep_time_ut','arr_time_ut',
                                             'route_type','trip_I','seq','route_I'])

net_l = nx.Graph()
for index, row in nodes_df.iterrows():
        net_l.add_node(row['stop_I'], coords=(row['lat'], row['lon']), pos=(row['lon'], row['lat']))
for index, row in edges_df.iterrows():
    net_l.add_edge(row['from_stop_I'], row['to_stop_I'],
                 type=transport_type[row['route_type']],
                color = transport_id_color[row['route_type']])

net_p = nx.Graph()
for index, row in nodes_df.iterrows():
        net_p.add_node(row['stop_I'], coords=(row['lat'], row['lon']), pos=(row['lon'], row['lat']))


routs = {}
routs_type = {}
rout_number = 0
routs_type[rout_number] = data_df.route_type[rout_number]
routs[rout_number] = [data_df.from_stop_I[rout_number], data_df.to_stop_I[rout_number]]
for i in range(1,data_df.shape[0]):
        
        if(data_df.trip_I[i] == data_df.trip_I[i-1]):  
            routs[rout_number].append(data_df.to_stop_I[i])

        else:
            rout_number += 1 
            temp = [data_df.from_stop_I[i], data_df.to_stop_I[i]]
            routs[rout_number] = temp
            routs_type[rout_number] = data_df.route_type[i]


unique_routs = {}
for k,v in routs.items():
    if v not in unique_routs.values():
        unique_routs[k]= v  
routs = unique_routs

for k,v in routs.items():
    for cnt1 in range(len(v)):
        for cnt2 in range(cnt1+1,len(v)):
            net_p.add_edge(v[cnt1],v[cnt2],color = transport_id_color[routs_type[k]] )
            

edges_c  = []
for ktuple in itertools.combinations(routs,2):
    if [value for value in routs[ktuple[0]] if value in routs[ktuple[1]]] != []:
        edges_c.append(ktuple)
        
net_c = nx.Graph()
net_c.add_edges_from(edges_c)        


colors = nx.get_edge_attributes(net_l, 'color').values()
all_colors = set(colors)
all_edge_types = {'g': 'Tram', 'skyblue': 'Subway', 'r': 'Rail', 'b': 'Bus', 'magenta': 'Ferry',
                  'y': 'Cable car', 'm': 'Gondola', 'maroon': 'Funicular'}
edge_types = {color: all_edge_types[color] for color in all_colors}

fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(1, 3, 1)


nx.draw_networkx(net_l, ax=ax1, pos=nx.get_node_attributes(net_l, 'pos'), with_labels=False, node_size=0.5,
                 edge_color=colors, alpha=0.5, node_color = 'black')

proxies = [make_proxy(clr, lw=5) for clr in edge_types.keys()]
labels = [edge_type for clr, edge_type in edge_types.items()]
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.set_title('lspace')
plt.legend(proxies, labels);

colors_p = nx.get_edge_attributes(net_p, 'color').values()
ax2 = fig.add_subplot(1, 3, 2)
nx.draw_networkx(net_p, ax=ax2,pos=nx.get_node_attributes(net_p, 'pos'), with_labels=False, node_size=0.5,
                 alpha=0.5, node_color = 'black', edge_color = colors_p)


ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
proxies = [make_proxy(clr, lw=5) for clr in edge_types.keys()]
labels = [edge_type for clr, edge_type in edge_types.items()]
ax2.set_title('pspace')
plt.legend(proxies, labels);


ax3 = fig.add_subplot(1, 3, 3)
GCC = max((net_c.subgraph(c) for c in nx.connected_components(net_c)), key=len) 
nx.draw_networkx(GCC, ax=ax3, with_labels=False, node_size=0.5,
                 alpha=0.5, node_color = 'black', edge_color = 'b')


plt.legend(scatterpoints = 1)
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
ax3.set_title('cspace')
fig.tight_layout()
plt.savefig(f'all_space_{city}.pdf')