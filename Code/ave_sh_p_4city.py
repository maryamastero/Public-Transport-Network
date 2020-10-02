import matplotlib.pyplot as plt
import json
import numpy as np
import seaborn as sns

#%% List of 27 cities
def get_list_cities_names():
    cities = ['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    return cities



#%%
if __name__ == '__main__':     
    mean_ave_shortest_path_random =[]
    cities = [ 'kuopio','berlin','paris', 'sydney']
    fig,ax = plt.subplots(2, 2,figsize=(10,8))
    ax = ax.flatten()
    for i, city in enumerate(cities): 
        network_measures_random = []
        with open(f'../Results/random/lspace/{city}.json', 'r') as f:
            s = f.read()
            s = s.replace('\'','\"')
            data = json.loads(s)          
            network_measures_random.append(data)    
        
        network_measures = []	
        with open(f'../Results/lspace/{city}.json', 'r') as f:	
            s = f.read()	
            s = s.replace('\'','\"')	
            data = json.loads(s)          	
            network_measures.append(data) 	
     	
        ave_shortest_path_real = float(network_measures[0]['Average shortest path'])
        
        
        ave_shortest_path_random = []
        
        for j in range(len(network_measures_random[0])):
            
            ave_shortest_path_random.append(float(network_measures_random[0][j]['Average shortest path']))
          
       
        mean_ave_shortest_path_random.append(float("%.2f"% np.mean(ave_shortest_path_random)))
        
        
        if i != 1:
            sns.kdeplot(ave_shortest_path_random, ax = ax[i])	
            ax[i].plot(ave_shortest_path_real,0, 'r*', markersize =10)
            
           
            
        elif i == 1:
            sns.kdeplot(ave_shortest_path_random, ax = ax[1], label = 'Average shortest path lengh\n  from configuration model')	
            ax[1].plot(ave_shortest_path_real,0, 'r*', markersize =10, label = 'Real value of\n Average shortest path lengh')	
            ax[1].legend(bbox_to_anchor=(0.275, 1.30), loc='upper left', borderaxespad=0., fancybox=True)
            
        #plt.setp(ax, yticks=[])
        ax[2].set_xlabel(f'Average shortest path length')
        ax[0].set_ylabel('Distribution of \n average shortest path length') 
        ax[3].set_xlabel(f'Average shortest path length')
        ax[2].set_ylabel('Distribution of \n average shortest path length') 
        ax[0].text(9.5, 2.35, 'Kuopio', fontsize=20)
        ax[1].text(11.85, 12, 'Berlin', fontsize=20)
        ax[2].text(40, 4.25,'Paris', fontsize=20)
        ax[3].text(28, 4.5, 'Sydney', fontsize=20)
        
      
      
        # =============================================================================
#         st = fig.suptitle("Average shortest path distribution from 100 configuration models \n and the real value in Lspace", fontsize="x-large", verticalalignment = 'baseline')
#         st.set_y(1.0)
# =============================================================================
        #plt.tight_layout()
        plt.savefig(f"../Results/graph/4citiesavspl.eps", format='eps')   

        #plt.show()
    