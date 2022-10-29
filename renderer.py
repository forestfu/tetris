from turtle import Turtle
from random import choice

PIECE_TEMPLATES = {
    1: [[0, 1, 1, 1, 2, 1, 3, 1],
        [2, 0, 2, 1, 2, 2, 2, 3],
        [0, 2, 1, 2, 2, 2, 3, 2],
        [1, 0, 1, 1, 1, 2, 1, 3]],
    2: [[0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 1]],
    3: [[1, 0, 0, 1, 1, 1, 2, 1],
        [1, 0, 1, 1, 1, 2, 2, 1],
        [0, 1, 1, 1, 2, 1, 1, 2],
        [1, 0, 1, 1, 1, 2, 0, 1]],
    4: [[0, 1, 1, 1, 1, 0, 2, 0],
        [1, 0, 1, 1, 2, 1, 2, 2],
        [0, 2, 1, 2, 1, 1, 2, 1],
        [0, 0, 0, 1, 1, 1, 1, 2]],
    5: [[0, 0, 1, 0, 1, 1, 2, 1],
        [2, 0, 2, 1, 1, 1, 1, 2],
        [0, 1, 1, 1, 1, 2, 2, 2],
        [1, 0, 1, 1, 0, 1, 0, 2]],
    6: [[0, 0, 0, 1, 1, 1, 2, 1],
        [2, 0, 1, 0, 1, 1, 1, 2],
        [0, 1, 1, 1, 2, 1, 2, 2],
        [1, 0, 1, 1, 1, 2, 0, 2]],
    7: [[0, 1, 1, 1, 2, 1, 2, 0],
        [1, 0, 1, 1, 1, 2, 2, 2],
        [2, 1, 1, 1, 0, 1, 0, 2],
        [0, 0, 1, 0, 1, 1, 1, 2]]
}
KICK_X = [0, 1, 1, 0, 1, 0, -1, -1, 0, -1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, -1, -1, 0, -1, 0, 1, 1, 0, 1, 0, -1, -1, 0,
          -1, 0, -1, -1, 0, -1, 0, -1, 2, -1, 2, 0, -2, 1, -2, 1, 0, 2, -1, 2, -1, 0, -1, 2, -1, 2, 0, 1, -2, 1, -2, 0,
          2, -1, 2, -1, 0, -2, 1, -2, 1, 0, 1, -2, 1, -2]
KICK_Y = [0, 0, 1, -2, -2, 0, 0, 1, -2, -2, 0, 0, -1, 2, 2, 0, 0, -1, 2, 2, 0, 0, 1, -2, -2, 0, 0, 1, -2, -2, 0, 0, -1,
          2, 2, 0, 0, -1, 2, 2, 0, 0, 0, 2, -1, 0, 0, 0, -1, 2, 0, 0, 0, 1, -2, 0, 0, 0, 2, -1, 0, 0, 0, -2, 1, 0, 0, 0,
          1, -2, 0, 0, 0, -1, 2, 0, 0, 0, -2, 1]


