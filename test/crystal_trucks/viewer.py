import argparse
import copy
import datetime

import arcade
import serial

# TODO faire une interface graphique pour choisir le port COM
# TODO mettre la grille dans une classe à part, ne mettre à jour la grille que si on change de tour, pour limiter les calculs

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Crystals VS Trucks"

trucks_images = (
    "images/towtruck.png",
    "images/transport.png",
    "images/truckdark.png",
    "images/truckdelivery.png",
    "images/firetruck.png",
    "images/truckcabin.png",
    "images/truck.png",
    "images/truckcabin_vintage.png",
    "images/suv_closed.png",
)

competition_turns = 0
competition_nb_crystals_left = 0


class Truck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movements = {}

    def move(self, turn, x, y):
        self.movements[turn] = (x, y)
        if not (self.x - 1 <= x <= self.x + 1 and self.y - 1 <= y <= self.y + 1):
            print(
                f"invalid move, too far away, turn {turn} to {x} {y} from {self.x} {self.y}"
            )
        if self.x < x:
            self.x += 1
        elif self.x > x:
            self.x -= 1
        elif self.y < y:
            self.y += 1
        elif self.y > y:
            self.y -= 1

    def position_at(self, clock):
        clock_turn = int(clock)
        ratio = clock - clock_turn
        to_turn = -2
        from_x, from_y = self.x, self.y
        # print(self.movements)
        for turn, (x, y) in sorted(self.movements.items()):
            if turn < clock_turn:
                from_x, from_y = x, y
            else:
                to_x, to_y, to_turn = x, y, turn
        # print(clock_turn, to_turn, "from", from_x, from_y)
        if to_turn == clock_turn:
            pos_x, pos_y = (
                from_x + (to_x - from_x) * ratio,
                from_y + (to_y - from_y) * ratio,
            )
        else:
            pos_x, pos_y = from_x, from_y
        # print("    ", self.x, self.y, pos_x, pos_y)
        return pos_x, pos_y


