#!/bin/bash
#SBATCH --job-name=random_lspace
#SBATCH --array=1-2700
#SBATCH --time=5-00:00:00
#SBATCH --mem-per-cpu=1G


module load anaconda

 for city in 'adelaide' 'antofagasta' 'athens' 'belfast' 'berlin' 'bordeaux' 'brisbane' 'canberra' 'detroit' 'dublin' 'grenoble' 'helsinki' '$
 do
        for i in {1..100..1}
        do
               srun  python3 random_lspace.py  "$city" > Results/random/lspace/"$city"/"$city"_"$i".json
        done
done

