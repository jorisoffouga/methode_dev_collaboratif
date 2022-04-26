# __author__ = "Dylan Orto"
#
# """----------------------------------------------------------"""

import roadmap
import filecmp


# test roadmap map 1
def test_write_map_1():
    roadmap.write_map(1, "test/test_sample_1.txt")
    assert filecmp.cmp("test/test_map_1.txt", "test/test_sample_1.txt") == True


def test_recuperation_data_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    data_02 = ["trucks: 7\n", "width: 25\n", "height: 14\n"]
    assert date_01 == data_02


def test_nb_camion_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    assert roadmap.nombre_de_camion(date_01) == 7


def test_nb_hauteur_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    assert roadmap.height_map(date_01) == 14


def test_nb_largeur_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    assert roadmap.width_map(date_01) == 25


def test_map_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    result = [
        "1  2 12 111 11 2 2 21   1\n",
        "1 212   2   1    12  2221\n",
        "2  2     1 2 11  11     1\n",
        "    11222 2     2   1   1\n",
        " 211  22    22   1  2 21 \n",
        "  21 222 1  2 1    12  1 \n",
        "    1 1    2  2    1   2 \n",
        " 2        22     1111    \n",
        "      2   1  2 12    2 1 \n",
        " 11    12   2122212   12 \n",
        "      22 2   1  1    12 1\n",
        "  122  2       2 11  1   \n",
        " 12   11     22 11    12 \n",
        "  21 1  2 12  2    112  2\n",
    ]
    assert roadmap.mapping("test/test_map_1.txt", roadmap.height_map(date_01)) == result


def test_matrice_map_1():
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    map_01 = roadmap.mapping("test/test_map_1.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    result = [
        {"x": 0, "y": 0, "dig": 1},
        {"x": 3, "y": 0, "dig": 2},
        {"x": 5, "y": 0, "dig": 1},
        {"x": 6, "y": 0, "dig": 2},
        {"x": 8, "y": 0, "dig": 1},
        {"x": 9, "y": 0, "dig": 1},
        {"x": 10, "y": 0, "dig": 1},
        {"x": 12, "y": 0, "dig": 1},
        {"x": 13, "y": 0, "dig": 1},
        {"x": 15, "y": 0, "dig": 2},
        {"x": 17, "y": 0, "dig": 2},
        {"x": 19, "y": 0, "dig": 2},
        {"x": 20, "y": 0, "dig": 1},
        {"x": 24, "y": 0, "dig": 1},
        {"x": 24, "y": 1, "dig": 1},
        {"x": 23, "y": 1, "dig": 2},
        {"x": 22, "y": 1, "dig": 2},
        {"x": 21, "y": 1, "dig": 2},
        {"x": 18, "y": 1, "dig": 2},
        {"x": 17, "y": 1, "dig": 1},
        {"x": 12, "y": 1, "dig": 1},
        {"x": 8, "y": 1, "dig": 2},
        {"x": 4, "y": 1, "dig": 2},
        {"x": 3, "y": 1, "dig": 1},
        {"x": 2, "y": 1, "dig": 2},
        {"x": 0, "y": 1, "dig": 1},
        {"x": 0, "y": 2, "dig": 2},
        {"x": 3, "y": 2, "dig": 2},
        {"x": 9, "y": 2, "dig": 1},
        {"x": 11, "y": 2, "dig": 2},
        {"x": 13, "y": 2, "dig": 1},
        {"x": 14, "y": 2, "dig": 1},
        {"x": 17, "y": 2, "dig": 1},
        {"x": 18, "y": 2, "dig": 1},
        {"x": 24, "y": 2, "dig": 1},
        {"x": 24, "y": 3, "dig": 1},
        {"x": 20, "y": 3, "dig": 1},
        {"x": 16, "y": 3, "dig": 2},
        {"x": 10, "y": 3, "dig": 2},
        {"x": 8, "y": 3, "dig": 2},
        {"x": 7, "y": 3, "dig": 2},
        {"x": 6, "y": 3, "dig": 2},
        {"x": 5, "y": 3, "dig": 1},
        {"x": 4, "y": 3, "dig": 1},
        {"x": 1, "y": 4, "dig": 2},
        {"x": 2, "y": 4, "dig": 1},
        {"x": 3, "y": 4, "dig": 1},
        {"x": 6, "y": 4, "dig": 2},
        {"x": 7, "y": 4, "dig": 2},
        {"x": 12, "y": 4, "dig": 2},
        {"x": 13, "y": 4, "dig": 2},
        {"x": 17, "y": 4, "dig": 1},
        {"x": 20, "y": 4, "dig": 2},
        {"x": 22, "y": 4, "dig": 2},
        {"x": 23, "y": 4, "dig": 1},
        {"x": 23, "y": 5, "dig": 1},
        {"x": 20, "y": 5, "dig": 2},
        {"x": 19, "y": 5, "dig": 1},
        {"x": 14, "y": 5, "dig": 1},
        {"x": 12, "y": 5, "dig": 2},
        {"x": 9, "y": 5, "dig": 1},
        {"x": 7, "y": 5, "dig": 2},
        {"x": 6, "y": 5, "dig": 2},
        {"x": 5, "y": 5, "dig": 2},
        {"x": 3, "y": 5, "dig": 1},
        {"x": 2, "y": 5, "dig": 2},
        {"x": 4, "y": 6, "dig": 1},
        {"x": 6, "y": 6, "dig": 1},
        {"x": 11, "y": 6, "dig": 2},
        {"x": 14, "y": 6, "dig": 2},
        {"x": 19, "y": 6, "dig": 1},
        {"x": 23, "y": 6, "dig": 2},
        {"x": 20, "y": 7, "dig": 1},
        {"x": 19, "y": 7, "dig": 1},
        {"x": 18, "y": 7, "dig": 1},
        {"x": 17, "y": 7, "dig": 1},
        {"x": 11, "y": 7, "dig": 2},
        {"x": 10, "y": 7, "dig": 2},
        {"x": 1, "y": 7, "dig": 2},
        {"x": 6, "y": 8, "dig": 2},
        {"x": 10, "y": 8, "dig": 1},
        {"x": 13, "y": 8, "dig": 2},
        {"x": 15, "y": 8, "dig": 1},
        {"x": 16, "y": 8, "dig": 2},
        {"x": 21, "y": 8, "dig": 2},
        {"x": 23, "y": 8, "dig": 1},
        {"x": 23, "y": 9, "dig": 2},
        {"x": 22, "y": 9, "dig": 1},
        {"x": 18, "y": 9, "dig": 2},
        {"x": 17, "y": 9, "dig": 1},
        {"x": 16, "y": 9, "dig": 2},
        {"x": 15, "y": 9, "dig": 2},
        {"x": 14, "y": 9, "dig": 2},
        {"x": 13, "y": 9, "dig": 1},
        {"x": 12, "y": 9, "dig": 2},
        {"x": 8, "y": 9, "dig": 2},
        {"x": 7, "y": 9, "dig": 1},
        {"x": 2, "y": 9, "dig": 1},
        {"x": 1, "y": 9, "dig": 1},
        {"x": 6, "y": 10, "dig": 2},
        {"x": 7, "y": 10, "dig": 2},
        {"x": 9, "y": 10, "dig": 2},
        {"x": 13, "y": 10, "dig": 1},
        {"x": 16, "y": 10, "dig": 1},
        {"x": 21, "y": 10, "dig": 1},
        {"x": 22, "y": 10, "dig": 2},
        {"x": 24, "y": 10, "dig": 1},
        {"x": 21, "y": 11, "dig": 1},
        {"x": 18, "y": 11, "dig": 1},
        {"x": 17, "y": 11, "dig": 1},
        {"x": 15, "y": 11, "dig": 2},
        {"x": 7, "y": 11, "dig": 2},
        {"x": 4, "y": 11, "dig": 2},
        {"x": 3, "y": 11, "dig": 2},
        {"x": 2, "y": 11, "dig": 1},
        {"x": 1, "y": 12, "dig": 1},
        {"x": 2, "y": 12, "dig": 2},
        {"x": 6, "y": 12, "dig": 1},
        {"x": 7, "y": 12, "dig": 1},
        {"x": 13, "y": 12, "dig": 2},
        {"x": 14, "y": 12, "dig": 2},
        {"x": 16, "y": 12, "dig": 1},
        {"x": 17, "y": 12, "dig": 1},
        {"x": 22, "y": 12, "dig": 1},
        {"x": 23, "y": 12, "dig": 2},
        {"x": 24, "y": 13, "dig": 2},
        {"x": 21, "y": 13, "dig": 2},
        {"x": 20, "y": 13, "dig": 1},
        {"x": 19, "y": 13, "dig": 1},
        {"x": 14, "y": 13, "dig": 2},
        {"x": 11, "y": 13, "dig": 2},
        {"x": 10, "y": 13, "dig": 1},
        {"x": 8, "y": 13, "dig": 2},
        {"x": 5, "y": 13, "dig": 1},
        {"x": 3, "y": 13, "dig": 1},
        {"x": 2, "y": 13, "dig": 2},
    ]
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    assert matrice_map_01 == result


