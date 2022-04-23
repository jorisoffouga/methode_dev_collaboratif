# __author__ = "Dylan Orto"
#
# """----------------------------------------------------------"""

from trucks_opti import Truck
import io
from contextlib import redirect_stdout
from crystal_truck import game

# Ecriture de la map choisit
# Avec les informations liées dans le fichier designée
def write_map(seed, filename):
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(seed)
    out = f.getvalue()
    with open(filename, "w", encoding="utf-8") as file:
        file.write(out)
        file.close()


# Recupereration des information de la map
# Nombre de camion, longueur et largeur de la map
def recuperation_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()[0:3]
        file.close()
    return data


# Nombre de camion
def nombre_de_camion(data):
    camion = data[0].split(" ")
    nombre_camion = int(camion[1])
    return nombre_camion


# Largeur de la map
def width_map(data):
    width = data[1].split(" ")
    number_width = int(width[1])
    return number_width


# hauteur de la map
def height_map(data):
    height = data[2].split(" ")
    nombre_hauteur = int(height[1])
    return nombre_hauteur


# Recupération de la map dans le fichier
def mapping(filename, number_height):
    with open(filename, "r", encoding="utf-8") as file:
        map = file.readlines()[5 : (5 + int(number_height))]
        file.close()
    return map


# Création d'un dictionnaire avec toute les coordonnées des crystaux
# Ainsi que le nombre de crystaux a l'emplacement
def matrice_de_la_map(map, number_width):
    matrice_map = []
    for y in range(len(map)):
        x = 0
        if not y % 2:
            for char in map[y]:
                if x <= int(number_width):
                    if char == "1":
                        matrice_map.append({"x": x, "y": y, "dig": 1})
                    elif char == "2":
                        matrice_map.append({"x": x, "y": y, "dig": 2})
                    else:
                        pass

                x += 1
        else:
            reversed_string = "".join(reversed(map[y]))
            x = int(number_width)

            for char in reversed_string:
                if x < int(number_width):
                    if char == "1":
                        matrice_map.append({"x": x, "y": y, "dig": 1})
                    elif char == "2":
                        matrice_map.append({"x": x, "y": y, "dig": 2})
                    else:
                        pass
                x -= 1
    return matrice_map


# Création de la liste de de camion
def list_truck(number_trucks):
    truck = []
    for number in range(int(number_trucks)):
        truck.append(Truck(number, {"x": 0, "y": number}))
    return truck


# Créarion des trajets optimisé
def trajet(matrice_map, truck):
    result = []
    while len(matrice_map) > 0:
        index = 0
        tour = 1000
        i = 0
        for camion in truck:
            if camion.nombre_turn() < tour:
                tour = camion.nombre_turn()
                index = i

            i += 1
        if matrice_map:
            plus_proche = truck[index].recherche_du_plus_proche(matrice_map)
            # print(plus_proche)
            result.append(truck[index].move(matrice_map[plus_proche]))
            del matrice_map[plus_proche]
        else:
            break

    return result


# Ecriture du trajet dans le fichier
def ecriture_trajet(filename, trajet):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("".join(trajet))
        file.close()
