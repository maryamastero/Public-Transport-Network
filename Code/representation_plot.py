import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def make_proxy(clr, mappable, **kwargs):
    return Line2D([0, 1], [0, 1], color=clr, **kwargs)

_c = ['skyblue','blue'] # way too many colors, trim after
clrs = [c for c in _c]

G=nx.Graph()
nodes_list1 = [1,2,3,4,5,6,7,8,9]
edges_list1 = [(1,2),(2,3),(3,4),(4,5),(5,6)]
edges_list2 = [(4,7),(7,8),(4,9)]
G.add_edges_from(edges_list1)
G.add_edges_from(edges_list2)


G2=nx.Graph()
edges_list12 = [(1,2),(1,3),(1,4),(1,5),(1,6),(3,2),(4,2),(2,5),(2,6),
                (3,5),(3,6),(3,4),(4,5),(4,6),(5,6)]
edges_list22 = [(4,9),(4,7),(4,8),(7,8),(7,9),(9,8)]
G2.add_edges_from(edges_list12)
G2.add_edges_from(edges_list22)

G3 = nx.Graph()
nodes_list13 = [1,2,3,4,5,6,7,8] 
edges_list13 = [(1,2),(2,3),(3,4),(4,5),(6,7),(7,8),(3,7),(4,7)]
G3.add_edges_from(edges_list13)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos=pos,nodelist=nodes_list1 , node_color='red', label='Stops')
h1 = nx.draw_networkx_edges(G,pos=pos, edgelist =edges_list1 , edge_color = 'skyblue',width = 3)
h2 = nx.draw_networkx(G,pos=pos, edgelist =edges_list2 , edge_color = 'blue', width = 3)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
proxies = [make_proxy(clr, h2, lw=5) for clr in clrs]
labels = ['Route 1','Route 2']
legend = plt.legend(proxies, labels, loc='upper left')
handles, _ = ax1.get_legend_handles_labels()
labels =['Stops']
ax1.legend(handles, labels, loc='center left')
ax1.add_artist(legend)
plt.savefig("../Results/graph/lspace_representation.pdf", dpi=150)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
pos = nx.spring_layout(G2)
nx.draw_networkx_nodes(G2,pos=pos,nodelist=nodes_list1 , node_color='red', label='Stops')
h1 = nx.draw_networkx_edges(G2,pos=pos, edgelist =edges_list12 , edge_color = 'skyblue',width = 3)
h2 = nx.draw_networkx(G2,pos=pos, edgelist =edges_list22 , edge_color = 'blue', width = 3)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
proxies = [make_proxy(clr, h2, lw=5) for clr in clrs]
labels = ['Route 1','Route 2']
legend = plt.legend(proxies, labels, loc='upper left')
handles, _ = ax1.get_legend_handles_labels()
labels =['Stops']
ax1.legend(handles, labels, loc='center left')
ax1.add_artist(legend)
plt.savefig("../Results/graph/pspace_representation.pdf", dpi=150)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
pos = nx.spring_layout(G3)
nx.draw_networkx_nodes(G3,pos=pos,nodelist=nodes_list13 , node_color='red', label='Stops')
h1 = nx.draw_networkx_edges(G3,pos=pos, edgelist =edges_list13 , edge_color = 'skyblue',width = 3)
#h2 = nx.draw_networkx(G3,pos=pos, edgelist =edges_list22 , edge_color = 'blue', width = 3)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
proxies = [make_proxy(clr, h1, lw=5) for clr in clrs]
labels = ['Stops']
legend = plt.legend(proxies, labels, loc='upper left')
handles, _ = ax1.get_legend_handles_labels()
labels =['Routes']
ax1.legend(handles, labels, loc='center left')
ax1.add_artist(legend)
plt.savefig("../Results/graph/cspace_representation.pdf", dpi=150)


network = G
nodes = network.nodes()
degrees = nx.degree_centrality(network)
betweenness = nx.betweenness_centrality(network, normalized=True)
closeness = nx.closeness_centrality(network)
   
degree1 = np.array([v for k, v in  sorted(degrees.items(), key=lambda pair: list(nodes).index(pair[0]))])
betweenness1 =np.array([v for k, v in  sorted(betweenness.items(), key=lambda  item: item[1], reverse = True)])
closeness1 = np.array([v for k, v in  sorted(closeness.items(), key=lambda  item: item[1], reverse = True)])
