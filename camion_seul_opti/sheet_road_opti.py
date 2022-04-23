import math
from truck import Truck
from crystal_trucks import game
import io
import sys
from contextlib import redirect_stdout


def write_map(seed):
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(seed)
    out = f.getvalue()
    with open("sample_opti.txt", "w", encoding="utf-8") as file:
        file.write(out)


write_map(4)

with open("sample_opti.txt", "r", encoding="utf-8") as file:
    data = file.readlines()[0:3]

    trucks = data[0].split(" ")
    number_trucks = trucks[1]

    width = data[1].split(" ")
    number_width = width[1]

    height = data[2].split(" ")
    number_height = height[1]

with open("sample_opti.txt", "r", encoding="utf-8") as file:
    map = file.readlines()[5 : (5 + int(number_height))]

matrice_map = []
with open("sample_opti.txt", "r", encoding="utf-8") as file:
    turn = 0
    for y in range(len(map)):
        x = 0
        if not y % 2:
            for char in map[y]:
                if x < int(number_width):
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

truck_0 = Truck(0, {"x": 0, "y": 0})
result = []
while matrice_map:
    plus_proche = truck_0.recherche_du_plus_proche(matrice_map)
    result.append(truck_0.move(matrice_map[plus_proche]))
    del matrice_map[plus_proche]

with open("sample_opti.txt", "a", encoding="utf-8") as file:
    file.write("".join(result))
