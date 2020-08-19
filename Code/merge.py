import json 
import glob


if __name__ == '__main__':
    cities =['adelaide', 'antofagasta', 'athens', 'belfast', 'berlin', 'bordeaux', 'brisbane', 'canberra',
              'detroit', 'dublin', 'grenoble', 'helsinki', 'kuopio', 'lisbon', 'luxembourg', 'melbourne',
              'nantes', 'palermo', 'paris', 'prague', 'rennes', 'rome', 'sydney', 'toulouse', 'turku',
              'venice', 'winnipeg']
    for city in cities:       
        glob_data = []
        for file in glob.glob(f"../Results/random/lspace_triton/{city}/*.json"):
            with open(file) as json_file:
                s = json_file.read()
                s = s.strip("'<>() ").replace('\'', '\"').replace('\'','\"')
                s = s.replace('\t','')
                s = s.replace('\n','')
                s = s.replace(',}','}')
                s = s.replace(',]',']')
                data = json.loads(s) 
                glob_data.append(data)
                
        with open(f'../Results/random/lspace/{city}.json', 'w') as f:
            json.dump(glob_data, f)

