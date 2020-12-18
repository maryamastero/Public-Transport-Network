import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities


#%%
def plot_degree_betweenness(degrees,betweennesses, markers, labels):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    for degree,betweenness, marker, label  in zip(degrees,betweennesses, markers, labels):    
        
        df = pd.DataFrame({"degree":degree,"betweennesses":betweenness})
        df = df.sort_values(["degree"])
        mean_betweennesses = df.groupby("degree").mean()
        bins = np.array(mean_betweennesses.index.tolist())
        
        ax.plot(bins,mean_betweennesses,marker, label = label, linestyle= "solid")
        
    ax.set_xlabel('Degree') 
    ax.set_ylabel('betweenness') 
    ax.set_title('betweenness Lpace vs degree dist Pspace')

    ax.legend(loc='best')
    plt.savefig("../Results/graph2/betweenness_degree.pdf", format='pdf')

    plt.show()
    return fig

#%%
def plot_degree_betweenness_one_city(n_city,degrees,betweennesses):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    cities = get_list_cities_names()
    degree = degrees[n_city]
    betweenness = betweennesses[n_city]
    df = pd.DataFrame({"degree":degree,"betweennesses":betweenness})
    df = df.sort_values(["degree"])
    mean_betweennesses = df.groupby("degree").mean()
    bins = np.array(mean_betweennesses.index.tolist())
    
    ax.plot(bins,mean_betweennesses,'ro-', label = cities[n_city], linestyle= "solid")
    
    ax.set_xlabel('Degree in Lspace',fontsize=14, fontweight='bold') 
    #ax.set_ylabel('closeness in Lspace',fontsize=14, fontweight='bold') 
    ax.set_ylabel('Betweenness in Lspace',fontsize=14, fontweight='bold') 

    ax.legend(loc='best')
    #plt.savefig(f"../Results/graph2/{cities[n_city]}_Lspace_closeness_Pspace_degree.pdf", format='pdf')
    plt.savefig(f"../Results/graph2/{cities[n_city]}_Lspace_betweeneess_Lspace_degree.pdf", format='pdf')


    plt.show()
    return fig
#%%
def scatter_plot_degree_betweenness_one_city(n_city,degrees,betweennesses):
   
    fig = plt.figure(figsize=(8,6)) 
    ax = fig.add_subplot(111)
    cities = get_list_cities_names()
    degree = degrees[n_city]
    betweenness = betweennesses[n_city]
    
    
    ax.scatter(degree,betweenness, label = cities[n_city], color='m')
    
    ax.set_xlabel('Degree in lspace',fontsize=14, fontweight='bold') 
    #ax.set_ylabel('closeness in Lspace',fontsize=14, fontweight='bold') 
    #ax.set_ylabel('Betweenness in Lspace',fontsize=14, fontweight='bold')
    ax.set_ylabel('Degree in Pspace',fontsize=14, fontweight='bold') 

    ax.legend(loc='best')
    #plt.savefig(f"../Results/graph3/{cities[n_city]}_scatter_Lspace_closeness_Lspace_degree.pdf", format='pdf')
    #plt.savefig(f"../Results/graph3/{cities[n_city]}_scatter_Lspace_betweenneess_pspace_degree.pdf", format='pdf')
    plt.savefig(f"../Results/graph3/{cities[n_city]}_scatter_pspace_degree_lspace_degree.pdf", format='pdf')



    plt.show()
    return fig

