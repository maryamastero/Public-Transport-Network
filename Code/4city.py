import numpy as np
import json
import matplotlib.pyplot as plt

#%% Calculate normalized distribution    
def ccdf(degree_dist):
    degree_dist = np.array(degree_dist)
    unique_degree_dist = np.unique(degree_dist) 
    ccdf = []
    normalizer=float(degree_dist.size) 

    for x in unique_degree_dist:
        ccdf.append((degree_dist[np.where(degree_dist >= x)].size)/normalizer)   

    return (unique_degree_dist.tolist(), ccdf)

#%%
def fit_powerlaw(xs, ys):
    S_lnx_lny = 0.0
    S_lnx_S_lny = 0.0
    S_lny = 0.0
    S_lnx = 0.0
    S_lnx2 = 0.0
    S_ln_x_2 = 0.0
    n = len(xs)
    for (x,y) in zip(xs, ys):
        S_lnx += np.log(x)
        S_lny += np.log(y)
        S_lnx_lny += np.log(x) * np.log(y)
        S_lnx_S_lny = S_lnx * S_lny
        S_lnx2 += np.power(np.log(x),2)
        S_ln_x_2 = np.power(S_lnx,2)
    #end
    b = (n * S_lnx_lny - S_lnx_S_lny ) / (n * S_lnx2 - S_ln_x_2)
    a = (S_lny - b * S_lnx)  / (n)
    return (np.exp(a), b)
#%%
def fit_exp(xs, ys):
    S_x2_y = 0.0
    S_y_lny = 0.0
    S_x_y = 0.0
    S_x_y_lny = 0.0
    S_y = 0.0
    for (x,y) in zip(xs, ys):
        S_x2_y += x * x * y
        S_y_lny += y * np.log(y)
        S_x_y += x * y
        S_x_y_lny += x * y * np.log(y)
        S_y += y
    #end
    a = (S_x2_y * S_y_lny - S_x_y * S_x_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
    b = (S_y * S_x_y_lny - S_x_y * S_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
    return (np.exp(a), b)

#%%%
if __name__=='__main__':    
   
    cities =  [ 'kuopio','berlin','paris', 'sydney']
# =============================================================================
#     cities =  ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
#       'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
#       'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
#       'venice', 'winnipeg']
# =============================================================================
    Bsl = []  
    fig,ax = plt.subplots(2, 2,figsize=(8,8), sharey = True, sharex= True)
    ax = ax.flatten()
    for j, city in enumerate(cities):   
        network_measures = []	
        with open(f'../Results/cspace/{city}.json', 'r') as f:	
            s = f.read()	
            s = s.replace('\'','\"')	
            data = json.loads(s)          	
            network_measures.append(data) 	

        uniq_deg, normalized_deg_dist = ccdf(network_measures[0]['Degree distribution'])   
        
        (A, B) = fit_exp(uniq_deg, normalized_deg_dist)
        Bsl.append(B)
        ax[j].loglog(uniq_deg, normalized_deg_dist, 'o-', label='Real Data', color = 'red')
        ax[j].loglog(uniq_deg, [A * np.exp(B *x) for x in uniq_deg], 'o-', label='Fit', color = 'skyblue')
        ax[j].set_title(f'Degree distribution in {city}', fontsize=10)    
       
                
   
    ax[2].set_xlabel('Degree' ) 
    ax[3].set_xlabel('Degree' ) 

    ax[0].set_ylabel('1-CDF degree') 
    ax[2].set_ylabel('1-CDF degree') 
    plt.tight_layout()
    st = fig.suptitle("Fitting exponential distribution to degree distribution in Cspace", fontsize="x-large", verticalalignment = 'baseline')
    st.set_y(1.0)
   
    plt.legend(bbox_to_anchor=(1.05, 2.25), loc='upper left', borderaxespad=0., fancybox=True)
    
        
    plt.show()

         
# =============================================================================
#     Bsp = []     
#     for j, city in enumerate(cities):   
#         network_measures = []	
#         with open(f'../Results/pspace/{city}.json', 'r') as f:	
#             s = f.read()	
#             s = s.replace('\'','\"')	
#             data = json.loads(s)          	
#             network_measures.append(data) 	
# 
#         uniq_deg, normalized_deg_dist = ccdf(network_measures[0]['Degree distribution'])
#    
# 
#         fig = plt.figure() 
#         ax = fig.add_subplot(111)
#         (A, B) = fit_exp(uniq_deg, normalized_deg_dist)
#         Bsp.append(B)
#         plt.semilogy(uniq_deg, normalized_deg_dist, 'o-', label='Raw Data')
#         plt.semilogy(uniq_deg, [A * np.exp(B *x) for x in uniq_deg], 'o-', label='Fit')
#         
#         ax.set_xlabel('Degree' ) 
#         ax.set_ylabel('1-CDF degree') 
#         ax.legend(loc='best')
#         ax.set_title(f'Degree distribution in {city}')
#         plt.legend(loc='best')
#         plt.tight_layout()
#         plt.show()
#         
#         
#     Bsc = []     
#     for j, city in enumerate(cities):   
#         network_measures = []	
#         with open(f'../Results/cspace/{city}.json', 'r') as f:	
#             s = f.read()	
#             s = s.replace('\'','\"')	
#             data = json.loads(s)          	
#             network_measures.append(data) 	
# 
#         uniq_deg, normalized_deg_dist = ccdf(network_measures[0]['Degree distribution'])
#    
# 
#         fig = plt.figure() 
#         ax = fig.add_subplot(111)
#         (A, B) = fit_exp(uniq_deg, normalized_deg_dist)
#         Bsc.append(B)
#         plt.plot(uniq_deg, normalized_deg_dist, 'o-', label='Raw Data')
#         plt.plot(uniq_deg, [A * np.exp(B *x) for x in uniq_deg], 'o-', label='Fit')
#         
#         ax.set_xlabel('Degree' ) 
#         ax.set_ylabel('1-CDF degree') 
#         ax.legend(loc='best')
#         ax.set_title(f'Degree distribution in {city}')
#         plt.legend(loc='best')
#         plt.tight_layout()
#         plt.show()
# =============================================================================
