# __author__ = "Dylan Orto"
#
# """----------------------------------------------------------"""

from trucks_opti import Truck


# test class Truck
def test_recherche_plus_proche_1():
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 2


def test_recherche_plus_proche_2():
    truck_01 = Truck(0, {"x": 5, "y": 1})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 1


def test_recherche_plus_proche_3():
    truck_01 = Truck(0, {"x": 8, "y": 9})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 0


def test_nombre_deplacement_1():
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.nombre_tour_deplacement(matrice_test[0]) == 20


def test_nombre_deplacement_2():
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.nombre_tour_deplacement(matrice_test[1]) == 5


def test_nombre_deplacement_3():
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    assert truck_01.nombre_tour_deplacement(matrice_test[2]) == 1


def test_move_1():
    result = ""
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    result += (
        f"0 MOVE 0 1 0\n"
        f"1 MOVE 0 2 0\n"
        f"2 MOVE 0 3 0\n"
        f"3 MOVE 0 4 0\n"
        f"4 MOVE 0 5 0\n"
        f"5 MOVE 0 6 0\n"
        f"6 MOVE 0 7 0\n"
        f"7 MOVE 0 8 0\n"
        f"8 MOVE 0 9 0\n"
        f"9 MOVE 0 10 0\n"
        f"10 MOVE 0 10 1\n"
        f"11 MOVE 0 10 2\n12 MOVE 0 10 3"
        f"\n13 MOVE 0 10 4\n14 MOVE 0 10 5\n"
        f"15 MOVE 0 10 6\n16 MOVE 0 10 7\n17 MOVE 0 10 8"
        f"\n18 MOVE 0 10 9\n19 MOVE 0 10 10\n"
        f"20 DIG 0 10 10\n"
    )
    assert truck_01.move(matrice_test[0]) == result


def test_move_2():
    result = ""
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    result += f"0 MOVE 0 1 0\n1 MOVE 0 2 0\n2 MOVE 0 3 0\n3 MOVE 0 4 0\n4 MOVE 0 5 0\n"
    result += f"5 DIG 0 5 0\n6 DIG 0 5 0\n"
    assert truck_01.move(matrice_test[1]) == result


def test_move_3():
    result = ""
    truck_01 = Truck(0, {"x": 0, "y": 0})
    matrice_test = [
        {"x": 10, "y": 10, "dig": 1},
        {"x": 5, "y": 0, "dig": 2},
        {"x": 1, "y": 0, "dig": 0},
    ]
    result += f"0 MOVE 0 1 0\n"
    assert truck_01.move(matrice_test[2]) == result