#%%
def plot_degree_degree_one_city(n_city,degree_dist_pspace,degree_dist_lspace):
   
    fig = plt.figure(figsize=(15,10)) 
    ax = fig.add_subplot(111)
    cities = get_list_cities_names()
    degree_p = degree_dist_pspace[n_city]
    degree_l = degree_dist_lspace[n_city]
    df = pd.DataFrame({"degree l":degree_l,"degree p":degree_p})
    df = df.sort_values(["degree l"])
    mean_degree_p = df.groupby("degree l").mean()
    bins = np.array(mean_degree_p.index.tolist())

    
    ax.plot(bins,mean_degree_p,'mo-', label = cities[n_city], linestyle= "solid")
    
    ax.set_xlabel('Degree in Lspace', fontsize=14, fontweight='bold') 
    ax.set_ylabel('Degree in Pspace', fontsize=14, fontweight='bold') 
    ax.legend(loc='best')
    plt.savefig(f"../Results/graph2/{cities[n_city]}_Lspace_degree_Lspace_degree.pdf", format='pdf')
    

    plt.show()
    return fig

#%%
def get_pearson_coef(n_city,degree_dist_pspace,degree_dist_lspace):
   
    cities = get_list_cities_names()
    degree_p = degree_dist_pspace[n_city]
    degree_l = degree_dist_lspace[n_city]
    
    pearson_coef, p_value = pearsonr(degree_p,degree_l)


    #return {cities[n_city]:round(pearson_coef,2)}
    return round(pearson_coef,2)
