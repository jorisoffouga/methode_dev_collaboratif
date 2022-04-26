class Truck:
    def __init__(
        self,
        id,
        curent_pos,
    ):
        self.id = id
        self.curent_pos = curent_pos
        self.destination = None
        self.etat = 0
        self.turn = -1

    def print_usage(self):
        print(f"ID truck : {self.id} -- position {self.curent_pos}")

    def nombre_turn(self):
        return self.turn

    def recherche_du_plus_proche(self, matrice_map):
        norme_mini = 10000
        i = 0
        best_index = 0

        for elem in matrice_map:

            if elem == self.curent_pos:
                pass
            else:

                norme = abs(self.curent_pos["x"] - elem["x"]) + abs(
                    self.curent_pos["y"] - elem["y"]
                )

                if norme < norme_mini:
                    norme_mini = norme
                    best_index = i

                i += 1
        return best_index

    def nombre_tour_deplacement(self, distination):
        return abs(self.curent_pos["x"] - distination["x"]) + abs(
            self.curent_pos["y"] - distination["y"]
        )

    def move(self, destination):

        result = ""

        for turn in range(self.nombre_tour_deplacement(destination)):
            self.turn += 1
            nombre_deplacement_x = destination["x"] - self.curent_pos["x"]
            nombre_deplacement_y = destination["y"] - self.curent_pos["y"]

            if nombre_deplacement_x < 0:
                self.curent_pos["x"] -= 1
                result += f"{self.turn} MOVE {self.id} {self.curent_pos['x']} {self.curent_pos['y']}\n"
            elif nombre_deplacement_x > 0:
                self.curent_pos["x"] += 1
                result += f"{self.turn} MOVE {self.id} {self.curent_pos['x']} {self.curent_pos['y']}\n"

            elif nombre_deplacement_y < 0:
                self.curent_pos["y"] -= 1
                result += f"{self.turn} MOVE {self.id} {self.curent_pos['x']} {self.curent_pos['y']}\n"
            elif nombre_deplacement_y > 0:
                self.curent_pos["y"] += 1
                result += f"{self.turn} MOVE {self.id} {self.curent_pos['x']} {self.curent_pos['y']}\n"
            else:
                break
        for dig in range(destination["dig"]):
            self.turn += 1
            result += f"{self.turn} DIG {self.id} {self.curent_pos['x']} {self.curent_pos['y']}\n"

        return result
