import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
    features = ['nodes','edges','clustering','degree','shortest path','assortativity']

    random_df = pd.read_csv('../Results/random_df.csv',encoding='utf-8',delimiter=",")   
    r = random_df.loc[:, features].values
    r = StandardScaler().fit_transform(r)
    r_t = r.T
    cov_r = np.cov(r_t)
    eig_vals_r,eig_vecs_r = np.linalg.eig(cov_r)
    print('Eigenvalues %s'%eig_vals_r)
    print('Eigenvalues ratio %s'% np.divide(eig_vals_r[0],sum(eig_vals_r)))
    projected_r = r.dot(eig_vecs_r.T[0])
    
    lspace_df = pd.read_csv('../Results/lspace_df.csv',encoding='utf-8',delimiter=",")   
    l = lspace_df.loc[:, features].values
    l = StandardScaler().fit_transform(l)
    l_t = l.T
    cov_l = np.cov(l_t)
    eig_vals_l,eig_vecs_l = np.linalg.eig(cov_l)
    print('Eigenvalues %s'%eig_vals_l)
    print('Eigenvalues ratio %s'% np.divide(eig_vals_l[0],sum(eig_vals_l)))
    projected_l = l.dot(eig_vecs_l.T[0])
    
    pspace_df =  pd.read_csv('../Results/pspace_df.csv',encoding='utf-8',delimiter=",") 
    p = lspace_df.loc[:, features].values
    p = StandardScaler().fit_transform(p)
    p_t = p.T
    cov_p = np.cov(p_t)
    eig_vals_p,eig_vecs_p = np.linalg.eig(cov_p)
    print('Eigenvalues %s'%eig_vals_p)
    print('Eigenvalues ratio %s'% np.divide(eig_vals_p[0],sum(eig_vals_p)))
    projected_p = p.dot(eig_vecs_p.T[0])
   
    cspace_df =  pd.read_csv('../Results/cspace_df.csv',encoding='utf-8',delimiter=",") 
    c = lspace_df.loc[:, features].values
    c = StandardScaler().fit_transform(c)
    c_t = c.T
    cov_c = np.cov(c_t)
    eig_vals_c,eig_vecs_c = np.linalg.eig(cov_c)
    print('Eigenvalues %s'%eig_vals_c)
    print('Eigenvalues ratio %s'% np.divide(eig_vals_c[0],sum(eig_vals_c)))
    projected_c = c.dot(eig_vecs_c.T[0])
    
    
    fig,ax = plt.subplots(4, 1,figsize=(10,15))
    ax = ax.flatten()

    ax[0].scatter(projected_l,projected_p, c='b', marker="s")
    ax[1].scatter(projected_l,projected_c,c='r', marker="o")
    ax[2].scatter(projected_p,projected_c, c='g', marker="*")
    ax[3].scatter(projected_l,projected_r,c='Lime', marker="X")
    
    ax[0].set_xlabel('PC lspace', fontsize = 15)
    ax[0].set_ylabel('PC pspace', fontsize = 15)  
    
    ax[1].set_xlabel('PC lspace', fontsize = 15)
    ax[1].set_ylabel('PC Cspace', fontsize = 15)
    
   
    ax[2].set_xlabel('PC pspace', fontsize = 15)
    ax[2].set_ylabel('PC space', fontsize = 15)
    
    ax[3].set_xlabel('PC lspace', fontsize = 15)
    ax[3].set_ylabel('PC random graph', fontsize = 15)  
    plt.savefig("../Results/graph/ownpca.pdf")
    