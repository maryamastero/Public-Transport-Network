import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities

#%%
if __name__ == '__main__':
    
    spaces = ['lspace','pspace','cspace']
    cities = get_list_cities_names()
    features = ['nodes','edges','clustering','degree','shortest path','assortativity']

    random_df = pd.read_csv('../Results/random_df.csv',encoding='utf-8',delimiter=",")   
    r = random_df.loc[:, features].values
    r = StandardScaler().fit_transform(r)
    pca_r = PCA(n_components=2)
    principalComponents_r = pca_r.fit_transform(r)
    principalDf_random = pd.DataFrame(data = principalComponents_r
             , columns = ['principal component 1', 'principal component 2'])
    
    
    lspace_df = pd.read_csv('../Results/lspace_df.csv',encoding='utf-8',delimiter=",")   
    l = lspace_df.loc[:, features].values
    l = StandardScaler().fit_transform(l)
    pca_l = PCA(n_components=2)
    principalComponents_l = pca_l.fit_transform(l)
    principalDf_lspace = pd.DataFrame(data = principalComponents_l
             , columns = ['principal component 1', 'principal component 2'])
    
    pspace_df =  pd.read_csv('../Results/pspace_df.csv',encoding='utf-8',delimiter=",") 
    p = lspace_df.loc[:, features].values
    p = StandardScaler().fit_transform(p)
    pca_p = PCA(n_components=2)
    principalComponents_p = pca_p.fit_transform(p)
    principalDf_pspace = pd.DataFrame(data = principalComponents_p
             , columns = ['principal component 1', 'principal component 2'])
    
    
    cspace_df =  pd.read_csv('../Results/cspace_df.csv',encoding='utf-8',delimiter=",") 
    c = lspace_df.loc[:, features].values
    c = StandardScaler().fit_transform(c)
    pca_c = PCA(n_components=2)
    principalComponents_c = pca_c.fit_transform(c)
    principalDf_cspace = pd.DataFrame(data = principalComponents_c
             , columns = ['principal component 1', 'principal component 2'])
    
    
    fig,ax = plt.subplots(4, 1,figsize=(10,15))
    ax = ax.flatten()
    ax[0].set_xlabel('Principal Component l', fontsize = 15)
    ax[0].set_ylabel('Principal Component p', fontsize = 15)  
    ax[0].scatter(principalDf_lspace['principal component 1'],
                  principalDf_pspace['principal component 1'],
                  c='b', marker="s")

    ax[1].scatter(principalDf_lspace['principal component 1'],
                  principalDf_cspace['principal component 1'],
                  c='r', marker="o")
    ax[1].set_xlabel('Principal Component l', fontsize = 15)
    ax[1].set_ylabel('Principal Component c', fontsize = 15)
    
    ax[2].scatter(principalDf_pspace['principal component 1'],
                  principalDf_cspace['principal component 1'],
                  c='g', marker="*")
    ax[2].set_xlabel('Principal Component p', fontsize = 15)
    ax[2].set_ylabel('Principal Component c', fontsize = 15)
    
    ax[3].set_xlabel('Principal Component l', fontsize = 15)
    ax[3].set_ylabel('Principal Component r', fontsize = 15)  
    ax[3].scatter(principalDf_lspace['principal component 1'],
                  principalDf_random['principal component 1'],
                  c='Lime', marker="X")
    plt.savefig("../Results/graph/pca.pdf")
    