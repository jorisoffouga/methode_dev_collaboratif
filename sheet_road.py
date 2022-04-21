from crystal_trucks import game
import io
import sys
from contextlib import redirect_stdout


def write_map(seed):
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(seed)
    out = f.getvalue()
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(out)


write_map(4)

with open("sample.txt", "r", encoding="utf-8") as file:
    data = file.readlines()[0:3]

    trucks = data[0].split(" ")
    number_trucks = trucks[1]

    width = data[1].split(" ")
    number_width = width[1]

    height = data[2].split(" ")
    number_height = height[1]

with open("sample.txt", "r", encoding="utf-8") as file:
    map = file.readlines()[5:(5+int(number_height))]
print(map)
# map.reverse()
# print(map)
# for elem in map:
#     for char in elem:
#         print(char)

with open("sample.txt", "a", encoding="utf-8") as file:
    turn = 0
    for y in range(len(map)):
        x = 0
        if not y % 2:
            for char in map[y]:
                if x < int(number_width):
                    if char == "1":
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        file.write(mouvement)
                        turn += 1
                    elif char == "2":
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        turn +=1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        file.write(mouvement)
                        turn += 1
                    else:
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        file.write(mouvement)

                x += 1
        else:
            reversed_string = ''.join(reversed(map[y]))
            x = int(number_width)

            for char in reversed_string:
                if x < int(number_width):
                    if char == "1":
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        file.write(mouvement)
                        turn += 1
                    elif char == "2":
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        turn += 1
                        mouvement += f"{turn} DIG 0 {x} {y}\n"
                        file.write(mouvement)
                        turn += 1
                    else:
                        mouvement = f"{turn} MOVE 0 {x} {y}\n"
                        turn += 1
                        file.write(mouvement)
                        # pass
                x -= 1
