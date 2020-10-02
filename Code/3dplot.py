import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from collections import Counter
import seaborn as sns
import plotly.express as px

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%%
if __name__ == '__main__':
    labels = get_list_cities_names()
    markers = ['o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	
               ,'h'	,'H'	,'+'	,'x'	,'D'	,'d'	,'8' , 'P','X',
               'o'	,'v'	,'^','<','>'	,'s'	,'p'	,'*'	,'h'	,'H']
    
    spaces = ['lspace','pspace','cspace']
    cities = get_list_cities_names()
    network_measures = []
    for space in spaces:   
        with open(f'../Results/All_cities/{space}.json', 'r') as f:
            network_measures.append(json.load(f))
            
    colors = ['Aqua', 'Black', 'Blue','BlueViolet','Brown','Chartreuse',
              'Chocolate','Crimson','DarkCyan','DarkGreen','DarkRed','DeepPink'
              ,'DodgerBlue','ForestGreen','Gold','Indigo','Lime','Magenta',
              'Olive', 'OrangeRed','Purple','Red','Salmon', 'SpringGreen',
              'Teal','Tomato','Violet']
    
    
    random_df = pd.read_csv('../Results/random_df.csv',encoding='utf-8',delimiter=",") 
    lspace_df = pd.read_csv('../Results/lspace_df.csv',encoding='utf-8',delimiter=",")
    pspace_df =  pd.read_csv('../Results/pspace_df.csv',encoding='utf-8',delimiter=",") 
    cspace_df =  pd.read_csv('../Results/cspace_df.csv',encoding='utf-8',delimiter=",") 
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection='3d')
    ax.scatter(lspace_df['degree'], pspace_df['degree'], cspace_df['degree'],
               c = 'b', s=60)
    ax.azim = 200
    ax.elev = 45
    ax.set_xlabel('Lspace')
    ax.set_ylabel('Pspacel')
    ax.set_zlabel('Cspace')
    ax.set_title('Average degree')
    plt.show()
    
    fig,ax = plt.subplots(3, 1, figsize=(15, 20)) 
    ax[0].scatter(lspace_df['degree'], pspace_df['degree'],
               c = 'b', s=60)
    ax[1].scatter(lspace_df['degree'], cspace_df['degree'],
               c = 'g', s=60)
    ax[2].scatter(pspace_df['degree'], pspace_df['degree'],
               c = 'r', s=60)
    plt.show()
    
    