def test_trajet_map_1():
    result = [
        "0 DIG 0 0 0\n",
        "0 DIG 1 0 1\n",
        "0 DIG 2 0 2\n1 DIG 2 0 2\n",
        "0 MOVE 3 1 3\n1 MOVE 3 1 4\n2 DIG 3 1 4\n3 DIG 3 1 4\n",
        "0 MOVE 4 1 4\n1 MOVE 4 2 4\n2 DIG 4 2 4\n",
        "0 MOVE 5 1 5\n1 MOVE 5 2 5\n2 DIG 5 2 5\n3 DIG 5 2 5\n",
        "0 MOVE 6 1 6\n1 MOVE 6 1 7\n2 DIG 6 1 7\n3 DIG 6 1 7\n",
        "1 MOVE 0 1 0\n2 MOVE 0 2 0\n3 MOVE 0 3 0\n4 DIG 0 3 0\n5 DIG 0 3 0\n",
        "1 MOVE 1 1 1\n2 MOVE 1 2 1\n3 DIG 1 2 1\n4 DIG 1 2 1\n",
        "2 MOVE 2 1 2\n3 MOVE 2 2 2\n4 MOVE 2 3 2\n5 DIG 2 3 2\n6 DIG 2 3 2\n",
        "3 MOVE 4 3 4\n4 DIG 4 3 4\n",
        "4 MOVE 3 2 4\n5 MOVE 3 3 4\n6 MOVE 3 3 5\n7 DIG 3 3 5\n",
        "4 MOVE 5 3 5\n5 MOVE 5 4 5\n6 MOVE 5 5 5\n7 DIG 5 5 5\n8 DIG 5 5 5\n",
        "4 MOVE 6 1 8\n5 MOVE 6 1 9\n6 DIG 6 1 9\n",
        "5 MOVE 1 3 1\n6 DIG 1 3 1\n",
        "5 MOVE 4 4 4\n6 MOVE 4 4 3\n7 DIG 4 4 3\n",
        "6 MOVE 0 4 0\n7 MOVE 0 5 0\n8 DIG 0 5 0\n",
        "7 MOVE 1 4 1\n8 DIG 1 4 1\n9 DIG 1 4 1\n",
        "7 MOVE 2 4 2\n8 MOVE 2 5 2\n9 MOVE 2 5 3\n10 DIG 2 5 3\n",
        "7 MOVE 6 2 9\n8 DIG 6 2 9\n",
        "8 MOVE 3 4 5\n9 MOVE 3 4 6\n10 DIG 3 4 6\n",
        "8 MOVE 4 5 3\n9 MOVE 4 6 3\n10 DIG 4 6 3\n11 DIG 4 6 3\n",
        "9 MOVE 0 6 0\n10 DIG 0 6 0\n11 DIG 0 6 0\n",
        "9 MOVE 5 6 5\n10 DIG 5 6 5\n11 DIG 5 6 5\n",
        "9 MOVE 6 2 10\n10 MOVE 6 2 11\n11 DIG 6 2 11\n",
        "10 MOVE 1 5 1\n11 MOVE 1 6 1\n12 MOVE 1 7 1\n13 MOVE 1 8 1\n14 DIG 1 8 1\n15 DIG 1 8 1\n",
        "11 MOVE 2 6 3\n12 MOVE 2 7 3\n13 DIG 2 7 3\n14 DIG 2 7 3\n",
        "11 MOVE 3 5 6\n12 MOVE 3 6 6\n13 DIG 3 6 6\n",
        "12 MOVE 0 7 0\n13 MOVE 0 8 0\n14 DIG 0 8 0\n",
        "12 MOVE 4 6 4\n13 DIG 4 6 4\n14 DIG 4 6 4\n",
        "12 MOVE 5 7 5\n13 DIG 5 7 5\n14 DIG 5 7 5\n",
        "12 MOVE 6 3 11\n13 DIG 6 3 11\n14 DIG 6 3 11\n",
        "14 MOVE 3 6 7\n15 MOVE 3 6 8\n16 DIG 3 6 8\n17 DIG 3 6 8\n",
        "15 MOVE 0 9 0\n16 DIG 0 9 0\n",
        "15 MOVE 2 8 3\n16 DIG 2 8 3\n17 DIG 2 8 3\n",
        "15 MOVE 4 7 4\n16 DIG 4 7 4\n17 DIG 4 7 4\n",
        "15 MOVE 5 8 5\n16 MOVE 5 9 5\n17 DIG 5 9 5\n",
        "15 MOVE 6 4 11\n16 DIG 6 4 11\n17 DIG 6 4 11\n",
        "16 MOVE 1 9 1\n17 MOVE 1 9 2\n18 DIG 1 9 2\n",
        "17 MOVE 0 10 0\n18 DIG 0 10 0\n",
        "18 MOVE 2 9 3\n19 MOVE 2 10 3\n20 DIG 2 10 3\n21 DIG 2 10 3\n",
        "18 MOVE 3 7 8\n19 MOVE 3 7 9\n20 DIG 3 7 9\n",
        "18 MOVE 4 8 4\n19 MOVE 4 9 4\n20 MOVE 4 10 4\n21 MOVE 4 11 4\n22 MOVE 4 12 4\n23 DIG 4 12 4\n24 DIG 4 12 4\n",
        "18 MOVE 5 10 5\n19 MOVE 5 11 5\n20 MOVE 5 12 5\n21 DIG 5 12 5\n22 DIG 5 12 5\n",
        "18 MOVE 6 5 11\n19 MOVE 6 6 11\n20 MOVE 6 6 10\n21 DIG 6 6 10\n22 DIG 6 6 10\n",
        "19 MOVE 0 11 0\n20 MOVE 0 12 0\n21 DIG 0 12 0\n",
        "19 MOVE 1 10 2\n20 MOVE 1 11 2\n21 DIG 1 11 2\n22 DIG 1 11 2\n",
        "21 MOVE 3 8 9\n22 DIG 3 8 9\n23 DIG 3 8 9\n",
        "22 MOVE 0 13 0\n23 DIG 0 13 0\n",
        "22 MOVE 2 11 3\n23 MOVE 2 12 3\n24 MOVE 2 12 2\n25 MOVE 2 12 1\n26 DIG 2 12 1\n",
        "23 MOVE 1 12 2\n24 MOVE 1 13 2\n25 DIG 1 13 2\n",
        "23 MOVE 5 13 5\n24 MOVE 5 13 4\n25 DIG 5 13 4\n26 DIG 5 13 4\n",
        "23 MOVE 6 7 10\n24 DIG 6 7 10\n25 DIG 6 7 10\n",
        "24 MOVE 0 14 0\n25 MOVE 0 15 0\n26 DIG 0 15 0\n27 DIG 0 15 0\n",
        "24 MOVE 3 9 9\n25 MOVE 3 9 10\n26 DIG 3 9 10\n27 DIG 3 9 10\n",
        "25 MOVE 4 13 4\n26 MOVE 4 14 4\n27 MOVE 4 14 5\n28 DIG 4 14 5\n",
        "26 MOVE 1 14 2\n27 DIG 1 14 2\n",
        "26 MOVE 6 7 11\n27 DIG 6 7 11\n28 DIG 6 7 11\n",
        "27 MOVE 2 13 1\n28 MOVE 2 14 1\n29 MOVE 2 15 1\n30 MOVE 2 16 1\n31 MOVE 2 17 1\n32 DIG 2 17 1\n",
        "27 MOVE 5 14 4\n28 MOVE 5 14 5\n29 MOVE 5 14 6\n30 DIG 5 14 6\n31 DIG 5 14 6\n",
        "28 MOVE 0 16 0\n29 MOVE 0 17 0\n30 DIG 0 17 0\n31 DIG 0 17 0\n",
        "28 MOVE 1 15 2\n29 MOVE 1 16 2\n30 MOVE 1 17 2\n31 DIG 1 17 2\n",
        "28 MOVE 3 10 10\n29 MOVE 3 10 9\n30 MOVE 3 10 8\n31 DIG 3 10 8\n",
        "29 MOVE 4 15 5\n30 MOVE 4 16 5\n31 MOVE 4 16 4\n32 MOVE 4 16 3\n33 DIG 4 16 3\n34 DIG 4 16 3\n",
        "29 MOVE 6 7 12\n30 DIG 6 7 12\n",
        "31 MOVE 6 6 12\n32 DIG 6 6 12\n",
        "32 MOVE 0 18 0\n33 MOVE 0 19 0\n34 DIG 0 19 0\n35 DIG 0 19 0\n",
        "32 MOVE 1 18 2\n33 DIG 1 18 2\n",
        "32 MOVE 3 10 7\n33 DIG 3 10 7\n34 DIG 3 10 7\n",
        "32 MOVE 5 13 6\n33 MOVE 5 12 6\n34 MOVE 5 11 6\n35 DIG 5 11 6\n36 DIG 5 11 6\n",
        "33 MOVE 2 18 1\n34 DIG 2 18 1\n35 DIG 2 18 1\n",
        "33 MOVE 6 5 12\n34 MOVE 6 5 13\n35 DIG 6 5 13\n",
        "34 MOVE 1 19 2\n35 MOVE 1 20 2\n36 MOVE 1 20 3\n37 DIG 1 20 3\n",
        "35 MOVE 3 11 7\n36 DIG 3 11 7\n37 DIG 3 11 7\n",
        "35 MOVE 4 17 3\n36 MOVE 4 17 4\n37 DIG 4 17 4\n",
        "36 MOVE 0 20 0\n37 DIG 0 20 0\n",
        "36 MOVE 2 19 1\n37 MOVE 2 20 1\n38 MOVE 2 21 1\n39 DIG 2 21 1\n40 DIG 2 21 1\n",
        "36 MOVE 6 4 13\n37 MOVE 6 3 13\n38 DIG 6 3 13\n",
        "37 MOVE 5 12 6\n38 MOVE 5 13 6\n39 MOVE 5 13 7\n40 MOVE 5 13 8\n41 DIG 5 13 8\n42 DIG 5 13 8\n",
        "38 MOVE 0 21 0\n39 MOVE 0 22 0\n40 MOVE 0 22 1\n41 DIG 0 22 1\n42 DIG 0 22 1\n",
        "38 MOVE 1 20 4\n39 DIG 1 20 4\n40 DIG 1 20 4\n",
        "38 MOVE 3 12 7\n39 MOVE 3 12 8\n40 MOVE 3 12 9\n41 DIG 3 12 9\n42 DIG 3 12 9\n",
        "38 MOVE 4 18 4\n39 MOVE 4 19 4\n40 MOVE 4 19 5\n41 DIG 4 19 5\n",
        "39 MOVE 6 2 13\n40 DIG 6 2 13\n41 DIG 6 2 13\n",
        "41 MOVE 1 20 5\n42 DIG 1 20 5\n43 DIG 1 20 5\n",
        "41 MOVE 2 22 1\n42 MOVE 2 23 1\n43 DIG 2 23 1\n44 DIG 2 23 1\n",
        "42 MOVE 4 19 6\n43 DIG 4 19 6\n",
        "42 MOVE 6 2 12\n43 DIG 6 2 12\n44 DIG 6 2 12\n",
        "43 MOVE 0 23 1\n44 MOVE 0 24 1\n45 DIG 0 24 1\n",
        "43 MOVE 3 13 9\n44 DIG 3 13 9\n",
        "43 MOVE 5 14 8\n44 MOVE 5 15 8\n45 DIG 5 15 8\n",
        "44 MOVE 1 20 6\n45 MOVE 1 20 7\n46 DIG 1 20 7\n",
        "44 MOVE 4 19 7\n45 DIG 4 19 7\n",
        "45 MOVE 2 24 1\n46 MOVE 2 24 0\n47 DIG 2 24 0\n",
        "45 MOVE 3 14 9\n46 DIG 3 14 9\n47 DIG 3 14 9\n",
        "45 MOVE 6 1 12\n46 DIG 6 1 12\n",
        "46 MOVE 0 24 2\n47 DIG 0 24 2\n",
        "46 MOVE 4 18 7\n47 DIG 4 18 7\n",
        "46 MOVE 5 16 8\n47 DIG 5 16 8\n48 DIG 5 16 8\n",
        "47 MOVE 1 21 7\n48 MOVE 1 21 8\n49 DIG 1 21 8\n50 DIG 1 21 8\n",
        "47 MOVE 6 2 12\n48 MOVE 6 3 12\n49 MOVE 6 4 12\n50 MOVE 6 5 12\n51 MOVE 6 6 12\n52 MOVE 6 7 12\n53 MOVE 6 8 12\n54 MOVE 6 8 13\n55 DIG 6 8 13\n56 DIG 6 8 13\n",
        "48 MOVE 0 24 3\n49 DIG 0 24 3\n",
        "48 MOVE 2 23 0\n49 MOVE 2 23 1\n50 MOVE 2 23 2\n51 MOVE 2 23 3\n52 MOVE 2 23 4\n53 DIG 2 23 4\n",
        "48 MOVE 3 15 9\n49 DIG 3 15 9\n50 DIG 3 15 9\n",
        "48 MOVE 4 17 7\n49 DIG 4 17 7\n",
        "49 MOVE 5 16 9\n50 DIG 5 16 9\n51 DIG 5 16 9\n",
        "50 MOVE 0 23 3\n51 MOVE 0 22 3\n52 MOVE 0 22 4\n53 DIG 0 22 4\n54 DIG 0 22 4\n",
        "50 MOVE 4 17 8\n51 MOVE 4 17 9\n52 DIG 4 17 9\n",
        "51 MOVE 1 22 8\n52 MOVE 1 23 8\n53 DIG 1 23 8\n",
        "51 MOVE 3 16 9\n52 MOVE 3 16 10\n53 DIG 3 16 10\n",
        "52 MOVE 5 17 9\n53 MOVE 5 18 9\n54 DIG 5 18 9\n55 DIG 5 18 9\n",
        "53 MOVE 4 17 10\n54 MOVE 4 17 11\n55 DIG 4 17 11\n",
        "54 MOVE 1 23 9\n55 DIG 1 23 9\n56 DIG 1 23 9\n",
        "54 MOVE 2 23 5\n55 DIG 2 23 5\n",
        "54 MOVE 3 15 10\n55 MOVE 3 15 11\n56 DIG 3 15 11\n57 DIG 3 15 11\n",
        "55 MOVE 0 23 4\n56 MOVE 0 23 5\n57 MOVE 0 23 6\n58 DIG 0 23 6\n59 DIG 0 23 6\n",
        "56 MOVE 2 22 5\n57 MOVE 2 22 6\n58 MOVE 2 22 7\n59 MOVE 2 22 8\n60 MOVE 2 22 9\n61 DIG 2 22 9\n",
        "56 MOVE 4 18 11\n57 DIG 4 18 11\n",
        "56 MOVE 5 19 9\n57 MOVE 5 20 9\n58 MOVE 5 21 9\n59 MOVE 5 21 10\n60 DIG 5 21 10\n",
        "57 MOVE 1 22 9\n58 MOVE 1 22 10\n59 DIG 1 22 10\n60 DIG 1 22 10\n",
        "57 MOVE 6 9 13\n58 MOVE 6 10 13\n59 DIG 6 10 13\n",
        "58 MOVE 3 14 11\n59 MOVE 3 14 12\n60 DIG 3 14 12\n61 DIG 3 14 12\n",
        "58 MOVE 4 17 11\n59 MOVE 4 17 12\n60 DIG 4 17 12\n",
        "60 MOVE 0 24 6\n61 MOVE 0 24 7\n62 MOVE 0 24 8\n63 MOVE 0 24 9\n64 MOVE 0 24 10\n65 DIG 0 24 10\n",
        "60 MOVE 6 11 13\n61 DIG 6 11 13\n62 DIG 6 11 13\n",
        "61 MOVE 1 21 10\n62 MOVE 1 21 11\n63 DIG 1 21 11\n",
        "61 MOVE 4 16 12\n62 DIG 4 16 12\n",
        "61 MOVE 5 22 10\n62 MOVE 5 22 11\n63 MOVE 5 22 12\n64 DIG 5 22 12\n",
        "62 MOVE 2 23 9\n63 MOVE 2 23 10\n64 MOVE 2 23 11\n65 MOVE 2 23 12\n66 DIG 2 23 12\n67 DIG 2 23 12\n",
        "62 MOVE 3 13 12\n63 DIG 3 13 12\n64 DIG 3 13 12\n",
        "63 MOVE 4 15 12\n64 MOVE 4 14 12\n65 MOVE 4 14 13\n66 DIG 4 14 13\n67 DIG 4 14 13\n",
        "63 MOVE 6 12 13\n64 MOVE 6 13 13\n65 MOVE 6 13 12\n66 MOVE 6 13 11\n67 MOVE 6 13 10\n68 DIG 6 13 10\n",
        "64 MOVE 1 21 12\n65 MOVE 1 21 13\n66 DIG 1 21 13\n67 DIG 1 21 13\n",
        "65 MOVE 3 14 12\n66 MOVE 3 15 12\n67 MOVE 3 16 12\n68 MOVE 3 17 12\n69 MOVE 3 18 12\n70 MOVE 3 19 12\n71 MOVE 3 19 13\n72 DIG 3 19 13\n",
        "65 MOVE 5 23 12\n66 MOVE 5 24 12\n67 MOVE 5 24 13\n68 DIG 5 24 13\n69 DIG 5 24 13\n",
        "66 MOVE 0 23 10\n67 MOVE 0 22 10\n68 MOVE 0 21 10\n69 MOVE 0 20 10\n70 MOVE 0 20 11\n71 MOVE 0 20 12\n72 MOVE 0 20 13\n73 DIG 0 20 13\n",
    ]
    date_01 = roadmap.recuperation_data("test/test_map_1.txt")
    map_01 = roadmap.mapping("test/test_map_1.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    number_truck = roadmap.nombre_de_camion(date_01)
    truck = roadmap.list_truck(number_truck)
    trajet = roadmap.trajet(matrice_map_01, truck)
    assert result == trajet


# test roadmap map 4
def test_write_map_4():
    roadmap.write_map(4, "test_sample_4.txt")
    assert filecmp.cmp("test/test_map_4.txt", "test/test_sample_4.txt") == True


def test_recuperation_data_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    data_02 = ["trucks: 6\n", "width: 28\n", "height: 11\n"]
    assert date_01 == data_02


def test_nb_camion_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 6


def test_nb_hauteur_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    assert roadmap.height_map(date_01) == 11


def test_nb_largeur_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    assert roadmap.width_map(date_01) == 28


def test_map_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    result = [
        "2   2 1          22       2 \n",
        "1   21       2  2      111 1\n",
        "  1    2 222   2       2    \n",
        "  2     121 11       1  1   \n",
        " 222   21221 2 11112    2 2 \n",
        "21 11 21  1  2 22221 21  2  \n",
        " 1   2   222     22 2    122\n",
        " 2 112      1 1121 1 2   1 1\n",
        "   12 1 1   1    11 1 2 1112\n",
        "2  1 1  1112 1 12   211 22  \n",
        "1  1  21       2  2    2  1 \n",
    ]
    assert roadmap.mapping("test/test_map_4.txt", roadmap.height_map(date_01)) == result


def test_matrice_map_4():
    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    map_01 = roadmap.mapping("test/test_map_4.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    result = [
        {"x": 0, "y": 0, "dig": 2},
        {"x": 4, "y": 0, "dig": 2},
        {"x": 6, "y": 0, "dig": 1},
        {"x": 17, "y": 0, "dig": 2},
        {"x": 18, "y": 0, "dig": 2},
        {"x": 26, "y": 0, "dig": 2},
        {"x": 27, "y": 1, "dig": 1},
        {"x": 25, "y": 1, "dig": 1},
        {"x": 24, "y": 1, "dig": 1},
        {"x": 23, "y": 1, "dig": 1},
        {"x": 16, "y": 1, "dig": 2},
        {"x": 13, "y": 1, "dig": 2},
        {"x": 5, "y": 1, "dig": 1},
        {"x": 4, "y": 1, "dig": 2},
        {"x": 0, "y": 1, "dig": 1},
        {"x": 2, "y": 2, "dig": 1},
        {"x": 7, "y": 2, "dig": 2},
        {"x": 9, "y": 2, "dig": 2},
        {"x": 10, "y": 2, "dig": 2},
        {"x": 11, "y": 2, "dig": 2},
        {"x": 15, "y": 2, "dig": 2},
        {"x": 23, "y": 2, "dig": 2},
        {"x": 24, "y": 3, "dig": 1},
        {"x": 21, "y": 3, "dig": 1},
        {"x": 13, "y": 3, "dig": 1},
        {"x": 12, "y": 3, "dig": 1},
        {"x": 10, "y": 3, "dig": 1},
        {"x": 9, "y": 3, "dig": 2},
        {"x": 8, "y": 3, "dig": 1},
        {"x": 2, "y": 3, "dig": 2},
        {"x": 1, "y": 4, "dig": 2},
        {"x": 2, "y": 4, "dig": 2},
        {"x": 3, "y": 4, "dig": 2},
        {"x": 7, "y": 4, "dig": 2},
        {"x": 8, "y": 4, "dig": 1},
        {"x": 9, "y": 4, "dig": 2},
        {"x": 10, "y": 4, "dig": 2},
        {"x": 11, "y": 4, "dig": 1},
        {"x": 13, "y": 4, "dig": 2},
        {"x": 15, "y": 4, "dig": 1},
        {"x": 16, "y": 4, "dig": 1},
        {"x": 17, "y": 4, "dig": 1},
        {"x": 18, "y": 4, "dig": 1},
        {"x": 19, "y": 4, "dig": 2},
        {"x": 24, "y": 4, "dig": 2},
        {"x": 26, "y": 4, "dig": 2},
        {"x": 25, "y": 5, "dig": 2},
        {"x": 22, "y": 5, "dig": 1},
        {"x": 21, "y": 5, "dig": 2},
        {"x": 19, "y": 5, "dig": 1},
        {"x": 18, "y": 5, "dig": 2},
        {"x": 17, "y": 5, "dig": 2},
        {"x": 16, "y": 5, "dig": 2},
        {"x": 15, "y": 5, "dig": 2},
        {"x": 13, "y": 5, "dig": 2},
        {"x": 10, "y": 5, "dig": 1},
        {"x": 7, "y": 5, "dig": 1},
        {"x": 6, "y": 5, "dig": 2},
        {"x": 4, "y": 5, "dig": 1},
        {"x": 3, "y": 5, "dig": 1},
        {"x": 1, "y": 5, "dig": 1},
        {"x": 0, "y": 5, "dig": 2},
        {"x": 1, "y": 6, "dig": 1},
        {"x": 5, "y": 6, "dig": 2},
        {"x": 9, "y": 6, "dig": 2},
        {"x": 10, "y": 6, "dig": 2},
        {"x": 11, "y": 6, "dig": 2},
        {"x": 17, "y": 6, "dig": 2},
        {"x": 18, "y": 6, "dig": 2},
        {"x": 20, "y": 6, "dig": 2},
        {"x": 25, "y": 6, "dig": 1},
        {"x": 26, "y": 6, "dig": 2},
        {"x": 27, "y": 6, "dig": 2},
        {"x": 27, "y": 7, "dig": 1},
        {"x": 25, "y": 7, "dig": 1},
        {"x": 21, "y": 7, "dig": 2},
        {"x": 19, "y": 7, "dig": 1},
        {"x": 17, "y": 7, "dig": 1},
        {"x": 16, "y": 7, "dig": 2},
        {"x": 15, "y": 7, "dig": 1},
        {"x": 14, "y": 7, "dig": 1},
        {"x": 12, "y": 7, "dig": 1},
        {"x": 5, "y": 7, "dig": 2},
        {"x": 4, "y": 7, "dig": 1},
        {"x": 3, "y": 7, "dig": 1},
        {"x": 1, "y": 7, "dig": 2},
        {"x": 3, "y": 8, "dig": 1},
        {"x": 4, "y": 8, "dig": 2},
        {"x": 6, "y": 8, "dig": 1},
        {"x": 8, "y": 8, "dig": 1},
        {"x": 12, "y": 8, "dig": 1},
        {"x": 17, "y": 8, "dig": 1},
        {"x": 18, "y": 8, "dig": 1},
        {"x": 20, "y": 8, "dig": 1},
        {"x": 22, "y": 8, "dig": 2},
        {"x": 24, "y": 8, "dig": 1},
        {"x": 25, "y": 8, "dig": 1},
        {"x": 26, "y": 8, "dig": 1},
        {"x": 27, "y": 8, "dig": 2},
        {"x": 25, "y": 9, "dig": 2},
        {"x": 24, "y": 9, "dig": 2},
        {"x": 22, "y": 9, "dig": 1},
        {"x": 21, "y": 9, "dig": 1},
        {"x": 20, "y": 9, "dig": 2},
        {"x": 16, "y": 9, "dig": 2},
        {"x": 15, "y": 9, "dig": 1},
        {"x": 13, "y": 9, "dig": 1},
        {"x": 11, "y": 9, "dig": 2},
        {"x": 10, "y": 9, "dig": 1},
        {"x": 9, "y": 9, "dig": 1},
        {"x": 8, "y": 9, "dig": 1},
        {"x": 5, "y": 9, "dig": 1},
        {"x": 3, "y": 9, "dig": 1},
        {"x": 0, "y": 9, "dig": 2},
        {"x": 0, "y": 10, "dig": 1},
        {"x": 3, "y": 10, "dig": 1},
        {"x": 6, "y": 10, "dig": 2},
        {"x": 7, "y": 10, "dig": 1},
        {"x": 15, "y": 10, "dig": 2},
        {"x": 18, "y": 10, "dig": 2},
        {"x": 23, "y": 10, "dig": 2},
        {"x": 26, "y": 10, "dig": 1},
    ]
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    assert matrice_map_01 == result


def test_trajet_map_4():
    result = [
        "0 DIG 0 0 0\n1 DIG 0 0 0\n",
        "0 DIG 1 0 1\n",
        "0 MOVE 2 1 2\n1 MOVE 2 2 2\n2 DIG 2 2 2\n",
        "0 MOVE 3 1 3\n1 MOVE 3 2 3\n2 DIG 3 2 3\n3 DIG 3 2 3\n",
        "0 MOVE 4 1 4\n1 DIG 4 1 4\n2 DIG 4 1 4\n",
        "0 DIG 5 0 5\n1 DIG 5 0 5\n",
        "1 MOVE 1 1 1\n2 MOVE 1 2 1\n3 MOVE 1 3 1\n4 MOVE 1 4 1\n5 DIG 1 4 1\n6 DIG 1 4 1\n",
        "2 MOVE 0 1 0\n3 MOVE 0 2 0\n4 MOVE 0 3 0\n5 MOVE 0 4 0\n6 DIG 0 4 0\n7 DIG 0 4 0\n",
        "2 MOVE 5 1 5\n3 DIG 5 1 5\n",
        "3 MOVE 2 2 3\n4 MOVE 2 2 4\n5 DIG 2 2 4\n6 DIG 2 2 4\n",
        "3 MOVE 4 2 4\n4 MOVE 4 3 4\n5 DIG 4 3 4\n6 DIG 4 3 4\n",
        "4 MOVE 3 3 3\n5 MOVE 3 3 4\n6 MOVE 3 3 5\n7 DIG 3 3 5\n",
        "4 MOVE 5 1 6\n5 DIG 5 1 6\n",
        "6 MOVE 5 1 7\n7 DIG 5 1 7\n8 DIG 5 1 7\n",
        "7 MOVE 1 5 1\n8 DIG 1 5 1\n",
        "7 MOVE 2 3 4\n8 MOVE 2 4 4\n9 MOVE 2 4 5\n10 DIG 2 4 5\n",
        "7 MOVE 4 3 5\n8 MOVE 4 3 6\n9 MOVE 4 3 7\n10 DIG 4 3 7\n",
        "8 MOVE 0 5 0\n9 MOVE 0 6 0\n10 DIG 0 6 0\n",
        "8 MOVE 3 4 5\n9 MOVE 3 5 5\n10 MOVE 3 6 5\n11 DIG 3 6 5\n12 DIG 3 6 5\n",
        "9 MOVE 1 6 1\n10 MOVE 1 7 1\n11 MOVE 1 7 2\n12 DIG 1 7 2\n13 DIG 1 7 2\n",
        "9 MOVE 5 2 7\n10 MOVE 5 3 7\n11 MOVE 5 4 7\n12 DIG 5 4 7\n",
        "11 MOVE 0 7 0\n12 MOVE 0 8 0\n13 MOVE 0 9 0\n14 MOVE 0 9 1\n15 MOVE 0 9 2\n16 DIG 0 9 2\n17 DIG 0 9 2\n",
        "11 MOVE 2 5 5\n12 MOVE 2 5 6\n13 DIG 2 5 6\n14 DIG 2 5 6\n",
        "11 MOVE 4 3 8\n12 DIG 4 3 8\n",
        "13 MOVE 3 7 5\n14 DIG 3 7 5\n",
        "13 MOVE 4 4 8\n14 DIG 4 4 8\n15 DIG 4 4 8\n",
        "13 MOVE 5 5 7\n14 DIG 5 5 7\n15 DIG 5 5 7\n",
        "14 MOVE 1 8 2\n15 MOVE 1 8 3\n16 DIG 1 8 3\n",
        "15 MOVE 2 6 6\n16 MOVE 2 6 7\n17 MOVE 2 6 8\n18 DIG 2 6 8\n",
        "15 MOVE 3 7 4\n16 DIG 3 7 4\n17 DIG 3 7 4\n",
        "16 MOVE 4 5 8\n17 MOVE 4 5 9\n18 DIG 4 5 9\n",
        "16 MOVE 5 6 7\n17 MOVE 5 7 7\n18 MOVE 5 8 7\n19 MOVE 5 8 8\n20 DIG 5 8 8\n",
        "17 MOVE 1 9 3\n18 DIG 1 9 3\n19 DIG 1 9 3\n",
        "18 MOVE 0 10 2\n19 DIG 0 10 2\n20 DIG 0 10 2\n",
        "18 MOVE 3 8 4\n19 DIG 3 8 4\n",
        "19 MOVE 2 6 9\n20 MOVE 2 6 10\n21 DIG 2 6 10\n22 DIG 2 6 10\n",
        "19 MOVE 4 4 9\n20 MOVE 4 3 9\n21 DIG 4 3 9\n",
        "20 MOVE 1 10 3\n21 DIG 1 10 3\n",
        "20 MOVE 3 9 4\n21 DIG 3 9 4\n22 DIG 3 9 4\n",
        "21 MOVE 0 11 2\n22 DIG 0 11 2\n23 DIG 0 11 2\n",
        "21 MOVE 5 8 9\n22 DIG 5 8 9\n",
        "22 MOVE 1 10 4\n23 DIG 1 10 4\n24 DIG 1 10 4\n",
        "22 MOVE 4 3 10\n23 DIG 4 3 10\n",
        "23 MOVE 2 7 10\n24 DIG 2 7 10\n",
        "23 MOVE 3 10 4\n24 MOVE 3 11 4\n25 DIG 3 11 4\n",
        "23 MOVE 5 9 9\n24 DIG 5 9 9\n",
        "24 MOVE 0 12 2\n25 MOVE 0 12 3\n26 DIG 0 12 3\n",
        "24 MOVE 4 2 10\n25 MOVE 4 1 10\n26 MOVE 4 0 10\n27 DIG 4 0 10\n",
        "25 MOVE 1 10 5\n26 DIG 1 10 5\n",
        "25 MOVE 2 8 10\n26 MOVE 2 9 10\n27 MOVE 2 10 10\n28 MOVE 2 10 9\n29 DIG 2 10 9\n",
        "25 MOVE 5 10 9\n26 MOVE 5 11 9\n27 DIG 5 11 9\n28 DIG 5 11 9\n",
        "26 MOVE 3 12 4\n27 MOVE 3 13 4\n28 DIG 3 13 4\n29 DIG 3 13 4\n",
        "27 MOVE 0 13 3\n28 DIG 0 13 3\n",
        "27 MOVE 1 10 6\n28 DIG 1 10 6\n29 DIG 1 10 6\n",
        "28 MOVE 4 0 9\n29 DIG 4 0 9\n30 DIG 4 0 9\n",
        "29 MOVE 0 13 2\n30 MOVE 0 13 1\n31 DIG 0 13 1\n32 DIG 0 13 1\n",
        "29 MOVE 5 12 9\n30 MOVE 5 12 8\n31 DIG 5 12 8\n",
        "30 MOVE 1 9 6\n31 DIG 1 9 6\n32 DIG 1 9 6\n",
        "30 MOVE 2 11 9\n31 MOVE 2 12 9\n32 MOVE 2 13 9\n33 DIG 2 13 9\n",
        "30 MOVE 3 13 5\n31 DIG 3 13 5\n32 DIG 3 13 5\n",
        "31 MOVE 4 1 9\n32 MOVE 4 2 9\n33 MOVE 4 3 9\n34 MOVE 4 4 9\n35 MOVE 4 5 9\n36 MOVE 4 6 9\n37 MOVE 4 7 9\n38 MOVE 4 8 9\n39 MOVE 4 9 9\n40 MOVE 4 10 9\n41 MOVE 4 11 9\n42 MOVE 4 11 8\n43 MOVE 4 11 7\n44 MOVE 4 11 6\n45 DIG 4 11 6\n46 DIG 4 11 6\n",
        "32 MOVE 5 12 7\n33 DIG 5 12 7\n",
        "33 MOVE 0 14 1\n34 MOVE 0 15 1\n35 MOVE 0 16 1\n36 DIG 0 16 1\n37 DIG 0 16 1\n",
        "33 MOVE 1 10 6\n34 MOVE 1 11 6\n35 MOVE 1 12 6\n36 MOVE 1 13 6\n37 MOVE 1 14 6\n38 MOVE 1 14 7\n39 DIG 1 14 7\n",
        "33 MOVE 3 14 5\n34 MOVE 3 15 5\n35 DIG 3 15 5\n36 DIG 3 15 5\n",
        "34 MOVE 2 14 9\n35 MOVE 2 15 9\n36 DIG 2 15 9\n",
        "34 MOVE 5 13 7\n35 MOVE 5 14 7\n36 MOVE 5 15 7\n37 DIG 5 15 7\n",
        "37 MOVE 2 16 9\n38 DIG 2 16 9\n39 DIG 2 16 9\n",
        "37 MOVE 3 15 4\n38 DIG 3 15 4\n",
        "38 MOVE 0 17 1\n39 MOVE 0 17 0\n40 DIG 0 17 0\n41 DIG 0 17 0\n",
        "38 MOVE 5 16 7\n39 DIG 5 16 7\n40 DIG 5 16 7\n",
        "39 MOVE 3 16 4\n40 DIG 3 16 4\n",
        "40 MOVE 1 15 7\n41 MOVE 1 16 7\n42 MOVE 1 17 7\n43 DIG 1 17 7\n",
        "40 MOVE 2 17 9\n41 MOVE 2 17 8\n42 DIG 2 17 8\n",
        "41 MOVE 3 17 4\n42 DIG 3 17 4\n",
        "41 MOVE 5 16 6\n42 MOVE 5 16 5\n43 DIG 5 16 5\n44 DIG 5 16 5\n",
        "42 MOVE 0 18 0\n43 DIG 0 18 0\n44 DIG 0 18 0\n",
        "43 MOVE 2 18 8\n44 DIG 2 18 8\n",
        "43 MOVE 3 18 4\n44 DIG 3 18 4\n",
        "44 MOVE 1 17 6\n45 DIG 1 17 6\n46 DIG 1 17 6\n",
        "45 MOVE 0 17 0\n46 MOVE 0 16 0\n47 MOVE 0 15 0\n48 MOVE 0 15 1\n49 MOVE 0 15 2\n50 DIG 0 15 2\n51 DIG 0 15 2\n",
        "45 MOVE 2 18 7\n46 MOVE 2 18 6\n47 DIG 2 18 6\n48 DIG 2 18 6\n",
        "45 MOVE 3 19 4\n46 DIG 3 19 4\n47 DIG 3 19 4\n",
        "45 MOVE 5 17 5\n46 DIG 5 17 5\n47 DIG 5 17 5\n",
        "47 MOVE 1 18 6\n48 MOVE 1 18 5\n49 DIG 1 18 5\n50 DIG 1 18 5\n",
        "47 MOVE 4 12 6\n48 MOVE 4 13 6\n49 MOVE 4 14 6\n50 MOVE 4 15 6\n51 MOVE 4 15 7\n52 MOVE 4 15 8\n53 MOVE 4 15 9\n54 MOVE 4 15 10\n55 DIG 4 15 10\n56 DIG 4 15 10\n",
        "48 MOVE 3 19 5\n49 DIG 3 19 5\n",
        "48 MOVE 5 18 5\n49 MOVE 5 19 5\n50 MOVE 5 20 5\n51 MOVE 5 21 5\n52 DIG 5 21 5\n53 DIG 5 21 5\n",
        "49 MOVE 2 19 6\n50 MOVE 2 20 6\n51 DIG 2 20 6\n52 DIG 2 20 6\n",
        "50 MOVE 3 19 6\n51 MOVE 3 19 7\n52 DIG 3 19 7\n",
        "51 MOVE 1 19 5\n52 MOVE 1 20 5\n53 MOVE 1 21 5\n54 MOVE 1 22 5\n55 DIG 1 22 5\n",
        "52 MOVE 0 16 2\n53 MOVE 0 17 2\n54 MOVE 0 18 2\n55 MOVE 0 19 2\n56 MOVE 0 20 2\n57 MOVE 0 21 2\n58 MOVE 0 21 3\n59 DIG 0 21 3\n",
        "53 MOVE 2 21 6\n54 MOVE 2 21 7\n55 DIG 2 21 7\n56 DIG 2 21 7\n",
        "53 MOVE 3 20 7\n54 MOVE 3 20 8\n55 DIG 3 20 8\n",
        "54 MOVE 5 22 5\n55 MOVE 5 23 5\n56 MOVE 5 24 5\n57 MOVE 5 24 4\n58 DIG 5 24 4\n59 DIG 5 24 4\n",
        "56 MOVE 1 23 5\n57 MOVE 1 24 5\n58 MOVE 1 25 5\n59 DIG 1 25 5\n60 DIG 1 25 5\n",
        "56 MOVE 3 20 9\n57 DIG 3 20 9\n58 DIG 3 20 9\n",
        "57 MOVE 2 22 7\n58 MOVE 2 22 8\n59 DIG 2 22 8\n60 DIG 2 22 8\n",
        "57 MOVE 4 16 10\n58 MOVE 4 17 10\n59 MOVE 4 18 10\n60 DIG 4 18 10\n61 DIG 4 18 10\n",
        "59 MOVE 3 21 9\n60 DIG 3 21 9\n",
        "60 MOVE 0 22 3\n61 MOVE 0 23 3\n62 MOVE 0 23 2\n63 DIG 0 23 2\n64 DIG 0 23 2\n",
        "60 MOVE 5 24 3\n61 DIG 5 24 3\n",
        "61 MOVE 1 25 6\n62 DIG 1 25 6\n",
        "61 MOVE 2 22 9\n62 DIG 2 22 9\n",
        "61 MOVE 3 22 9\n62 MOVE 3 23 9\n63 MOVE 3 24 9\n64 DIG 3 24 9\n65 DIG 3 24 9\n",
        "62 MOVE 4 19 10\n63 MOVE 4 20 10\n64 MOVE 4 21 10\n65 MOVE 4 22 10\n66 MOVE 4 23 10\n67 DIG 4 23 10\n68 DIG 4 23 10\n",
        "62 MOVE 5 24 2\n63 MOVE 5 24 1\n64 DIG 5 24 1\n",
        "63 MOVE 1 26 6\n64 DIG 1 26 6\n65 DIG 1 26 6\n",
        "63 MOVE 2 23 9\n64 MOVE 2 24 9\n65 MOVE 2 24 8\n66 DIG 2 24 8\n",
        "65 MOVE 0 23 1\n66 DIG 0 23 1\n",
        "65 MOVE 5 25 1\n66 DIG 5 25 1\n",
        "66 MOVE 1 27 6\n67 DIG 1 27 6\n68 DIG 1 27 6\n",
        "66 MOVE 3 25 9\n67 DIG 3 25 9\n68 DIG 3 25 9\n",
        "67 MOVE 0 24 1\n68 MOVE 0 25 1\n69 MOVE 0 26 1\n70 MOVE 0 26 0\n71 DIG 0 26 0\n72 DIG 0 26 0\n",
        "67 MOVE 2 25 8\n68 DIG 2 25 8\n",
        "67 MOVE 5 26 1\n68 MOVE 5 27 1\n69 DIG 5 27 1\n",
        "69 MOVE 1 27 7\n70 DIG 1 27 7\n",
        "69 MOVE 2 25 7\n70 DIG 2 25 7\n",
        "69 MOVE 3 26 9\n70 MOVE 3 26 8\n71 DIG 3 26 8\n",
        "69 MOVE 4 24 10\n70 MOVE 4 25 10\n71 MOVE 4 26 10\n72 DIG 4 26 10\n",
        "70 MOVE 5 26 1\n71 MOVE 5 26 2\n72 MOVE 5 26 3\n73 MOVE 5 26 4\n74 DIG 5 26 4\n75 DIG 5 26 4\n",
        "71 MOVE 1 27 8\n72 DIG 1 27 8\n73 DIG 1 27 8\n",
    ]

    date_01 = roadmap.recuperation_data("test/test_map_4.txt")
    map_01 = roadmap.mapping("test/test_map_4.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    number_truck = roadmap.nombre_de_camion(date_01)
    truck = roadmap.list_truck(number_truck)
    trajet = roadmap.trajet(matrice_map_01, truck)
    assert result == trajet


# test roadmap map 8
def test_write_map_8():
    roadmap.write_map(8, "test/test_sample_8.txt")
    assert filecmp.cmp("test/test_map_8.txt", "test/test_sample_8.txt") == True


def test_recuperation_data_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    data_02 = ["trucks: 2\n", "width: 20\n", "height: 17\n"]
    assert date_01 == data_02


def test_nb_camion_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 2


def test_nb_hauteur_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    assert roadmap.height_map(date_01) == 17


def test_nb_largeur_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    assert roadmap.width_map(date_01) == 20


def test_map_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    result = [
        "   2   1 1   1 11  1\n",
        "    212  2 2 1  21 2\n",
        "2        1 2   2222 \n",
        "       2  2  1   112\n",
        "2 2222   11 222     \n",
        "2    12  2 2  21  1 \n",
        " 2 22  1       2 22 \n",
        "22   2121  2   2 212\n",
        "    2 22    2  2    \n",
        "      1 2  1   2 1 1\n",
        " 2  1   1   122 2  2\n",
        "21  12     111  222 \n",
        "1 1 11 11 121 21    \n",
        "  1122  22 21  21 21\n",
        "21 221 1     1211   \n",
        "  2 1   2       2   \n",
        " 1 1 1  2 11  2   1 \n",
    ]
    assert roadmap.mapping("test/test_map_8.txt", roadmap.height_map(date_01)) == result


def test_matrice_map_8():
    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    map_01 = roadmap.mapping("test/test_map_8.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    result = [
        {"x": 3, "y": 0, "dig": 2},
        {"x": 7, "y": 0, "dig": 1},
        {"x": 9, "y": 0, "dig": 1},
        {"x": 13, "y": 0, "dig": 1},
        {"x": 15, "y": 0, "dig": 1},
        {"x": 16, "y": 0, "dig": 1},
        {"x": 19, "y": 0, "dig": 1},
        {"x": 19, "y": 1, "dig": 2},
        {"x": 17, "y": 1, "dig": 1},
        {"x": 16, "y": 1, "dig": 2},
        {"x": 13, "y": 1, "dig": 1},
        {"x": 11, "y": 1, "dig": 2},
        {"x": 9, "y": 1, "dig": 2},
        {"x": 6, "y": 1, "dig": 2},
        {"x": 5, "y": 1, "dig": 1},
        {"x": 4, "y": 1, "dig": 2},
        {"x": 0, "y": 2, "dig": 2},
        {"x": 9, "y": 2, "dig": 1},
        {"x": 11, "y": 2, "dig": 2},
        {"x": 15, "y": 2, "dig": 2},
        {"x": 16, "y": 2, "dig": 2},
        {"x": 17, "y": 2, "dig": 2},
        {"x": 18, "y": 2, "dig": 2},
        {"x": 19, "y": 3, "dig": 2},
        {"x": 18, "y": 3, "dig": 1},
        {"x": 17, "y": 3, "dig": 1},
        {"x": 13, "y": 3, "dig": 1},
        {"x": 10, "y": 3, "dig": 2},
        {"x": 7, "y": 3, "dig": 2},
        {"x": 0, "y": 4, "dig": 2},
        {"x": 2, "y": 4, "dig": 2},
        {"x": 3, "y": 4, "dig": 2},
        {"x": 4, "y": 4, "dig": 2},
        {"x": 5, "y": 4, "dig": 2},
        {"x": 9, "y": 4, "dig": 1},
        {"x": 10, "y": 4, "dig": 1},
        {"x": 12, "y": 4, "dig": 2},
        {"x": 13, "y": 4, "dig": 2},
        {"x": 14, "y": 4, "dig": 2},
        {"x": 18, "y": 5, "dig": 1},
        {"x": 15, "y": 5, "dig": 1},
        {"x": 14, "y": 5, "dig": 2},
        {"x": 11, "y": 5, "dig": 2},
        {"x": 9, "y": 5, "dig": 2},
        {"x": 6, "y": 5, "dig": 2},
        {"x": 5, "y": 5, "dig": 1},
        {"x": 0, "y": 5, "dig": 2},
        {"x": 1, "y": 6, "dig": 2},
        {"x": 3, "y": 6, "dig": 2},
        {"x": 4, "y": 6, "dig": 2},
        {"x": 7, "y": 6, "dig": 1},
        {"x": 15, "y": 6, "dig": 2},
        {"x": 17, "y": 6, "dig": 2},
        {"x": 18, "y": 6, "dig": 2},
        {"x": 19, "y": 7, "dig": 2},
        {"x": 18, "y": 7, "dig": 1},
        {"x": 17, "y": 7, "dig": 2},
        {"x": 15, "y": 7, "dig": 2},
        {"x": 11, "y": 7, "dig": 2},
        {"x": 8, "y": 7, "dig": 1},
        {"x": 7, "y": 7, "dig": 2},
        {"x": 6, "y": 7, "dig": 1},
        {"x": 5, "y": 7, "dig": 2},
        {"x": 1, "y": 7, "dig": 2},
        {"x": 0, "y": 7, "dig": 2},
        {"x": 4, "y": 8, "dig": 2},
        {"x": 6, "y": 8, "dig": 2},
        {"x": 7, "y": 8, "dig": 2},
        {"x": 12, "y": 8, "dig": 2},
        {"x": 15, "y": 8, "dig": 2},
        {"x": 19, "y": 9, "dig": 1},
        {"x": 17, "y": 9, "dig": 1},
        {"x": 15, "y": 9, "dig": 2},
        {"x": 11, "y": 9, "dig": 1},
        {"x": 8, "y": 9, "dig": 2},
        {"x": 6, "y": 9, "dig": 1},
        {"x": 1, "y": 10, "dig": 2},
        {"x": 4, "y": 10, "dig": 1},
        {"x": 8, "y": 10, "dig": 1},
        {"x": 12, "y": 10, "dig": 1},
        {"x": 13, "y": 10, "dig": 2},
        {"x": 14, "y": 10, "dig": 2},
        {"x": 16, "y": 10, "dig": 2},
        {"x": 19, "y": 10, "dig": 2},
        {"x": 18, "y": 11, "dig": 2},
        {"x": 17, "y": 11, "dig": 2},
        {"x": 16, "y": 11, "dig": 2},
        {"x": 13, "y": 11, "dig": 1},
        {"x": 12, "y": 11, "dig": 1},
        {"x": 11, "y": 11, "dig": 1},
        {"x": 5, "y": 11, "dig": 2},
        {"x": 4, "y": 11, "dig": 1},
        {"x": 1, "y": 11, "dig": 1},
        {"x": 0, "y": 11, "dig": 2},
        {"x": 0, "y": 12, "dig": 1},
        {"x": 2, "y": 12, "dig": 1},
        {"x": 4, "y": 12, "dig": 1},
        {"x": 5, "y": 12, "dig": 1},
        {"x": 7, "y": 12, "dig": 1},
        {"x": 8, "y": 12, "dig": 1},
        {"x": 10, "y": 12, "dig": 1},
        {"x": 11, "y": 12, "dig": 2},
        {"x": 12, "y": 12, "dig": 1},
        {"x": 14, "y": 12, "dig": 2},
        {"x": 15, "y": 12, "dig": 1},
        {"x": 19, "y": 13, "dig": 1},
        {"x": 18, "y": 13, "dig": 2},
        {"x": 16, "y": 13, "dig": 1},
        {"x": 15, "y": 13, "dig": 2},
        {"x": 12, "y": 13, "dig": 1},
        {"x": 11, "y": 13, "dig": 2},
        {"x": 9, "y": 13, "dig": 2},
        {"x": 8, "y": 13, "dig": 2},
        {"x": 5, "y": 13, "dig": 2},
        {"x": 4, "y": 13, "dig": 2},
        {"x": 3, "y": 13, "dig": 1},
        {"x": 2, "y": 13, "dig": 1},
        {"x": 0, "y": 14, "dig": 2},
        {"x": 1, "y": 14, "dig": 1},
        {"x": 3, "y": 14, "dig": 2},
        {"x": 4, "y": 14, "dig": 2},
        {"x": 5, "y": 14, "dig": 1},
        {"x": 7, "y": 14, "dig": 1},
        {"x": 13, "y": 14, "dig": 1},
        {"x": 14, "y": 14, "dig": 2},
        {"x": 15, "y": 14, "dig": 1},
        {"x": 16, "y": 14, "dig": 1},
        {"x": 16, "y": 15, "dig": 2},
        {"x": 8, "y": 15, "dig": 2},
        {"x": 4, "y": 15, "dig": 1},
        {"x": 2, "y": 15, "dig": 2},
        {"x": 1, "y": 16, "dig": 1},
        {"x": 3, "y": 16, "dig": 1},
        {"x": 5, "y": 16, "dig": 1},
        {"x": 8, "y": 16, "dig": 2},
        {"x": 10, "y": 16, "dig": 1},
        {"x": 11, "y": 16, "dig": 1},
        {"x": 14, "y": 16, "dig": 2},
        {"x": 18, "y": 16, "dig": 1},
    ]

    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    assert matrice_map_01 == result


def test_trajet_map_8():
    result = [
        "0 MOVE 0 0 1\n1 MOVE 0 0 2\n2 DIG 0 0 2\n3 DIG 0 0 2\n",
        "0 MOVE 1 0 2\n1 MOVE 1 0 3\n2 MOVE 1 0 4\n3 DIG 1 0 4\n4 DIG 1 0 4\n",
        "4 MOVE 0 0 3\n5 MOVE 0 0 4\n6 MOVE 0 0 5\n7 DIG 0 0 5\n8 DIG 0 0 5\n",
        "5 MOVE 1 1 4\n6 MOVE 1 2 4\n7 DIG 1 2 4\n8 DIG 1 2 4\n",
        "9 MOVE 0 1 5\n10 MOVE 0 1 6\n11 DIG 0 1 6\n12 DIG 0 1 6\n",
        "9 MOVE 1 3 4\n10 DIG 1 3 4\n11 DIG 1 3 4\n",
        "12 MOVE 1 4 4\n13 DIG 1 4 4\n14 DIG 1 4 4\n",
        "13 MOVE 0 1 7\n14 DIG 0 1 7\n15 DIG 0 1 7\n",
        "15 MOVE 1 5 4\n16 DIG 1 5 4\n17 DIG 1 5 4\n",
        "16 MOVE 0 0 7\n17 DIG 0 0 7\n18 DIG 0 0 7\n",
        "18 MOVE 1 5 5\n19 DIG 1 5 5\n",
        "19 MOVE 0 1 7\n20 MOVE 0 2 7\n21 MOVE 0 3 7\n22 MOVE 0 3 6\n23 DIG 0 3 6\n24 DIG 0 3 6\n",
        "20 MOVE 1 6 5\n21 DIG 1 6 5\n22 DIG 1 6 5\n",
        "23 MOVE 1 7 5\n24 MOVE 1 7 6\n25 DIG 1 7 6\n",
        "25 MOVE 0 4 6\n26 DIG 0 4 6\n27 DIG 0 4 6\n",
        "26 MOVE 1 7 7\n27 DIG 1 7 7\n28 DIG 1 7 7\n",
        "28 MOVE 0 5 6\n29 MOVE 0 5 7\n30 DIG 0 5 7\n31 DIG 0 5 7\n",
        "29 MOVE 1 8 7\n30 DIG 1 8 7\n",
        "31 MOVE 1 7 7\n32 MOVE 1 6 7\n33 DIG 1 6 7\n",
        "32 MOVE 0 4 7\n33 MOVE 0 4 8\n34 DIG 0 4 8\n35 DIG 0 4 8\n",
        "34 MOVE 1 6 8\n35 DIG 1 6 8\n36 DIG 1 6 8\n",
        "36 MOVE 0 4 9\n37 MOVE 0 4 10\n38 DIG 0 4 10\n",
        "37 MOVE 1 7 8\n38 DIG 1 7 8\n39 DIG 1 7 8\n",
        "39 MOVE 0 4 11\n40 DIG 0 4 11\n",
        "40 MOVE 1 8 8\n41 MOVE 1 8 9\n42 DIG 1 8 9\n43 DIG 1 8 9\n",
        "41 MOVE 0 5 11\n42 DIG 0 5 11\n43 DIG 0 5 11\n",
        "44 MOVE 0 5 12\n45 DIG 0 5 12\n",
        "44 MOVE 1 8 10\n45 DIG 1 8 10\n",
        "46 MOVE 0 4 12\n47 DIG 0 4 12\n",
        "46 MOVE 1 8 11\n47 MOVE 1 8 12\n48 DIG 1 8 12\n",
        "48 MOVE 0 4 13\n49 DIG 0 4 13\n50 DIG 0 4 13\n",
        "49 MOVE 1 7 12\n50 DIG 1 7 12\n",
        "51 MOVE 0 5 13\n52 DIG 0 5 13\n53 DIG 0 5 13\n",
        "51 MOVE 1 8 12\n52 MOVE 1 8 13\n53 DIG 1 8 13\n54 DIG 1 8 13\n",
        "54 MOVE 0 5 14\n55 DIG 0 5 14\n",
        "55 MOVE 1 9 13\n56 DIG 1 9 13\n57 DIG 1 9 13\n",
        "56 MOVE 0 4 14\n57 DIG 0 4 14\n58 DIG 0 4 14\n",
        "58 MOVE 1 10 13\n59 MOVE 1 10 12\n60 DIG 1 10 12\n",
        "59 MOVE 0 3 14\n60 DIG 0 3 14\n61 DIG 0 3 14\n",
        "61 MOVE 1 11 12\n62 DIG 1 11 12\n63 DIG 1 11 12\n",
        "62 MOVE 0 3 13\n63 DIG 0 3 13\n",
        "64 MOVE 0 2 13\n65 DIG 0 2 13\n",
        "64 MOVE 1 11 11\n65 DIG 1 11 11\n",
        "66 MOVE 0 2 12\n67 DIG 0 2 12\n",
        "66 MOVE 1 12 11\n67 DIG 1 12 11\n",
        "68 MOVE 0 1 12\n69 MOVE 0 1 11\n70 DIG 0 1 11\n",
        "68 MOVE 1 12 10\n69 DIG 1 12 10\n",
        "70 MOVE 1 13 10\n71 DIG 1 13 10\n72 DIG 1 13 10\n",
        "71 MOVE 0 1 10\n72 DIG 0 1 10\n73 DIG 0 1 10\n",
        "73 MOVE 1 14 10\n74 DIG 1 14 10\n75 DIG 1 14 10\n",
        "74 MOVE 0 0 10\n75 MOVE 0 0 11\n76 DIG 0 0 11\n77 DIG 0 0 11\n",
        "76 MOVE 1 15 10\n77 MOVE 1 15 9\n78 DIG 1 15 9\n79 DIG 1 15 9\n",
        "78 MOVE 0 0 12\n79 DIG 0 0 12\n",
        "80 MOVE 0 0 13\n81 MOVE 0 0 14\n82 DIG 0 0 14\n83 DIG 0 0 14\n",
        "80 MOVE 1 15 8\n81 DIG 1 15 8\n82 DIG 1 15 8\n",
        "83 MOVE 1 15 7\n84 DIG 1 15 7\n85 DIG 1 15 7\n",
        "84 MOVE 0 1 14\n85 DIG 0 1 14\n",
        "86 MOVE 0 2 14\n87 MOVE 0 2 15\n88 DIG 0 2 15\n89 DIG 0 2 15\n",
        "86 MOVE 1 15 6\n87 DIG 1 15 6\n88 DIG 1 15 6\n",
        "89 MOVE 1 15 5\n90 DIG 1 15 5\n",
        "90 MOVE 0 3 15\n91 MOVE 0 4 15\n92 DIG 0 4 15\n",
        "91 MOVE 1 14 5\n92 DIG 1 14 5\n93 DIG 1 14 5\n",
        "93 MOVE 0 3 15\n94 MOVE 0 3 16\n95 DIG 0 3 16\n",
        "94 MOVE 1 14 4\n95 DIG 1 14 4\n96 DIG 1 14 4\n",
        "96 MOVE 0 2 16\n97 MOVE 0 1 16\n98 DIG 0 1 16\n",
        "97 MOVE 1 13 4\n98 DIG 1 13 4\n99 DIG 1 13 4\n",
        "99 MOVE 0 2 16\n100 MOVE 0 3 16\n101 MOVE 0 4 16\n102 MOVE 0 5 16\n103 DIG 0 5 16\n",
        "100 MOVE 1 13 3\n101 DIG 1 13 3\n",
        "102 MOVE 1 13 2\n103 MOVE 1 13 1\n104 DIG 1 13 1\n",
        "104 MOVE 0 6 16\n105 MOVE 0 7 16\n106 MOVE 0 8 16\n107 DIG 0 8 16\n108 DIG 0 8 16\n",
        "105 MOVE 1 13 0\n106 DIG 1 13 0\n",
        "107 MOVE 1 14 0\n108 MOVE 1 15 0\n109 DIG 1 15 0\n",
        "109 MOVE 0 8 15\n110 DIG 0 8 15\n111 DIG 0 8 15\n",
        "110 MOVE 1 16 0\n111 DIG 1 16 0\n",
        "112 MOVE 0 7 15\n113 MOVE 0 7 14\n114 DIG 0 7 14\n",
        "112 MOVE 1 16 1\n113 DIG 1 16 1\n114 DIG 1 16 1\n",
        "115 MOVE 0 8 14\n116 MOVE 0 9 14\n117 MOVE 0 10 14\n118 MOVE 0 11 14\n119 MOVE 0 11 13\n120 DIG 0 11 13\n121 DIG 0 11 13\n",
        "115 MOVE 1 17 1\n116 DIG 1 17 1\n",
        "117 MOVE 1 17 2\n118 DIG 1 17 2\n119 DIG 1 17 2\n",
        "120 MOVE 1 16 2\n121 DIG 1 16 2\n122 DIG 1 16 2\n",
        "122 MOVE 0 12 13\n123 DIG 0 12 13\n",
        "123 MOVE 1 15 2\n124 DIG 1 15 2\n125 DIG 1 15 2\n",
        "124 MOVE 0 12 12\n125 DIG 0 12 12\n",
        "126 MOVE 0 13 12\n127 MOVE 0 13 11\n128 DIG 0 13 11\n",
        "126 MOVE 1 16 2\n127 MOVE 1 17 2\n128 MOVE 1 18 2\n129 DIG 1 18 2\n130 DIG 1 18 2\n",
        "129 MOVE 0 14 11\n130 MOVE 0 14 12\n131 DIG 0 14 12\n132 DIG 0 14 12\n",
        "131 MOVE 1 18 3\n132 DIG 1 18 3\n",
        "133 MOVE 0 15 12\n134 DIG 0 15 12\n",
        "133 MOVE 1 19 3\n134 DIG 1 19 3\n135 DIG 1 19 3\n",
        "135 MOVE 0 15 13\n136 DIG 0 15 13\n137 DIG 0 15 13\n",
        "136 MOVE 1 19 2\n137 MOVE 1 19 1\n138 DIG 1 19 1\n139 DIG 1 19 1\n",
        "138 MOVE 0 16 13\n139 DIG 0 16 13\n",
        "140 MOVE 0 16 14\n141 DIG 0 16 14\n",
        "140 MOVE 1 19 0\n141 DIG 1 19 0\n",
        "142 MOVE 0 15 14\n143 DIG 0 15 14\n",
        "142 MOVE 1 18 0\n143 MOVE 1 17 0\n144 MOVE 1 17 1\n145 MOVE 1 17 2\n146 MOVE 1 17 3\n147 DIG 1 17 3\n",
        "144 MOVE 0 14 14\n145 DIG 0 14 14\n146 DIG 0 14 14\n",
        "147 MOVE 0 13 14\n148 DIG 0 13 14\n",
        "148 MOVE 1 18 3\n149 MOVE 1 18 4\n150 MOVE 1 18 5\n151 DIG 1 18 5\n",
        "149 MOVE 0 14 14\n150 MOVE 0 14 15\n151 MOVE 0 14 16\n152 DIG 0 14 16\n153 DIG 0 14 16\n",
        "152 MOVE 1 18 6\n153 DIG 1 18 6\n154 DIG 1 18 6\n",
        "154 MOVE 0 15 16\n155 MOVE 0 16 16\n156 MOVE 0 16 15\n157 DIG 0 16 15\n158 DIG 0 16 15\n",
        "155 MOVE 1 17 6\n156 DIG 1 17 6\n157 DIG 1 17 6\n",
        "158 MOVE 1 17 7\n159 DIG 1 17 7\n160 DIG 1 17 7\n",
        "159 MOVE 0 17 15\n160 MOVE 0 18 15\n161 MOVE 0 18 16\n162 DIG 0 18 16\n",
        "161 MOVE 1 18 7\n162 DIG 1 18 7\n",
        "163 MOVE 0 18 15\n164 MOVE 0 18 14\n165 MOVE 0 18 13\n166 DIG 0 18 13\n167 DIG 0 18 13\n",
        "163 MOVE 1 19 7\n164 DIG 1 19 7\n165 DIG 1 19 7\n",
        "166 MOVE 1 19 8\n167 MOVE 1 19 9\n168 DIG 1 19 9\n",
        "168 MOVE 0 19 13\n169 DIG 0 19 13\n",
        "169 MOVE 1 19 10\n170 DIG 1 19 10\n171 DIG 1 19 10\n",
        "170 MOVE 0 18 13\n171 MOVE 0 18 12\n172 MOVE 0 18 11\n173 DIG 0 18 11\n174 DIG 0 18 11\n",
        "172 MOVE 1 18 10\n173 MOVE 1 17 10\n174 MOVE 1 17 9\n175 DIG 1 17 9\n",
        "175 MOVE 0 17 11\n176 DIG 0 17 11\n177 DIG 0 17 11\n",
        "176 MOVE 1 16 9\n177 MOVE 1 16 10\n178 DIG 1 16 10\n179 DIG 1 16 10\n",
        "178 MOVE 0 16 11\n179 DIG 0 16 11\n180 DIG 0 16 11\n",
        "180 MOVE 1 15 10\n181 MOVE 1 14 10\n182 MOVE 1 13 10\n183 MOVE 1 12 10\n184 MOVE 1 12 9\n185 MOVE 1 12 8\n186 DIG 1 12 8\n187 DIG 1 12 8\n",
        "181 MOVE 0 15 11\n182 MOVE 0 14 11\n183 MOVE 0 13 11\n184 MOVE 0 12 11\n185 MOVE 0 11 11\n186 MOVE 0 11 10\n187 MOVE 0 11 9\n188 DIG 0 11 9\n",
        "188 MOVE 1 11 8\n189 MOVE 1 11 7\n190 DIG 1 11 7\n191 DIG 1 11 7\n",
        "189 MOVE 0 11 8\n190 MOVE 0 11 7\n191 MOVE 0 11 6\n192 MOVE 0 11 5\n193 DIG 0 11 5\n194 DIG 0 11 5\n",
        "192 MOVE 1 10 7\n193 MOVE 1 10 6\n194 MOVE 1 10 5\n195 MOVE 1 10 4\n196 DIG 1 10 4\n",
        "195 MOVE 0 12 5\n196 MOVE 0 12 4\n197 DIG 0 12 4\n198 DIG 0 12 4\n",
        "197 MOVE 1 10 3\n198 DIG 1 10 3\n199 DIG 1 10 3\n",
        "199 MOVE 0 11 4\n200 MOVE 0 11 3\n201 MOVE 0 11 2\n202 DIG 0 11 2\n203 DIG 0 11 2\n",
        "200 MOVE 1 9 3\n201 MOVE 1 9 2\n202 DIG 1 9 2\n",
        "203 MOVE 1 9 1\n204 DIG 1 9 1\n205 DIG 1 9 1\n",
        "204 MOVE 0 11 1\n205 DIG 0 11 1\n206 DIG 0 11 1\n",
        "206 MOVE 1 9 0\n207 DIG 1 9 0\n",
        "207 MOVE 0 10 1\n208 MOVE 0 9 1\n209 MOVE 0 8 1\n210 MOVE 0 7 1\n211 MOVE 0 7 0\n212 DIG 0 7 0\n",
        "208 MOVE 1 8 0\n209 MOVE 1 7 0\n210 MOVE 1 6 0\n211 MOVE 1 6 1\n212 DIG 1 6 1\n213 DIG 1 6 1\n",
        "213 MOVE 0 6 0\n214 MOVE 0 5 0\n215 MOVE 0 5 1\n216 DIG 0 5 1\n",
        "214 MOVE 1 5 1\n215 MOVE 1 4 1\n216 DIG 1 4 1\n217 DIG 1 4 1\n",
        "217 MOVE 0 4 1\n218 MOVE 0 3 1\n219 MOVE 0 3 0\n220 DIG 0 3 0\n221 DIG 0 3 0\n",
        "218 MOVE 1 5 1\n219 MOVE 1 6 1\n220 MOVE 1 7 1\n221 MOVE 1 7 2\n222 MOVE 1 7 3\n223 DIG 1 7 3\n224 DIG 1 7 3\n",
        "222 MOVE 0 4 0\n223 MOVE 0 5 0\n224 MOVE 0 6 0\n225 MOVE 0 7 0\n226 MOVE 0 8 0\n227 MOVE 0 9 0\n228 MOVE 0 9 1\n229 MOVE 0 9 2\n230 MOVE 0 9 3\n231 MOVE 0 9 4\n232 DIG 0 9 4\n",
        "225 MOVE 1 8 3\n226 MOVE 1 9 3\n227 MOVE 1 9 4\n228 MOVE 1 9 5\n229 DIG 1 9 5\n230 DIG 1 9 5\n",
        "231 MOVE 1 8 5\n232 MOVE 1 7 5\n233 MOVE 1 6 5\n234 MOVE 1 6 6\n235 MOVE 1 6 7\n236 MOVE 1 6 8\n237 MOVE 1 6 9\n238 DIG 1 6 9\n",
        "233 MOVE 0 10 4\n234 MOVE 0 10 5\n235 MOVE 0 10 6\n236 MOVE 0 10 7\n237 MOVE 0 10 8\n238 MOVE 0 10 9\n239 MOVE 0 10 10\n240 MOVE 0 10 11\n241 MOVE 0 10 12\n242 MOVE 0 10 13\n243 MOVE 0 10 14\n244 MOVE 0 10 15\n245 MOVE 0 10 16\n246 DIG 0 10 16\n",
        "239 MOVE 1 7 9\n240 MOVE 1 8 9\n241 MOVE 1 9 9\n242 MOVE 1 10 9\n243 MOVE 1 11 9\n244 MOVE 1 11 10\n245 MOVE 1 11 11\n246 MOVE 1 11 12\n247 MOVE 1 11 13\n248 MOVE 1 11 14\n249 MOVE 1 11 15\n250 MOVE 1 11 16\n251 DIG 1 11 16\n",
    ]

    date_01 = roadmap.recuperation_data("test/test_map_8.txt")
    map_01 = roadmap.mapping("test/test_map_8.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    number_truck = roadmap.nombre_de_camion(date_01)
    truck = roadmap.list_truck(number_truck)
    trajet = roadmap.trajet(matrice_map_01, truck)
    assert result == trajet


# test roadmap map 12
def test_write_map_12():
    roadmap.write_map(12, "test/test_sample_12.txt")
    assert filecmp.cmp("test/test_map_12.txt", "test/test_sample_12.txt") == True


def test_recuperation_data_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    data_02 = ["trucks: 6\n", "width: 12\n", "height: 13\n"]
    assert date_01 == data_02


def test_nb_camion_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    nb_camion = roadmap.nombre_de_camion(date_01)
    assert nb_camion == 6


def test_nb_hauteur_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    assert roadmap.height_map(date_01) == 13


def test_nb_largeur_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    assert roadmap.width_map(date_01) == 12


def test_map_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    result = [
        "  21 1 1 22 \n",
        "     212    \n",
        "   1      21\n",
        " 2    1   1 \n",
        "1 1 22     2\n",
        "2   2   2   \n",
        "         1 1\n",
        "1212        \n",
        "1 21   211  \n",
        "  21 1  2   \n",
        " 2    1 22  \n",
        "  121  2    \n",
        " 1 12 2  122\n",
    ]
    assert (
        roadmap.mapping("test/test_map_12.txt", roadmap.height_map(date_01)) == result
    )


def test_matrice_map_12():
    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    map_01 = roadmap.mapping("test/test_map_12.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    result = [
        {"x": 2, "y": 0, "dig": 2},
        {"x": 3, "y": 0, "dig": 1},
        {"x": 5, "y": 0, "dig": 1},
        {"x": 7, "y": 0, "dig": 1},
        {"x": 9, "y": 0, "dig": 2},
        {"x": 10, "y": 0, "dig": 2},
        {"x": 7, "y": 1, "dig": 2},
        {"x": 6, "y": 1, "dig": 1},
        {"x": 5, "y": 1, "dig": 2},
        {"x": 3, "y": 2, "dig": 1},
        {"x": 10, "y": 2, "dig": 2},
        {"x": 11, "y": 2, "dig": 1},
        {"x": 10, "y": 3, "dig": 1},
        {"x": 6, "y": 3, "dig": 1},
        {"x": 1, "y": 3, "dig": 2},
        {"x": 0, "y": 4, "dig": 1},
        {"x": 2, "y": 4, "dig": 1},
        {"x": 4, "y": 4, "dig": 2},
        {"x": 5, "y": 4, "dig": 2},
        {"x": 11, "y": 4, "dig": 2},
        {"x": 8, "y": 5, "dig": 2},
        {"x": 4, "y": 5, "dig": 2},
        {"x": 0, "y": 5, "dig": 2},
        {"x": 9, "y": 6, "dig": 1},
        {"x": 11, "y": 6, "dig": 1},
        {"x": 3, "y": 7, "dig": 2},
        {"x": 2, "y": 7, "dig": 1},
        {"x": 1, "y": 7, "dig": 2},
        {"x": 0, "y": 7, "dig": 1},
        {"x": 0, "y": 8, "dig": 1},
        {"x": 2, "y": 8, "dig": 2},
        {"x": 3, "y": 8, "dig": 1},
        {"x": 7, "y": 8, "dig": 2},
        {"x": 8, "y": 8, "dig": 1},
        {"x": 9, "y": 8, "dig": 1},
        {"x": 8, "y": 9, "dig": 2},
        {"x": 5, "y": 9, "dig": 1},
        {"x": 3, "y": 9, "dig": 1},
        {"x": 2, "y": 9, "dig": 2},
        {"x": 1, "y": 10, "dig": 2},
        {"x": 6, "y": 10, "dig": 1},
        {"x": 8, "y": 10, "dig": 2},
        {"x": 9, "y": 10, "dig": 2},
        {"x": 7, "y": 11, "dig": 2},
        {"x": 4, "y": 11, "dig": 1},
        {"x": 3, "y": 11, "dig": 2},
        {"x": 2, "y": 11, "dig": 1},
        {"x": 1, "y": 12, "dig": 1},
        {"x": 3, "y": 12, "dig": 1},
        {"x": 4, "y": 12, "dig": 2},
        {"x": 6, "y": 12, "dig": 2},
        {"x": 9, "y": 12, "dig": 1},
        {"x": 10, "y": 12, "dig": 2},
        {"x": 11, "y": 12, "dig": 2},
    ]

    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    assert matrice_map_01 == result


def test_trajet_map_12():
    result = [
        "0 MOVE 0 1 0\n1 MOVE 0 2 0\n2 DIG 0 2 0\n3 DIG 0 2 0\n",
        "0 MOVE 1 1 1\n1 MOVE 1 1 2\n2 MOVE 1 1 3\n3 DIG 1 1 3\n4 DIG 1 1 3\n",
        "0 MOVE 2 0 3\n1 MOVE 2 0 4\n2 DIG 2 0 4\n",
        "0 MOVE 3 0 4\n1 MOVE 3 0 5\n2 DIG 3 0 5\n3 DIG 3 0 5\n",
        "0 MOVE 4 1 4\n1 MOVE 4 2 4\n2 DIG 4 2 4\n",
        "0 MOVE 5 0 6\n1 MOVE 5 0 7\n2 DIG 5 0 7\n",
        "3 MOVE 2 1 4\n4 MOVE 2 2 4\n5 MOVE 2 3 4\n6 MOVE 2 4 4\n7 DIG 2 4 4\n8 DIG 2 4 4\n",
        "3 MOVE 4 3 4\n4 MOVE 4 3 3\n5 MOVE 4 3 2\n6 DIG 4 3 2\n",
        "3 MOVE 5 1 7\n4 DIG 5 1 7\n5 DIG 5 1 7\n",
        "4 MOVE 0 3 0\n5 DIG 0 3 0\n",
        "4 MOVE 3 0 6\n5 MOVE 3 0 7\n6 MOVE 3 0 8\n7 DIG 3 0 8\n",
        "5 MOVE 1 2 3\n6 MOVE 1 3 3\n7 MOVE 1 4 3\n8 MOVE 1 5 3\n9 MOVE 1 6 3\n10 DIG 1 6 3\n",
        "6 MOVE 0 4 0\n7 MOVE 0 5 0\n8 DIG 0 5 0\n",
        "6 MOVE 5 2 7\n7 DIG 5 2 7\n",
        "7 MOVE 4 4 2\n8 MOVE 4 5 2\n9 MOVE 4 5 1\n10 DIG 4 5 1\n11 DIG 4 5 1\n",
        "8 MOVE 3 1 8\n9 MOVE 3 2 8\n10 DIG 3 2 8\n11 DIG 3 2 8\n",
        "8 MOVE 5 3 7\n9 DIG 5 3 7\n10 DIG 5 3 7\n",
        "9 MOVE 0 6 0\n10 MOVE 0 7 0\n11 DIG 0 7 0\n",
        "9 MOVE 2 5 4\n10 DIG 2 5 4\n11 DIG 2 5 4\n",
        "11 MOVE 1 6 2\n12 MOVE 1 6 1\n13 DIG 1 6 1\n",
        "11 MOVE 5 3 8\n12 DIG 5 3 8\n",
        "12 MOVE 0 7 1\n13 DIG 0 7 1\n14 DIG 0 7 1\n",
        "12 MOVE 2 4 4\n13 MOVE 2 4 5\n14 DIG 2 4 5\n15 DIG 2 4 5\n",
        "12 MOVE 3 2 9\n13 DIG 3 2 9\n14 DIG 3 2 9\n",
        "12 MOVE 4 6 1\n13 MOVE 4 7 1\n14 MOVE 4 8 1\n15 MOVE 4 9 1\n16 MOVE 4 9 0\n17 DIG 4 9 0\n18 DIG 4 9 0\n",
        "13 MOVE 5 3 9\n14 DIG 5 3 9\n",
        "14 MOVE 1 7 1\n15 MOVE 1 8 1\n16 MOVE 1 9 1\n17 MOVE 1 10 1\n18 MOVE 1 10 0\n19 DIG 1 10 0\n20 DIG 1 10 0\n",
        "15 MOVE 0 8 1\n16 MOVE 0 9 1\n17 MOVE 0 10 1\n18 MOVE 0 10 2\n19 DIG 0 10 2\n20 DIG 0 10 2\n",
        "15 MOVE 3 1 9\n16 MOVE 3 1 10\n17 DIG 3 1 10\n18 DIG 3 1 10\n",
        "15 MOVE 5 4 9\n16 MOVE 5 5 9\n17 DIG 5 5 9\n",
        "16 MOVE 2 5 5\n17 MOVE 2 6 5\n18 MOVE 2 7 5\n19 MOVE 2 8 5\n20 DIG 2 8 5\n21 DIG 2 8 5\n",
        "18 MOVE 5 6 9\n19 MOVE 5 6 10\n20 DIG 5 6 10\n",
        "19 MOVE 3 2 10\n20 MOVE 3 2 11\n21 DIG 3 2 11\n",
        "19 MOVE 4 10 0\n20 MOVE 4 11 0\n21 MOVE 4 11 1\n22 MOVE 4 11 2\n23 DIG 4 11 2\n",
        "21 MOVE 0 10 3\n22 DIG 0 10 3\n",
        "21 MOVE 1 11 0\n22 MOVE 1 11 1\n23 MOVE 1 11 2\n24 MOVE 1 11 3\n25 MOVE 1 11 4\n26 DIG 1 11 4\n27 DIG 1 11 4\n",
        "21 MOVE 5 7 10\n22 MOVE 5 8 10\n23 DIG 5 8 10\n24 DIG 5 8 10\n",
        "22 MOVE 2 9 5\n23 MOVE 2 9 6\n24 DIG 2 9 6\n",
        "22 MOVE 3 3 11\n23 DIG 3 3 11\n24 DIG 3 3 11\n",
        "23 MOVE 0 11 3\n24 MOVE 0 11 4\n25 MOVE 0 11 5\n26 MOVE 0 11 6\n27 DIG 0 11 6\n",
        "24 MOVE 4 10 2\n25 MOVE 4 9 2\n26 MOVE 4 9 3\n27 MOVE 4 9 4\n28 MOVE 4 9 5\n29 MOVE 4 9 6\n30 MOVE 4 9 7\n31 MOVE 4 9 8\n32 DIG 4 9 8\n",
        "25 MOVE 2 8 6\n26 MOVE 2 8 7\n27 MOVE 2 8 8\n28 DIG 2 8 8\n",
        "25 MOVE 3 4 11\n26 DIG 3 4 11\n",
        "25 MOVE 5 8 9\n26 DIG 5 8 9\n27 DIG 5 8 9\n",
        "27 MOVE 3 4 12\n28 DIG 3 4 12\n29 DIG 3 4 12\n",
        "28 MOVE 0 10 6\n29 MOVE 0 9 6\n30 MOVE 0 8 6\n31 MOVE 0 7 6\n32 MOVE 0 7 7\n33 MOVE 0 7 8\n34 DIG 0 7 8\n35 DIG 0 7 8\n",
        "28 MOVE 1 10 4\n29 MOVE 1 9 4\n30 MOVE 1 9 5\n31 MOVE 1 9 6\n32 MOVE 1 9 7\n33 MOVE 1 9 8\n34 MOVE 1 9 9\n35 MOVE 1 9 10\n36 DIG 1 9 10\n37 DIG 1 9 10\n",
        "28 MOVE 5 7 9\n29 MOVE 5 7 10\n30 MOVE 5 7 11\n31 DIG 5 7 11\n32 DIG 5 7 11\n",
        "29 MOVE 2 9 8\n30 MOVE 2 9 9\n31 MOVE 2 9 10\n32 MOVE 2 9 11\n33 MOVE 2 9 12\n34 DIG 2 9 12\n",
        "30 MOVE 3 3 12\n31 DIG 3 3 12\n",
        "32 MOVE 3 2 12\n33 MOVE 3 1 12\n34 DIG 3 1 12\n",
        "33 MOVE 4 10 8\n34 MOVE 4 10 9\n35 MOVE 4 10 10\n36 MOVE 4 10 11\n37 MOVE 4 10 12\n38 DIG 4 10 12\n39 DIG 4 10 12\n",
        "33 MOVE 5 6 11\n34 MOVE 5 6 12\n35 DIG 5 6 12\n36 DIG 5 6 12\n",
        "35 MOVE 2 10 12\n36 MOVE 2 11 12\n37 DIG 2 11 12\n38 DIG 2 11 12\n",
    ]

    date_01 = roadmap.recuperation_data("test/test_map_12.txt")
    map_01 = roadmap.mapping("test/test_map_12.txt", roadmap.height_map(date_01))
    width = roadmap.width_map(date_01)
    matrice_map_01 = roadmap.matrice_de_la_map(map_01, width)
    number_truck = roadmap.nombre_de_camion(date_01)
    truck = roadmap.list_truck(number_truck)
    trajet = roadmap.trajet(matrice_map_01, truck)
    assert result == trajet
