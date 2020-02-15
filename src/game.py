import random
from tkinter import Frame, Label, CENTER

import helper


GRID_BACKGROUND_COLOR = "#92877d"
BACKGROUND_COLOR = "#9e948a"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",

                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", }

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2",

                   4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                   32768: "#776e65", 65536: "#f9f6f2", }

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"


class GridCreator(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {
                        KEY_UP: helper.up,
                        KEY_DOWN: helper.down,
                        KEY_LEFT: helper.left,
                        KEY_RIGHT: helper.right,
                        }
        
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        """
        initialize new 4x4 empty grid
        """
        background = Frame(self, bg=GRID_BACKGROUND_COLOR)
        background.grid()

        # iterate over grid (row, column) wise (typically 2048 is of 4x4 grid)
        for i in range(4):
            grid_row = []
            for j in range(4):
                cell = Frame(background, bg=BACKGROUND_COLOR)
                cell.grid(row=i, column=j, padx=5, pady=5)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR, font=("Times New Roman", 20), width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def gen(self):
        """
        Returns:
            position between 0-3 (used for random row/column position)
        """
        return random.randint(0, 3) # 3 because grid length - 1

    def init_matrix(self):
        """
        Create matrix of values with two randomly placed numbers
        """
        self.matrix = helper.new_game(4)
        self.matrix = helper.add_two(self.matrix)
        self.matrix = helper.add_two(self.matrix)

    def update_grid_cells(self):
        """
        Update values in the grid
        """
        for i in range(4):
            for j in range(4):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=BACKGROUND_COLOR)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=BACKGROUND_COLOR_DICT[new_number],
                        fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        """
        take appropriate action on the corresponding key events
        parameters:
            event - key press event
        """
        key = repr(event.char)
        if key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = helper.add_two(self.matrix)
                self.update_grid_cells()
                done = False
                if helper.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(
                        text="You", bg=BACKGROUND_COLOR)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=BACKGROUND_COLOR)
                if helper.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(
                        text="You", bg=BACKGROUND_COLOR)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=BACKGROUND_COLOR)

    def generate_next(self):
        "Generate value in the matrix randomly on any up/down/left/right key event"
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


if __name__ == "__main__":
    GridCreator()