class CrystalsVsTrucksGameView(arcade.View):
    def __init__(self, window=None, commands=None):
        super().__init__(window)
        self.commands: CommandContent = commands
        self.grid = copy.deepcopy(commands.grid)
        self.trucks = [Truck(0, truck_id) for truck_id in range(commands.nb_trucks)]
        self.clock = 0
        self.clock_factor = 1
        self.running = True
        self.commands_history = {}

        arcade.set_background_color(arcade.color.AMAZON)

    @property
    def nb_crystals_left(self):
        if self.grid is not None:
            return sum(sum(line) for line in self.grid)
        return 0

    def position_to_px(self, x, y):
        return int((x + 0.5) * self.commands.cell_width), int(
            (y + 0.5) * self.commands.cell_height
        )

    def compute_sprites(self):
        self.crystal_list = arcade.SpriteList()
        for cell_x in range(self.commands.grid_width):
            for cell_y in range(self.commands.grid_height):
                if self.grid[cell_y][cell_x] > 0:
                    crystal_sprite = arcade.Sprite(
                        "images/element_blue_polygon_glossy.png", 0.5
                    )
                    x, y = self.position_to_px(cell_x, cell_y)
                    crystal_sprite.center_x = x - crystal_sprite.width // 2
                    crystal_sprite.center_y = y - crystal_sprite.height // 2 - 10
                    self.crystal_list.append(crystal_sprite)
                if self.grid[cell_y][cell_x] > 1:
                    crystal_sprite = arcade.Sprite(
                        "images/element_red_polygon_glossy.png", 0.5
                    )
                    x, y = self.position_to_px(cell_x, cell_y)
                    crystal_sprite.center_x = x - crystal_sprite.width // 2 + 10
                    crystal_sprite.center_y = y - crystal_sprite.height // 2 - 10 + 10
                    self.crystal_list.append(crystal_sprite)

        self.truck_list = arcade.SpriteList()
        for truck_id, truck in enumerate(self.trucks):
            truck_sprite = arcade.Sprite(trucks_images[truck_id], 1.5)
            x, y = self.position_to_px(*truck.position_at(self.clock))
            truck_sprite.center_x = x - truck_sprite.width // 2 + 10
            truck_sprite.center_y = y - truck_sprite.height // 2 - 10
            self.truck_list.append(truck_sprite)

    def setup(self):
        """Set up the game variables. Call to re-start the game."""
        self.compute_sprites()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.crystal_list.draw()
        self.truck_list.draw()

        arcade.draw_text(
            str(int(self.clock)),
            0,
            SCREEN_HEIGHT - 50,
            arcade.color.WHITE,
            font_size=40,
            align="center",
            width=SCREEN_WIDTH,
        )

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        def extract_time(command):
            return int(command[0])

        if self.running:
            self.clock += delta_time * self.clock_factor
        if (
            self.nb_crystals_left == 0
            or self.clock > self.commands.max_command_turn + 1
        ):
            score_view = ScoreView(
                self.window,
                turn=int(self.clock),
                nb_crystals_left=self.nb_crystals_left,
            )
            self.window.show_view(score_view)
        # print("new frame at", self.clock)
        self.grid = copy.deepcopy(self.commands.grid)
        self.trucks = [
            Truck(0, truck_id) for truck_id in range(self.commands.nb_trucks)
        ]
        for command in sorted(self.commands.commands, key=extract_time):
            time, command, *args = command
            time = int(time)
            if time < self.clock:
                self.interpret(time, command, args)

        # for truck_index, truck in enumerate(self.trucks):
        #     print(truck_index, truck.x, truck.y)

        self.compute_sprites()

    def interpret(self, turn, command, args):
        # print(turn, command, args)
        if args:
            truck_id = args[0]
            history = self.commands_history.get((turn, truck_id))
            if history is not None and history != (command, args):
                print(
                    "invalid command, the truck already did an action at turn",
                    turn,
                    command,
                    args,
                )
                # print(self.commands_history)
                return
            if not (0 <= int(truck_id) < self.commands.nb_trucks):
                print("invalid truck ID", command, args)
                return
            self.commands_history[(turn, truck_id)] = (command, args)
        if command == "MOVE":
            if len(args) != 3:
                print("invalid move command, must have 3 arguments", command, args)
                return
            truck_id, x, y = (int(a) for a in args)
            if not 0 <= truck_id < self.commands.nb_trucks:
                print("invalid move command, invalid truck id", command, args)
                return
            if not 0 <= x < self.commands.grid_width:
                print("invalid move command, invalid x", command, args)
                return
            if not 0 <= y < self.commands.grid_height:
                print("invalid move command, invalid y", command, args)
                return
            self.trucks[truck_id].move(turn, x, y)
        elif command == "DIG":
            if len(args) != 3:
                print("invalid dig command, must have 3 arguments", command, args)
                return
            truck_id, x, y = (int(a) for a in args)
            if not 0 <= truck_id < self.commands.nb_trucks:
                print("invalid dig command, invalid truck id", command, args)
                return
            if not 0 <= x < self.commands.grid_width:
                print("invalid dig command, invalid x", command, args)
                return
            if not 0 <= y < self.commands.grid_height:
                print("invalid dig command, invalid y", command, args)
                return
            truck = self.trucks[truck_id]
            truck.position_at(self.clock)
            if x != truck.x or y != truck.y:
                print("invalid dig command, cannot dig on non current position")
                print(f"    {truck_id=} {truck.x=} {truck.y=} dig at {x=} {y=}")
                return
            self.grid[y][x] = max(0, self.grid[y][x] - 1)
        else:
            print("invalid command", command, args)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.LEFT:
            self.clock = max(0, int(self.clock - 1))
        elif key == arcade.key.RIGHT:
            self.clock += 1
        elif key == arcade.key.UP:
            self.clock_factor *= 1.1
        elif key == arcade.key.DOWN:
            self.clock_factor /= 1.1
        elif key == arcade.key.SPACE:
            self.running = not self.running


