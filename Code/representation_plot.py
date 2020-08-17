import networkx as nx
import matplotlib.pyplot as plt
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
node_list13 = [1,2,3,4,5,6,7,8] 
edges_list13 = [(1,2),(2,3),(3,4),(4,5),(6,7),(7,8),(3,7),(4,7)]
G3.add_edges_from(edges_list13)


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 3, 1)
pos = nx.spring_layout(G)
nx.draw_networkx(G,pos=pos,ax=ax, edgelist =edges_list1 , edge_color = 'skyblue',width = 3, node_color =  'violet')
nx.draw_networkx(G,pos=pos,ax=ax, edgelist =edges_list2 , edge_color = 'blue', width = 3, node_color = 'violet')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title('Lspace')

ax2 = fig.add_subplot(1, 3, 2)
pos2 = nx.spring_layout(G2)
nx.draw_networkx(G2,pos=pos2,ax=ax2, edgelist =edges_list12 , edge_color = 'skyblue',width = 3 , node_color =  'violet')
nx.draw_networkx(G2,pos=pos2,ax=ax2, edgelist =edges_list22 , edge_color = 'blue', width = 3, node_color =  'violet' )
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax2.set_title('Pspace')

ax3 = fig.add_subplot(1, 3, 3)
pos3 = nx.spring_layout(G3)
nx.draw_networkx(G3,pos=pos3,ax=ax3, edgelist = edges_list13 , edge_color = 'violet',width = 3 , node_color = 'skyblue')
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
ax3.set_title('Cspace')
plt.savefig(f'all_space.pdf')
plt.show()

