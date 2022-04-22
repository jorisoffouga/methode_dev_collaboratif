import math
from trucks_opti import Truck
import io
from contextlib import redirect_stdout
import sys
from crystal_trucks import game


def write_map(seed, filename):
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(seed)
    out = f.getvalue()
    with open(filename, "w", encoding="utf-8") as file:
        file.write(out)
        file.close()


write_map(1, "test_map_1.txt")
write_map(4, "test_map_4.txt")
write_map(8, "test_map_8.txt")
write_map(12, "test_map_12.txt")