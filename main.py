import sys

import roadmap

number_map = int(sys.argv[1])
sample = str(sys.argv[2])

# """------------------------------Main----------------------------"""

roadmap.write_map(number_map, sample)

# definition des données de la map
data = roadmap.recuperation_data(sample)
number_trucks = roadmap.nombre_de_camion(data)
number_width = roadmap.width_map(data)
number_height = roadmap.height_map(data)

# definition de la map
map = roadmap.mapping(sample,number_height)

# matrice de donnée
matrice_map = roadmap.matrice_de_la_map(map,number_width)
print(matrice_map)

# liste de camion
truck = roadmap.list_truck(number_trucks)


# création des trajets
result = roadmap.trajet(matrice_map,truck)

print(result)

# ecriture du trajet
roadmap.ecriture_trajet(sample, result)

