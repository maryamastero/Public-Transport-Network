import json 
import glob



if __name__ == '__main__':
    glob_data = []
    for file in glob.glob('../Results/pspace/*.json'):
        with open(file) as json_file:
            data = json.load(json_file)
            glob_data.append(data)
            
    with open('../Results/network_measures_pspace.json', 'w') as f:
        json.dump(glob_data, f)
            