#%%
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='Blue', row_colors=['skyblue', 'w'], edge_color='w',
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
    cities = get_list_cities_names()
    labels = get_list_cities_names()
    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    
    network_measures_pspace = []
    with open('../Results/All_cities/pspace.json', 'r') as f:
        network_measures_pspace.append(json.load(f))
            
        
    all_data_lspace = []
    with open('../Results/All_cities/lspace.json', 'r') as f:
        all_data_lspace.append(json.load(f))
        
        
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    
    degree_dist_pspace = []
    ave_shortest_path_pspace = []
    for j in range(len(network_measures_pspace[0])):
        ave_shortest_path_pspace.append(float(network_measures_pspace[0][j]['Average shortest path']))
        degree_dist_pspace.append(network_measures_pspace[0][j]['Degree distribution'])
    
    nodes_l = []
    edges_l = []
    degree_dist_lspace = []
    for j in range(len(all_data_lspace[0])):
        degree_dist_lspace.append(all_data_lspace[0][j]['Degree distribution'])
        nodes_l.append(all_data_lspace[0][j]['Number of nodes'])
        edges_l.append(all_data_lspace[0][j]['Number of edges'])
        
    
    network_measures_lspace = []
    with open('../Results/lspace_centrality/network_centrality_measures_lspace.json', 'r') as f:
        network_measures_lspace.append(json.load(f))     
            
    betweenness_lspace = []
    closeness_lspace = []
    
    
    for city in cities:
        betweenness_lspace.append(list(network_measures_lspace[0][city]['betweenness'].values()))
        closeness_lspace.append(list(network_measures_lspace[0][city]['closeness'].values()))
    
    
    #plot_degree_betweenness(degree_dist_pspace,betweenness_lspace, markers, labels)
    p_coef_b = []
    p_coef_c = []
    p_coef_d = []
    p_coef_bl = []
    p_coef_cl = []

    for n_city in range(len(cities)):
        #plot_degree_betweenness_one_city(n_city,degree_dist_pspace,closeness_lspace)
        #plot_degree_degree_one_city(n_city,degree_dist_pspace,degree_dist_lspace)
        #plot_degree_betweenness_one_city(n_city,degree_dist_lspace,betweenness_lspace)
        #scatter_plot_degree_betweenness_one_city(n_city,degree_dist_lspace,degree_dist_pspace)
        p_coef_b.append(get_pearson_coef(n_city,degree_dist_pspace,betweenness_lspace))
        p_coef_c.append(get_pearson_coef(n_city,degree_dist_pspace,closeness_lspace))
        p_coef_d.append(get_pearson_coef(n_city,degree_dist_pspace,degree_dist_lspace))
        p_coef_bl.append(get_pearson_coef(n_city,degree_dist_lspace,betweenness_lspace))
        p_coef_cl.append(get_pearson_coef(n_city,degree_dist_lspace,closeness_lspace))




    features = ['City','D_P, B_L','D_L, B_L', 'D_P, C_L','D_L, C_L', 'D_P, D_L']
    df_table = pd.DataFrame(list(zip(cities,p_coef_b, p_coef_bl,p_coef_c,p_coef_cl, p_coef_d)),columns= features)
    fig,ax = render_mpl_table(df_table, header_columns=0, col_width=2.0)
    plt.show()
   # fig.savefig("../Report/datafram.png")
    features2 = ['City','Nodes','L_space Edges','D_P, B_L','D_L, B_L', 'D_P, C_L','D_L, C_L', 'D_P, D_L']
    df = pd.DataFrame(list(zip(cities,nodes_l,edges_l,p_coef_b, p_coef_bl,p_coef_c,p_coef_cl, p_coef_d)),columns= features2)
   
    plt.scatter(range(1,28),sorted(df['D_P, B_L']),label = 'P-space degree vs Betweenness')
    plt.scatter(range(1,28),sorted(df['D_L, B_L']),label = 'L-space degree vs Betweenness')
    plt.scatter(range(1,28),sorted(df[ 'D_P, C_L']),label = 'P-space degree vs Clossness')
    plt.scatter(range(1,28),sorted(df[ 'D_L, C_L']),label = 'L-space degree vs Clossness')
    plt.scatter(range(1,28),sorted(df['D_P, D_L']),label = 'P-space degree vs L-space degree')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 15})
    plt.title('Sorted values')
    plt.show()
    
    
    plt.scatter(range(1,28),df['D_P, B_L'],label = 'P-space degree vs Betweenness')
    plt.scatter(range(1,28),df['D_L, B_L'],label = 'L-space degree vs Betweenness')
    plt.scatter(range(1,28),df[ 'D_P, C_L'],label = 'P-space degree vs Clossness')
    plt.scatter(range(1,28),df[ 'D_L, C_L'],label = 'L-space degree vs Clossness')
    plt.scatter(range(1,28),df['D_P, D_L'],label = 'P-space degree vs L-space degree')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 15})

    plt.title('Pure values')
    plt.show()
    
  
    
    
    max_dic = {'max nodes' : df['City'][df['Nodes'].idxmax()], 
                'max Degree P-space - Betweenness':df['City'][df['D_P, B_L'].idxmax()],
                'max Degree L-space - Betweenness':df['City'][df['D_L, B_L'].idxmax()],
                'max Degree P-space - Closeness':df['City'][df['D_P, C_L'].idxmax()],
                'max Degree L-space - Closeness':df['City'][df['D_L, B_L'].idxmax()],
                'max Degree P-space - Degree L-space':df['City'][df['D_P, D_L'].idxmax()]}

    
    
    min_dic = {'min nodes' : df['City'][df['Nodes'].idxmin()], 
                'min Degree P-space - Betweenness':df['City'][df['D_P, B_L'].idxmin()],
                'min Degree L-space - Betweenness':df['City'][df['D_L, B_L'].idxmin()],
                'min Degree P-space - Closeness':df['City'][df['D_P, C_L'].idxmin()],
                'min Degree L-space - Closeness':df['City'][df['D_L, B_L'].idxmin()],
                'min Degree P-space - Degree L-space':df['City'][df['D_P, D_L'].idxmin()]}

  #  plt.figure(figsize=(10, 20))
    heatmap = sns.heatmap(df[['D_P, B_L','D_L, B_L', 'D_P, C_L','D_L, C_L', 'D_P, D_L']], cmap="YlOrRd")#, square=True)
    heatmap.set_yticklabels(cities,rotation=0) 
    heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=0)    
    plt.setp(ax.get_yticklabels(), ha="center")
    plt.xlabel("Pearson Correlation Coefficient ")
    plt.ylabel("Cities") 
    plt.tight_layout()
    plt.savefig("../Results/graph5/heatmap2.pdf", format='pdf')
    plt.show()










    
    