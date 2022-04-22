# __author__ = "Dylan Orto"
#
# """----------------------------------------------------------"""

import roadmap
from trucks_opti import Truck
import filecmp

# def inc(x):
#     return x + 1
# def test_answer():
#     assert inc(10) == 11



# test class Truck
def test_recherche_plus_proche_1():
    truck_01 = Truck(0,{'x':0,'y':0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 2


def test_recherche_plus_proche_2():
    truck_01 = Truck(0, {'x': 5, 'y': 1})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 1


def test_recherche_plus_proche_3():
    truck_01 = Truck(0, {'x': 8, 'y': 9})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.recherche_du_plus_proche(matrice_test) == 0


def test_nombre_deplacement_1():
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.nombre_tour_deplacement(matrice_test[0]) == 20


def test_nombre_deplacement_2():
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.nombre_tour_deplacement(matrice_test[1]) == 5


def test_nombre_deplacement_3():
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    assert truck_01.nombre_tour_deplacement(matrice_test[2]) == 1


def test_move_1():
    result = ""
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    result += f"0 MOVE 0 1 0\n1 MOVE 0 2 0\n2 MOVE 0 3 0\n3 MOVE 0 4 0\n4 MOVE 0 5 0\n"
    result += f"5 MOVE 0 6 0\n6 MOVE 0 7 0\n7 MOVE 0 8 0\n8 MOVE 0 9 0\n9 MOVE 0 10 0\n"
    result += f"10 MOVE 0 10 1\n11 MOVE 0 10 2\n12 MOVE 0 10 3\n13 MOVE 0 10 4\n14 MOVE 0 10 5\n"
    result += f"15 MOVE 0 10 6\n16 MOVE 0 10 7\n17 MOVE 0 10 8\n18 MOVE 0 10 9\n19 MOVE 0 10 10\n"
    result += f"20 DIG 0 10 10\n"
    assert truck_01.move(matrice_test[0]) == result


def test_move_2():
    result = ""
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    result += f"0 MOVE 0 1 0\n1 MOVE 0 2 0\n2 MOVE 0 3 0\n3 MOVE 0 4 0\n4 MOVE 0 5 0\n"
    result += f"5 DIG 0 5 0\n6 DIG 0 5 0\n"
    assert truck_01.move(matrice_test[1]) == result


def test_move_3():
    result = ""
    truck_01 = Truck(0, {'x': 0, 'y': 0})
    matrice_test = [{'x':10,'y':10, 'dig': 1},{'x':5,'y':0, 'dig': 2},{'x':1,'y':0, 'dig': 0}]
    result += f"0 MOVE 0 1 0\n"
    assert truck_01.move(matrice_test[2]) == result


# test roadmap map 1
def test_write_map_1():
    roadmap.write_map(1,"test_sample_1.txt")
    assert filecmp.cmp("test_map_1.txt", "test_sample_1.txt") == True


def test_recuperation_data_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    data_02 = ["trucks: 7\n", "width: 25\n", "height: 14\n"]
    assert date_01 == data_02


def test_nb_camion_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    assert roadmap.nombre_de_camion(date_01) == 7


def test_nb_hauteur_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    assert roadmap.height_map(date_01) == 14


def test_nb_largeur_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    assert roadmap.width_map(date_01) == 25


def test_map_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    result= [   '1  2 12 111 11 2 2 21   1\n',
                '1 212   2   1    12  2221\n',
                '2  2     1 2 11  11     1\n',
                '    11222 2     2   1   1\n',
                ' 211  22    22   1  2 21 \n',
                '  21 222 1  2 1    12  1 \n',
                '    1 1    2  2    1   2 \n',
                ' 2        22     1111    \n',
                '      2   1  2 12    2 1 \n',
                ' 11    12   2122212   12 \n',
                '      22 2   1  1    12 1\n',
                '  122  2       2 11  1   \n',
                ' 12   11     22 11    12 \n',
                '  21 1  2 12  2    112  2\n']
    assert roadmap.mapping("test_map_1.txt",roadmap.height_map(date_01)) == result


def test_matrice_map_1():
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    map_01 = roadmap.mapping("test_map_1.txt",roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    result = [{'x': 0, 'y': 0, 'dig': 1}, {'x': 3, 'y': 0, 'dig': 2}, {'x': 5, 'y': 0, 'dig': 1},
              {'x': 6, 'y': 0, 'dig': 2}, {'x': 8, 'y': 0, 'dig': 1}, {'x': 9, 'y': 0, 'dig': 1},
              {'x': 10, 'y': 0, 'dig': 1}, {'x': 12, 'y': 0, 'dig': 1}, {'x': 13, 'y': 0, 'dig': 1},
              {'x': 15, 'y': 0, 'dig': 2}, {'x': 17, 'y': 0, 'dig': 2}, {'x': 19, 'y': 0, 'dig': 2},
              {'x': 20, 'y': 0, 'dig': 1}, {'x': 24, 'y': 0, 'dig': 1}, {'x': 24, 'y': 1, 'dig': 1},
              {'x': 23, 'y': 1, 'dig': 2}, {'x': 22, 'y': 1, 'dig': 2}, {'x': 21, 'y': 1, 'dig': 2},
              {'x': 18, 'y': 1, 'dig': 2}, {'x': 17, 'y': 1, 'dig': 1}, {'x': 12, 'y': 1, 'dig': 1},
              {'x': 8, 'y': 1, 'dig': 2}, {'x': 4, 'y': 1, 'dig': 2}, {'x': 3, 'y': 1, 'dig': 1},
              {'x': 2, 'y': 1, 'dig': 2}, {'x': 0, 'y': 1, 'dig': 1}, {'x': 0, 'y': 2, 'dig': 2},
              {'x': 3, 'y': 2, 'dig': 2}, {'x': 9, 'y': 2, 'dig': 1}, {'x': 11, 'y': 2, 'dig': 2},
              {'x': 13, 'y': 2, 'dig': 1}, {'x': 14, 'y': 2, 'dig': 1}, {'x': 17, 'y': 2, 'dig': 1},
              {'x': 18, 'y': 2, 'dig': 1}, {'x': 24, 'y': 2, 'dig': 1}, {'x': 24, 'y': 3, 'dig': 1},
              {'x': 20, 'y': 3, 'dig': 1}, {'x': 16, 'y': 3, 'dig': 2}, {'x': 10, 'y': 3, 'dig': 2},
              {'x': 8, 'y': 3, 'dig': 2}, {'x': 7, 'y': 3, 'dig': 2}, {'x': 6, 'y': 3, 'dig': 2},
              {'x': 5, 'y': 3, 'dig': 1}, {'x': 4, 'y': 3, 'dig': 1}, {'x': 1, 'y': 4, 'dig': 2},
              {'x': 2, 'y': 4, 'dig': 1}, {'x': 3, 'y': 4, 'dig': 1}, {'x': 6, 'y': 4, 'dig': 2},
              {'x': 7, 'y': 4, 'dig': 2}, {'x': 12, 'y': 4, 'dig': 2}, {'x': 13, 'y': 4, 'dig': 2},
              {'x': 17, 'y': 4, 'dig': 1}, {'x': 20, 'y': 4, 'dig': 2}, {'x': 22, 'y': 4, 'dig': 2},
              {'x': 23, 'y': 4, 'dig': 1}, {'x': 23, 'y': 5, 'dig': 1}, {'x': 20, 'y': 5, 'dig': 2},
              {'x': 19, 'y': 5, 'dig': 1}, {'x': 14, 'y': 5, 'dig': 1}, {'x': 12, 'y': 5, 'dig': 2},
              {'x': 9, 'y': 5, 'dig': 1}, {'x': 7, 'y': 5, 'dig': 2}, {'x': 6, 'y': 5, 'dig': 2},
              {'x': 5, 'y': 5, 'dig': 2}, {'x': 3, 'y': 5, 'dig': 1}, {'x': 2, 'y': 5, 'dig': 2},
              {'x': 4, 'y': 6, 'dig': 1}, {'x': 6, 'y': 6, 'dig': 1}, {'x': 11, 'y': 6, 'dig': 2},
              {'x': 14, 'y': 6, 'dig': 2}, {'x': 19, 'y': 6, 'dig': 1}, {'x': 23, 'y': 6, 'dig': 2},
              {'x': 20, 'y': 7, 'dig': 1}, {'x': 19, 'y': 7, 'dig': 1}, {'x': 18, 'y': 7, 'dig': 1},
              {'x': 17, 'y': 7, 'dig': 1}, {'x': 11, 'y': 7, 'dig': 2}, {'x': 10, 'y': 7, 'dig': 2},
              {'x': 1, 'y': 7, 'dig': 2}, {'x': 6, 'y': 8, 'dig': 2}, {'x': 10, 'y': 8, 'dig': 1},
              {'x': 13, 'y': 8, 'dig': 2}, {'x': 15, 'y': 8, 'dig': 1}, {'x': 16, 'y': 8, 'dig': 2},
              {'x': 21, 'y': 8, 'dig': 2}, {'x': 23, 'y': 8, 'dig': 1}, {'x': 23, 'y': 9, 'dig': 2},
              {'x': 22, 'y': 9, 'dig': 1}, {'x': 18, 'y': 9, 'dig': 2}, {'x': 17, 'y': 9, 'dig': 1},
              {'x': 16, 'y': 9, 'dig': 2}, {'x': 15, 'y': 9, 'dig': 2}, {'x': 14, 'y': 9, 'dig': 2},
              {'x': 13, 'y': 9, 'dig': 1}, {'x': 12, 'y': 9, 'dig': 2}, {'x': 8, 'y': 9, 'dig': 2},
              {'x': 7, 'y': 9, 'dig': 1}, {'x': 2, 'y': 9, 'dig': 1}, {'x': 1, 'y': 9, 'dig': 1},
              {'x': 6, 'y': 10, 'dig': 2}, {'x': 7, 'y': 10, 'dig': 2}, {'x': 9, 'y': 10, 'dig': 2},
              {'x': 13, 'y': 10, 'dig': 1}, {'x': 16, 'y': 10, 'dig': 1}, {'x': 21, 'y': 10, 'dig': 1},
              {'x': 22, 'y': 10, 'dig': 2}, {'x': 24, 'y': 10, 'dig': 1}, {'x': 21, 'y': 11, 'dig': 1},
              {'x': 18, 'y': 11, 'dig': 1}, {'x': 17, 'y': 11, 'dig': 1}, {'x': 15, 'y': 11, 'dig': 2},
              {'x': 7, 'y': 11, 'dig': 2}, {'x': 4, 'y': 11, 'dig': 2}, {'x': 3, 'y': 11, 'dig': 2},
              {'x': 2, 'y': 11, 'dig': 1}, {'x': 1, 'y': 12, 'dig': 1}, {'x': 2, 'y': 12, 'dig': 2},
              {'x': 6, 'y': 12, 'dig': 1}, {'x': 7, 'y': 12, 'dig': 1}, {'x': 13, 'y': 12, 'dig': 2},
              {'x': 14, 'y': 12, 'dig': 2}, {'x': 16, 'y': 12, 'dig': 1}, {'x': 17, 'y': 12, 'dig': 1},
              {'x': 22, 'y': 12, 'dig': 1}, {'x': 23, 'y': 12, 'dig': 2}, {'x': 24, 'y': 13, 'dig': 2},
              {'x': 21, 'y': 13, 'dig': 2}, {'x': 20, 'y': 13, 'dig': 1}, {'x': 19, 'y': 13, 'dig': 1},
              {'x': 14, 'y': 13, 'dig': 2}, {'x': 11, 'y': 13, 'dig': 2}, {'x': 10, 'y': 13, 'dig': 1},
              {'x': 8, 'y': 13, 'dig': 2}, {'x': 5, 'y': 13, 'dig': 1}, {'x': 3, 'y': 13, 'dig': 1},
              {'x': 2, 'y': 13, 'dig': 2}]
    matrice_map_01 = roadmap.matrice_de_la_map(map_01,width)
    assert matrice_map_01 == result


def test_trajet_map_1():
    result = ['0 DIG 0 0 0\n', '0 DIG 1 0 1\n', '0 DIG 2 0 2\n1 DIG 2 0 2\n', '0 MOVE 3 1 3\n1 MOVE 3 1 4\n2 DIG 3 1 4\n3 DIG 3 1 4\n', '0 MOVE 4 1 4\n1 MOVE 4 2 4\n2 DIG 4 2 4\n', '0 MOVE 5 1 5\n1 MOVE 5 2 5\n2 DIG 5 2 5\n3 DIG 5 2 5\n', '0 MOVE 6 1 6\n1 MOVE 6 1 7\n2 DIG 6 1 7\n3 DIG 6 1 7\n', '1 MOVE 0 1 0\n2 MOVE 0 2 0\n3 MOVE 0 3 0\n4 DIG 0 3 0\n5 DIG 0 3 0\n', '1 MOVE 1 1 1\n2 MOVE 1 2 1\n3 DIG 1 2 1\n4 DIG 1 2 1\n', '2 MOVE 2 1 2\n3 MOVE 2 2 2\n4 MOVE 2 3 2\n5 DIG 2 3 2\n6 DIG 2 3 2\n', '3 MOVE 4 3 4\n4 DIG 4 3 4\n', '4 MOVE 3 2 4\n5 MOVE 3 3 4\n6 MOVE 3 3 5\n7 DIG 3 3 5\n', '4 MOVE 5 3 5\n5 MOVE 5 4 5\n6 MOVE 5 5 5\n7 DIG 5 5 5\n8 DIG 5 5 5\n', '4 MOVE 6 1 8\n5 MOVE 6 1 9\n6 DIG 6 1 9\n', '5 MOVE 1 3 1\n6 DIG 1 3 1\n', '5 MOVE 4 4 4\n6 MOVE 4 4 3\n7 DIG 4 4 3\n', '6 MOVE 0 4 0\n7 MOVE 0 5 0\n8 DIG 0 5 0\n', '7 MOVE 1 4 1\n8 DIG 1 4 1\n9 DIG 1 4 1\n', '7 MOVE 2 4 2\n8 MOVE 2 5 2\n9 MOVE 2 5 3\n10 DIG 2 5 3\n', '7 MOVE 6 2 9\n8 DIG 6 2 9\n', '8 MOVE 3 4 5\n9 MOVE 3 4 6\n10 DIG 3 4 6\n', '8 MOVE 4 5 3\n9 MOVE 4 6 3\n10 DIG 4 6 3\n11 DIG 4 6 3\n', '9 MOVE 0 6 0\n10 DIG 0 6 0\n11 DIG 0 6 0\n', '9 MOVE 5 6 5\n10 DIG 5 6 5\n11 DIG 5 6 5\n', '9 MOVE 6 2 10\n10 MOVE 6 2 11\n11 DIG 6 2 11\n', '10 MOVE 1 5 1\n11 MOVE 1 6 1\n12 MOVE 1 7 1\n13 MOVE 1 8 1\n14 DIG 1 8 1\n15 DIG 1 8 1\n', '11 MOVE 2 6 3\n12 MOVE 2 7 3\n13 DIG 2 7 3\n14 DIG 2 7 3\n', '11 MOVE 3 5 6\n12 MOVE 3 6 6\n13 DIG 3 6 6\n', '12 MOVE 0 7 0\n13 MOVE 0 8 0\n14 DIG 0 8 0\n', '12 MOVE 4 6 4\n13 DIG 4 6 4\n14 DIG 4 6 4\n', '12 MOVE 5 7 5\n13 DIG 5 7 5\n14 DIG 5 7 5\n', '12 MOVE 6 3 11\n13 DIG 6 3 11\n14 DIG 6 3 11\n', '14 MOVE 3 6 7\n15 MOVE 3 6 8\n16 DIG 3 6 8\n17 DIG 3 6 8\n', '15 MOVE 0 9 0\n16 DIG 0 9 0\n', '15 MOVE 2 8 3\n16 DIG 2 8 3\n17 DIG 2 8 3\n', '15 MOVE 4 7 4\n16 DIG 4 7 4\n17 DIG 4 7 4\n', '15 MOVE 5 8 5\n16 MOVE 5 9 5\n17 DIG 5 9 5\n', '15 MOVE 6 4 11\n16 DIG 6 4 11\n17 DIG 6 4 11\n', '16 MOVE 1 9 1\n17 MOVE 1 9 2\n18 DIG 1 9 2\n', '17 MOVE 0 10 0\n18 DIG 0 10 0\n', '18 MOVE 2 9 3\n19 MOVE 2 10 3\n20 DIG 2 10 3\n21 DIG 2 10 3\n', '18 MOVE 3 7 8\n19 MOVE 3 7 9\n20 DIG 3 7 9\n', '18 MOVE 4 8 4\n19 MOVE 4 9 4\n20 MOVE 4 10 4\n21 MOVE 4 11 4\n22 MOVE 4 12 4\n23 DIG 4 12 4\n24 DIG 4 12 4\n', '18 MOVE 5 10 5\n19 MOVE 5 11 5\n20 MOVE 5 12 5\n21 DIG 5 12 5\n22 DIG 5 12 5\n', '18 MOVE 6 5 11\n19 MOVE 6 6 11\n20 MOVE 6 6 10\n21 DIG 6 6 10\n22 DIG 6 6 10\n', '19 MOVE 0 11 0\n20 MOVE 0 12 0\n21 DIG 0 12 0\n', '19 MOVE 1 10 2\n20 MOVE 1 11 2\n21 DIG 1 11 2\n22 DIG 1 11 2\n', '21 MOVE 3 8 9\n22 DIG 3 8 9\n23 DIG 3 8 9\n', '22 MOVE 0 13 0\n23 DIG 0 13 0\n', '22 MOVE 2 11 3\n23 MOVE 2 12 3\n24 MOVE 2 12 2\n25 MOVE 2 12 1\n26 DIG 2 12 1\n', '23 MOVE 1 12 2\n24 MOVE 1 13 2\n25 DIG 1 13 2\n', '23 MOVE 5 13 5\n24 MOVE 5 13 4\n25 DIG 5 13 4\n26 DIG 5 13 4\n', '23 MOVE 6 7 10\n24 DIG 6 7 10\n25 DIG 6 7 10\n', '24 MOVE 0 14 0\n25 MOVE 0 15 0\n26 DIG 0 15 0\n27 DIG 0 15 0\n', '24 MOVE 3 9 9\n25 MOVE 3 9 10\n26 DIG 3 9 10\n27 DIG 3 9 10\n', '25 MOVE 4 13 4\n26 MOVE 4 14 4\n27 MOVE 4 14 5\n28 DIG 4 14 5\n', '26 MOVE 1 14 2\n27 DIG 1 14 2\n', '26 MOVE 6 7 11\n27 DIG 6 7 11\n28 DIG 6 7 11\n', '27 MOVE 2 13 1\n28 MOVE 2 14 1\n29 MOVE 2 15 1\n30 MOVE 2 16 1\n31 MOVE 2 17 1\n32 DIG 2 17 1\n', '27 MOVE 5 14 4\n28 MOVE 5 14 5\n29 MOVE 5 14 6\n30 DIG 5 14 6\n31 DIG 5 14 6\n', '28 MOVE 0 16 0\n29 MOVE 0 17 0\n30 DIG 0 17 0\n31 DIG 0 17 0\n', '28 MOVE 1 15 2\n29 MOVE 1 16 2\n30 MOVE 1 17 2\n31 DIG 1 17 2\n', '28 MOVE 3 10 10\n29 MOVE 3 10 9\n30 MOVE 3 10 8\n31 DIG 3 10 8\n', '29 MOVE 4 15 5\n30 MOVE 4 16 5\n31 MOVE 4 16 4\n32 MOVE 4 16 3\n33 DIG 4 16 3\n34 DIG 4 16 3\n', '29 MOVE 6 7 12\n30 DIG 6 7 12\n', '31 MOVE 6 6 12\n32 DIG 6 6 12\n', '32 MOVE 0 18 0\n33 MOVE 0 19 0\n34 DIG 0 19 0\n35 DIG 0 19 0\n', '32 MOVE 1 18 2\n33 DIG 1 18 2\n', '32 MOVE 3 10 7\n33 DIG 3 10 7\n34 DIG 3 10 7\n', '32 MOVE 5 13 6\n33 MOVE 5 12 6\n34 MOVE 5 11 6\n35 DIG 5 11 6\n36 DIG 5 11 6\n', '33 MOVE 2 18 1\n34 DIG 2 18 1\n35 DIG 2 18 1\n', '33 MOVE 6 5 12\n34 MOVE 6 5 13\n35 DIG 6 5 13\n', '34 MOVE 1 19 2\n35 MOVE 1 20 2\n36 MOVE 1 20 3\n37 DIG 1 20 3\n', '35 MOVE 3 11 7\n36 DIG 3 11 7\n37 DIG 3 11 7\n', '35 MOVE 4 17 3\n36 MOVE 4 17 4\n37 DIG 4 17 4\n', '36 MOVE 0 20 0\n37 DIG 0 20 0\n', '36 MOVE 2 19 1\n37 MOVE 2 20 1\n38 MOVE 2 21 1\n39 DIG 2 21 1\n40 DIG 2 21 1\n', '36 MOVE 6 4 13\n37 MOVE 6 3 13\n38 DIG 6 3 13\n', '37 MOVE 5 12 6\n38 MOVE 5 13 6\n39 MOVE 5 13 7\n40 MOVE 5 13 8\n41 DIG 5 13 8\n42 DIG 5 13 8\n', '38 MOVE 0 21 0\n39 MOVE 0 22 0\n40 MOVE 0 22 1\n41 DIG 0 22 1\n42 DIG 0 22 1\n', '38 MOVE 1 20 4\n39 DIG 1 20 4\n40 DIG 1 20 4\n', '38 MOVE 3 12 7\n39 MOVE 3 12 8\n40 MOVE 3 12 9\n41 DIG 3 12 9\n42 DIG 3 12 9\n', '38 MOVE 4 18 4\n39 MOVE 4 19 4\n40 MOVE 4 19 5\n41 DIG 4 19 5\n', '39 MOVE 6 2 13\n40 DIG 6 2 13\n41 DIG 6 2 13\n', '41 MOVE 1 20 5\n42 DIG 1 20 5\n43 DIG 1 20 5\n', '41 MOVE 2 22 1\n42 MOVE 2 23 1\n43 DIG 2 23 1\n44 DIG 2 23 1\n', '42 MOVE 4 19 6\n43 DIG 4 19 6\n', '42 MOVE 6 2 12\n43 DIG 6 2 12\n44 DIG 6 2 12\n', '43 MOVE 0 23 1\n44 MOVE 0 24 1\n45 DIG 0 24 1\n', '43 MOVE 3 13 9\n44 DIG 3 13 9\n', '43 MOVE 5 14 8\n44 MOVE 5 15 8\n45 DIG 5 15 8\n', '44 MOVE 1 20 6\n45 MOVE 1 20 7\n46 DIG 1 20 7\n', '44 MOVE 4 19 7\n45 DIG 4 19 7\n', '45 MOVE 2 24 1\n46 MOVE 2 24 0\n47 DIG 2 24 0\n', '45 MOVE 3 14 9\n46 DIG 3 14 9\n47 DIG 3 14 9\n', '45 MOVE 6 1 12\n46 DIG 6 1 12\n', '46 MOVE 0 24 2\n47 DIG 0 24 2\n', '46 MOVE 4 18 7\n47 DIG 4 18 7\n', '46 MOVE 5 16 8\n47 DIG 5 16 8\n48 DIG 5 16 8\n', '47 MOVE 1 21 7\n48 MOVE 1 21 8\n49 DIG 1 21 8\n50 DIG 1 21 8\n', '47 MOVE 6 2 12\n48 MOVE 6 3 12\n49 MOVE 6 4 12\n50 MOVE 6 5 12\n51 MOVE 6 6 12\n52 MOVE 6 7 12\n53 MOVE 6 8 12\n54 MOVE 6 8 13\n55 DIG 6 8 13\n56 DIG 6 8 13\n', '48 MOVE 0 24 3\n49 DIG 0 24 3\n', '48 MOVE 2 23 0\n49 MOVE 2 23 1\n50 MOVE 2 23 2\n51 MOVE 2 23 3\n52 MOVE 2 23 4\n53 DIG 2 23 4\n', '48 MOVE 3 15 9\n49 DIG 3 15 9\n50 DIG 3 15 9\n', '48 MOVE 4 17 7\n49 DIG 4 17 7\n', '49 MOVE 5 16 9\n50 DIG 5 16 9\n51 DIG 5 16 9\n', '50 MOVE 0 23 3\n51 MOVE 0 22 3\n52 MOVE 0 22 4\n53 DIG 0 22 4\n54 DIG 0 22 4\n', '50 MOVE 4 17 8\n51 MOVE 4 17 9\n52 DIG 4 17 9\n', '51 MOVE 1 22 8\n52 MOVE 1 23 8\n53 DIG 1 23 8\n', '51 MOVE 3 16 9\n52 MOVE 3 16 10\n53 DIG 3 16 10\n', '52 MOVE 5 17 9\n53 MOVE 5 18 9\n54 DIG 5 18 9\n55 DIG 5 18 9\n', '53 MOVE 4 17 10\n54 MOVE 4 17 11\n55 DIG 4 17 11\n', '54 MOVE 1 23 9\n55 DIG 1 23 9\n56 DIG 1 23 9\n', '54 MOVE 2 23 5\n55 DIG 2 23 5\n', '54 MOVE 3 15 10\n55 MOVE 3 15 11\n56 DIG 3 15 11\n57 DIG 3 15 11\n', '55 MOVE 0 23 4\n56 MOVE 0 23 5\n57 MOVE 0 23 6\n58 DIG 0 23 6\n59 DIG 0 23 6\n', '56 MOVE 2 22 5\n57 MOVE 2 22 6\n58 MOVE 2 22 7\n59 MOVE 2 22 8\n60 MOVE 2 22 9\n61 DIG 2 22 9\n', '56 MOVE 4 18 11\n57 DIG 4 18 11\n', '56 MOVE 5 19 9\n57 MOVE 5 20 9\n58 MOVE 5 21 9\n59 MOVE 5 21 10\n60 DIG 5 21 10\n', '57 MOVE 1 22 9\n58 MOVE 1 22 10\n59 DIG 1 22 10\n60 DIG 1 22 10\n', '57 MOVE 6 9 13\n58 MOVE 6 10 13\n59 DIG 6 10 13\n', '58 MOVE 3 14 11\n59 MOVE 3 14 12\n60 DIG 3 14 12\n61 DIG 3 14 12\n', '58 MOVE 4 17 11\n59 MOVE 4 17 12\n60 DIG 4 17 12\n', '60 MOVE 0 24 6\n61 MOVE 0 24 7\n62 MOVE 0 24 8\n63 MOVE 0 24 9\n64 MOVE 0 24 10\n65 DIG 0 24 10\n', '60 MOVE 6 11 13\n61 DIG 6 11 13\n62 DIG 6 11 13\n', '61 MOVE 1 21 10\n62 MOVE 1 21 11\n63 DIG 1 21 11\n', '61 MOVE 4 16 12\n62 DIG 4 16 12\n', '61 MOVE 5 22 10\n62 MOVE 5 22 11\n63 MOVE 5 22 12\n64 DIG 5 22 12\n', '62 MOVE 2 23 9\n63 MOVE 2 23 10\n64 MOVE 2 23 11\n65 MOVE 2 23 12\n66 DIG 2 23 12\n67 DIG 2 23 12\n', '62 MOVE 3 13 12\n63 DIG 3 13 12\n64 DIG 3 13 12\n', '63 MOVE 4 15 12\n64 MOVE 4 14 12\n65 MOVE 4 14 13\n66 DIG 4 14 13\n67 DIG 4 14 13\n', '63 MOVE 6 12 13\n64 MOVE 6 13 13\n65 MOVE 6 13 12\n66 MOVE 6 13 11\n67 MOVE 6 13 10\n68 DIG 6 13 10\n', '64 MOVE 1 21 12\n65 MOVE 1 21 13\n66 DIG 1 21 13\n67 DIG 1 21 13\n', '65 MOVE 3 14 12\n66 MOVE 3 15 12\n67 MOVE 3 16 12\n68 MOVE 3 17 12\n69 MOVE 3 18 12\n70 MOVE 3 19 12\n71 MOVE 3 19 13\n72 DIG 3 19 13\n', '65 MOVE 5 23 12\n66 MOVE 5 24 12\n67 MOVE 5 24 13\n68 DIG 5 24 13\n69 DIG 5 24 13\n', '66 MOVE 0 23 10\n67 MOVE 0 22 10\n68 MOVE 0 21 10\n69 MOVE 0 20 10\n70 MOVE 0 20 11\n71 MOVE 0 20 12\n72 MOVE 0 20 13\n73 DIG 0 20 13\n']
    date_01 = roadmap.recuperation_data("test_map_1.txt")
    map_01 = roadmap.mapping("test_map_1.txt",roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    number_truck = roadmap.nombre_de_camion(date_01)
    truck = roadmap.list_truck(number_truck)
    trajet = roadmap.trajet(matrice_map_01,truck)
    assert result == trajet


# test roadmap map 4
def test_write_map_4():
    roadmap.write_map(4,"test_sample_4.txt")
    assert filecmp.cmp("test_map_4.txt", "test_sample_4.txt") == True


def test_recuperation_data_4():
    date_01 = roadmap.recuperation_data("test_map_4.txt")
    data_02 = ["trucks: 6\n", "width: 28\n", "height: 11\n"]
    assert date_01 == data_02


def test_nb_camion_4():
    date_01 = roadmap.recuperation_data("test_map_4.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 6


# test roadmap map 8
def test_write_map_8():
    roadmap.write_map(8,"test_sample_8.txt")
    assert filecmp.cmp("test_map_8.txt", "test_sample_8.txt") == True


def test_recuperation_data_8():
    date_01 = roadmap.recuperation_data("test_map_8.txt")
    data_02 = ["trucks: 2\n", "width: 20\n", "height: 17\n"]
    assert date_01 == data_02


def test_nb_camion_8():
    date_01 = roadmap.recuperation_data("test_map_8.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 2


# test roadmap map 12
def test_write_map_12():
    roadmap.write_map(12,"test_sample_12.txt")
    assert filecmp.cmp("test_map_12.txt", "test_sample_12.txt") == True


def test_recuperation_data_12():
    date_01 = roadmap.recuperation_data("test_map_12.txt")
    data_02 = ["trucks: 6\n", "width: 12\n", "height: 13\n"]
    assert date_01 == data_02


def test_nb_camion_12():
    date_01 = roadmap.recuperation_data("test_map_12.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 6
