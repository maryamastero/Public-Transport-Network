import numpy as np
import json
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer
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
    
def power_law(k, gamma,k0, c): 
    return k0 * np.power(k,-gamma) +c
#%%
def exponentional(k, alpha, k0, c):
    return k0 * np.exp(k *-alpha) + c 
#%%
def fit_powerlaw(xs, ys):
    S_lnx_lny = 0.0
    S_lnx_S_lny = 0.0
    S_lny = 0.0
    S_lnx = 0.0
    S_lnx2 = 0.0
    ln_x_S = 0.0
    n = len(xs)
    for (x,y) in zip(xs, ys):
        S_lnx += np.log(x)
        S_lny += np.log(y)
        S_lnx_lny += np.log(x) * np.log(y)
        S_lnx_S_lny = S_lnx *S_lny
        S_lnx2 += np.power(np.log(x),2)
        ln_x_S = np.power(S_lnx,2)
    #end
    b = (n * S_lnx_lny - S_lnx_S_lny ) / (n * S_lnx2 - ln_x_S)
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
   
    cities =  ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
      'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
      'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
      'venice', 'winnipeg']
    Bs = []  
    for j, city in enumerate(cities):   
        network_measures = []	
        with open(f'../Results/lspace/{city}.json', 'r') as f:	
            s = f.read()	
            s = s.replace('\'','\"')	
            data = json.loads(s)          	
            network_measures.append(data) 	

        uniq_deg, normalized_deg_dist = ccdf(network_measures[0]['Degree distribution'])


       # popt, pcov = curve_fit(exponentional, uniq_deg, normalized_deg_dist,p0= [1,0.0001,1],maxfev = 6000)
   

        fig = plt.figure() 
        ax = fig.add_subplot(111)
        (A, B) = fit_exp(uniq_deg, normalized_deg_dist)
        (A, B) = fit_powerlaw(uniq_deg, normalized_deg_dist)
        plt.plot(uniq_deg, normalized_deg_dist, 'o-', label='Raw Data')
        plt.plot(uniq_deg, [A * np.exp(B *x) for x in uniq_deg], 'o-', label='Fit')
        
        ax.set_xlabel('Degree' ) 
        ax.set_ylabel('1-CDF degree') 
        ax.legend(loc='best')
        ax.set_title(f'Degree distribution in {city}')
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()
# =============================================================================
#         plt.figure()
#         plt.semilogy(uniq_deg, normalized_deg_dist, 'o-', label='Raw Data')
#         plt.semilogy(uniq_deg, [A * np.exp(B *x) for x in uniq_deg], 'o-', label='Fit')
#         ax.set_xlabel('Degree' ) 
#         ax.set_ylabel('1-CDF degree') 
#         ax.legend(loc='best')
#         ax.set_title(f'Degree distribution in {city}')
#         plt.tight_layout()
# 
#         plt.show()
# =============================================================================
        
        Bs.append(B)