class Renderer(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.game_over = False
        self.grid = [[0] * 10 for _ in range(22)]
        self.GRID_SIZE = 20
        self.piece_fall_timer = 0
        self.piece_fall_speed = 18
        self.piece_x = 0
        self.piece_y = 0
        self.piece_rotation = 0
        self.piece_type = 1
        self.random_bag = []
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.s = False
        self.key_hold_frames = {
            "right": -1,
            "left": -1,
            "up": -1,
            "space": -1,
            "s": -1,
        }
        self.score = 0
        self.level = 0
        self.lines_cleared = 0
        self.held_piece = 0
        self.changed = False
        self.next_piece = 0

    def reset_grid(self):
        self.grid = [[0] * 10 for _ in range(22)]

    def reset_key_frames(self):
        self.key_hold_frames = {
            "right": -1,
            "left": -1,
            "up": -1,
            "space": -1,
        }

    def render_grid(self):

        # render grid border and grid list
        self.clear()
        self.pensize(4)
        self.pencolor("black")
        self.penup()
        self.goto(5 * self.GRID_SIZE + 3, 12 * self.GRID_SIZE)
        self.pendown()
        self.goto(5 * self.GRID_SIZE + 3, -12 * self.GRID_SIZE - 3)
        self.goto(-5 * self.GRID_SIZE - 2, -12 * self.GRID_SIZE - 3)
        self.goto(-5 * self.GRID_SIZE - 2, 12 * self.GRID_SIZE)
        self.goto(5 * self.GRID_SIZE + 3, 12 * self.GRID_SIZE)
        self.goto(0, 12 * self.GRID_SIZE)
        self.goto(0, 8 * self.GRID_SIZE + 2)
        self.goto(-5 * self.GRID_SIZE - 2, 8 * self.GRID_SIZE + 2)
        self.goto(5 * self.GRID_SIZE + 2, 8 * self.GRID_SIZE + 2)
        self.penup()

        for y in range(2, len(self.grid)):
            for x in range(len(self.grid[0])):
                self.render_tile(x, y, self.grid[y][x])

        # render the piece currently in the air
        piece_coordinates = self.get_piece_coordinates(self.piece_x, self.piece_y, self.piece_rotation, self.piece_type)
        for x, y in zip(piece_coordinates["x"], piece_coordinates["y"]):
            if y > 1:
                self.render_tile(x, y, self.piece_type)

        # render held piece
        if self.held_piece != 0:
            if self.held_piece == 1:
                piece_coordinates = self.get_piece_coordinates(5.5, -1.5, 0, self.held_piece)
            elif self.held_piece == 2:
                piece_coordinates = self.get_piece_coordinates(6.5, -1, 0, self.held_piece)
            else:
                piece_coordinates = self.get_piece_coordinates(6, -1, 0, self.held_piece)
            for x, y in zip(piece_coordinates["x"], piece_coordinates["y"]):
                self.render_tile(x, y, self.held_piece)

        if self.next_piece != 0:
            if self.next_piece == 1:
                piece_coordinates = self.get_piece_coordinates(0.5, -1.5, 0, self.next_piece)
            elif self.next_piece == 2:
                piece_coordinates = self.get_piece_coordinates(1.5, -1, 0, self.next_piece)
            else:
                piece_coordinates = self.get_piece_coordinates(1, -1, 0, self.next_piece)
            for x, y in zip(piece_coordinates["x"], piece_coordinates["y"]):
                self.render_tile(x, y, self.next_piece)

        # render score
        self.goto(0, 250)
        self.color("grey")
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))

    def render_tile(self, x, y, type):
        if not type == 0:
            self.color("black")
            self.goto(-5 * self.GRID_SIZE + (x + 0.5) * self.GRID_SIZE,
                      8 * self.GRID_SIZE - (y - 1.5) * self.GRID_SIZE)
            self.stamp()
            if type == 1:
                self.color("cyan")
            if type == 2:
                self.color("yellow")
            if type == 3:
                self.color("magenta")
            if type == 4:
                self.color("lime green")
            if type == 5:
                self.color("red")
            if type == 6:
                self.color("blue")
            if type == 7:
                self.color("orange")
            self.shapesize(0.9, 0.9)
            self.stamp()
            self.shapesize(1, 1)

    def get_piece_coordinates(self, x, y, rotation, type):
        piece_template = PIECE_TEMPLATES[type][rotation]
        piece_tile_coordinates = {"x": [], "y": []}
        for i in range(0, 8, 2):
            piece_tile_coordinates["x"].append(piece_template[i] + x)
            piece_tile_coordinates["y"].append(piece_template[i + 1] + y)
        return piece_tile_coordinates

    def generate_piece(self):
        self.changed = False
        if not self.random_bag:
            self.random_bag = [i for i in range(1, 8)]
        self.piece_type = self.next_piece
        if self.piece_type == 0:
            self.piece_type = choice(self.random_bag)
            self.random_bag.remove(self.piece_type)
        self.next_piece = choice(self.random_bag)
        self.random_bag.remove(self.next_piece)
        self.piece_y = 1
        self.piece_x = 3
        if self.piece_type == 2:
            self.piece_x = 4
        self.piece_rotation = 0
        if not self.is_piece_valid(self.piece_x, self.piece_y, self.piece_rotation, self.piece_type):
            self.clear()
            self.goto(0, 0)
            self.color("grey")
            self.write("Game Over!", align="center", font=("Courier", 60, "bold"))
            self.goto(-4, 4)
            self.color("red3")
            self.write("Game Over!", align="center", font=("Courier", 60, "bold"))
            self.goto(0, -50)
            self.color("grey")
            self.write(f"Score: {self.score}", align="center", font=("Courier", 45, "bold"))
            self.goto(-4, -46)
            self.color("black")
            self.write(f"Score: {self.score}", align="center", font=("Courier", 45, "bold"))
            self.game_over = True

    def update_falling_piece(self):
        self.piece_fall_timer += 1
        if self.key_hold_frames["space"] == 0:
            while self.is_piece_valid(self.piece_x, self.piece_y, self.piece_rotation, self.piece_type):
                self.piece_y += 1
            self.piece_y -= 1
            self.store_piece_to_grid(self.piece_x, self.piece_y, self.piece_rotation, self.piece_type)
            self.clear_filled_rows()
            self.generate_piece()
            self.piece_fall_timer = 0
        else:
            if self.key_hold_frames["right"] % 2 == 0 and not str(self.key_hold_frames["right"]) in "24":
                if self.is_piece_valid(self.piece_x + 1, self.piece_y, self.piece_rotation, self.piece_type):
                    self.piece_x += 1

            if self.key_hold_frames["left"] % 2 == 0 and not str(self.key_hold_frames["left"]) in "24":
                if self.is_piece_valid(self.piece_x - 1, self.piece_y, self.piece_rotation, self.piece_type):
                    self.piece_x -= 1

            if self.key_hold_frames["up"] == 0:
                self.rotate_piece(1)

            if self.key_hold_frames["s"] == 0 and not self.changed:
                self.swap_held_piece()

            if self.piece_fall_timer > self.piece_fall_speed or self.down:
                if self.is_piece_valid(self.piece_x, self.piece_y + 1, self.piece_rotation, self.piece_type):
                    self.piece_y += 1
                else:
                    self.store_piece_to_grid(self.piece_x, self.piece_y, self.piece_rotation, self.piece_type)
                    self.clear_filled_rows()
                    self.generate_piece()
                self.piece_fall_timer = 0

    def is_piece_valid(self, x, y, rotation, type):
        piece_coordinates = self.get_piece_coordinates(x, y, rotation, type)
        is_valid = True
        for piece_x, piece_y in zip(piece_coordinates["x"], piece_coordinates["y"]):
            if piece_y > 21 or piece_x > 9 or piece_x < 0 or not self.grid[piece_y][piece_x] == 0:
                is_valid = False
        return is_valid

    def store_piece_to_grid(self, x, y, rotation, type):
        piece_coordinates = self.get_piece_coordinates(x, y, rotation, type)
        for piece_x, piece_y in zip(piece_coordinates["x"], piece_coordinates["y"]):
            self.grid[piece_y][piece_x] = type

    def clear_filled_rows(self):
        filled_rows = self.find_filled_rows()
        for idx in filled_rows:
            self.grid.pop(idx)
            self.grid.insert(0, [0] * 10)
        if len(filled_rows) == 1:
            self.score += 40 * (self.level + 1)
        elif len(filled_rows) == 2:
            self.score += 100 * (self.level + 1)
        elif len(filled_rows) == 3:
            self.score += 300 * (self.level + 1)
        elif len(filled_rows) == 4:
            self.score += 1200 * (self.level + 1)
        self.lines_cleared += len(filled_rows)
        self.level = self.lines_cleared // 10
        self.piece_fall_speed = 18 - 2 * self.level
        if self.piece_fall_speed < 0:
            self.piece_fall_speed = 0

    def find_filled_rows(self):
        return [idx for row, idx in zip(self.grid, range(22)) if 0 not in row]

    def update_key_frames(self):
        if self.right:
            self.key_hold_frames["right"] += 1
        else:
            self.key_hold_frames["right"] = -1

        if self.left:
            self.key_hold_frames["left"] += 1
        else:
            self.key_hold_frames["left"] = -1

        if self.up:
            self.key_hold_frames["up"] += 1
        else:
            self.key_hold_frames["up"] = -1

        if self.space:
            self.key_hold_frames["space"] += 1
        else:
            self.key_hold_frames["space"] = -1

        if self.s:
            self.key_hold_frames["s"] += 1
        else:
            self.key_hold_frames["s"] = -1

    def rotate_piece(self, direction):
        idx = 0
        if self.piece_type == 1:
            idx += 40
        idx += self.piece_rotation * 10
        if direction == 1:
            idx += 5
        for idx in range(idx, idx + 5):
            if self.is_piece_valid(self.piece_x + KICK_X[idx], self.piece_y + KICK_Y[idx],
                                   (self.piece_rotation + direction) % 4, self.piece_type):
                self.piece_x += KICK_X[idx]
                self.piece_y += KICK_Y[idx]
                self.piece_rotation = (self.piece_rotation + direction) % 4
                break

    def swap_held_piece(self):
        last_piece = self.piece_type
        self.piece_type = self.held_piece
        self.held_piece = last_piece
        self.piece_x = 3
        self.piece_y = 1
        if self.piece_type == 2:
            self.piece_x = 4
        if self.piece_type == 0:
            self.generate_piece()
        self.changed = True

    def move_right(self):
        if self.is_piece_valid(self.piece_x + 1, self.piece_y, self.piece_rotation, self.piece_type):
            self.piece_x += 1

    def move_left(self):
        if self.is_piece_valid(self.piece_x - 1, self.piece_y, self.piece_rotation, self.piece_type):
            self.piece_x -= 1

    def right_pressed(self):
        self.right = True

    def right_release(self):
        self.right = False

    def left_pressed(self):
        self.left = True

    def left_release(self):
        self.left = False

    def up_pressed(self):
        self.up = True

    def up_release(self):
        self.up = False

    def down_pressed(self):
        self.down = True

    def down_release(self):
        self.down = False

    def space_pressed(self):
        self.space = True

    def space_release(self):
        self.space = False

    def s_pressed(self):
        self.s = True

    def s_release(self):
        self.s = False