class ScoreView(arcade.View):
    def __init__(self, window=None, nb_crystals_left=1000, turn=1000):
        global competition_nb_crystals_left, competition_turns
        super().__init__(window)
        self.nb_crystals_left = nb_crystals_left
        self.turn = turn
        competition_turns = turn
        competition_nb_crystals_left = nb_crystals_left

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        if args.competition:
            arcade.close_window()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Score",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 75,
            arcade.color.BLACK,
            font_size=50,
            anchor_x="center",
        )
        plural = "s" if self.nb_crystals_left > 1 else ""
        arcade.draw_text(
            f"{self.nb_crystals_left} crystal{plural} left",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arcade.color.GRAY,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            f"after {self.turn} turns",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 75,
            arcade.color.GRAY,
            font_size=20,
            anchor_x="center",
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = CrystalsVsTrucksGameView(self.window, commands=commands)
        self.window.show_view(game_view)
        game_view.setup()


class CommandContent:
    def __init__(self, path=None, serial_port=None):
        if path is None and serial_port is None:
            print("Either file path or serial port must be configured")
        self.commands = []
        self.nb_trucks = 0
        self.grid_width = 0
        self.grid_height = 0
        self.grid = []
        self.cell_width = 0
        self.cell_height = 0
        self._max_command_turn = None

        lines = []
        if path is not None:
            with open(path, encoding="utf-8") as file:
                lines = list(file)
        if serial_port is not None:
            print("waiting for data on", serial_port)
            filename = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
            filename = f"serial_{filename}.txt"
            with serial.Serial(serial_port, 115200, timeout=1) as ser, open(
                filename, "w", encoding="utf-8"
            ) as log:
                nb_empty_lines = 0
                while True:
                    if nb_empty_lines > 10:
                        break
                    line = ser.readline().decode("utf-8").rstrip()
                    if line:
                        print(line)
                        log.write(line)
                        log.write("\r\n")
                        lines.append(line)
                        nb_empty_lines = 0
                    else:
                        nb_empty_lines += 1
        self._read_config(lines)

    def _read_config(self, lines):
        in_grid = False
        for line in lines:
            line = line.rstrip()
            if in_grid and not line.startswith("### End Grid ###"):
                self.grid.append([])
                for char in line:
                    if char == " ":
                        self.grid[-1].append(0)
                    else:
                        self.grid[-1].append(int(char))
                for _ in range(len(self.grid[-1]), self.grid_width):
                    self.grid[-1].append(0)
            elif line.startswith("### End Grid ###"):
                in_grid = False
            elif line.startswith("trucks: "):
                self.nb_trucks = int(line.split()[-1])
            elif line.startswith("width: "):
                self.grid_width = int(line.split()[-1])
                self.cell_width = SCREEN_WIDTH // self.grid_width
            elif line.startswith("height: "):
                self.grid_height = int(line.split()[-1])
                self.cell_height = SCREEN_HEIGHT // self.grid_height
            elif line.startswith("### Grid ###"):
                in_grid = True
            else:
                parts = line.split()
                if len(parts) != 5 or parts[1] not in ("DIG", "MOVE"):
                    print("ignore", line, end="")
                else:
                    self.commands.append(parts)

    @property
    def max_command_turn(self):
        if self._max_command_turn is None:
            last_command = max(self.commands, key=lambda c: int(c[0]))
            self._max_command_turn = int(last_command[0])
        return self._max_command_turn


commands = None
args = None


def main():
    """Main function"""
    global commands, args
    parser = argparse.ArgumentParser(description="Viewer for crystals vs trucks.")
    input_parser = parser.add_mutually_exclusive_group(required=True)
    input_parser.add_argument(
        "-i",
        "--input",
        metavar="PATH",
        type=str,
        help="path of the file containing commands",
        default=None,
    )
    input_parser.add_argument(
        "-s",
        "--serial-port",
        metavar="COM1",
        type=str,
        help="name of the serial device (115200 8N1)",
        default=None,
    )
    parser.add_argument(
        "-c",
        "--competition",
        action="store_true",
        help="competition mode, gives only the score",
    )
    args = parser.parse_args()
    commands = CommandContent(path=args.input, serial_port=args.serial_port)

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = CrystalsVsTrucksGameView(commands=commands)
    window.show_view(game_view)
    game_view.setup()
    if args.competition:
        game_view.clock = commands.max_command_turn
    arcade.run()
    if args.competition:
        print()
        print("turns:", competition_turns)
        print("nb_crystals_left:", competition_nb_crystals_left)


if __name__ == "__main__":
    main()
