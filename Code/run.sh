#!/bin/bash 
 cities=('kuopio''nantes') 
 for city in 'kuopio' 'nantes'
 do
	for i in {1..5..1}
	do
                 echo "$city" " $i"
		python3 random_lspace.py  "$city" > ../Results/random/lspace/"$city"/"city"_"$i".json
	done 
done
