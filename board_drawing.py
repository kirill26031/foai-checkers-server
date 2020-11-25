import time

import tkinter

from main import game


# Board Drawing manager
class BDManager:
    # Properties
    _needsUpdate = True

    def __init__(self):
        # Initialize parameters
        self.ROWS = 8
        self.COLS = 8
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.col_width = self.WINDOW_WIDTH / self.COLS
        self.row_height = self.WINDOW_HEIGHT / self.ROWS
        # Game
        self.game = game
        # Drawing
        self._draw_board_only()
        # self.update_board()
        # while not self.game.is_over():
        #     self.root.update()
        #     print(self.game.is_over())
        #     time.sleep(0.5)
        self.root.mainloop()

    def _draw_board_only(self):
        self.root = tkinter.Tk()
        self.c = tkinter.Canvas(self.root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, borderwidth=5,
                                background='white')
        self.c.pack()
        self.tiles = set()

        # Print dark square
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if (i + j) % 2 == 1:
                    self.c.create_rectangle(i * self.row_height, j * self.col_width,
                                            (i + 1) * self.row_height, (j + 1) * self.col_width, fill="gray",
                                            outline="gray")

        # Print grid lines
        for i in range(self.ROWS):
            self.c.create_line(0, self.row_height * i, self.WINDOW_WIDTH, self.row_height * i, width=2)
            self.c.create_line(self.col_width * i, 0, self.col_width * i, self.WINDOW_HEIGHT, width=2)

        # Place checks on the board
        self.update_board()

    def update_board(self):
        if self.game.is_over():
            return
        # if not self._needsUpdate:
        #   return
        # remove old pieces
        for tile in self.tiles:
            self.c.delete(tile)
        self.tiles -= self.tiles
        # draw new
        for piece in self.game.board.pieces:
            if piece.captured:
                continue

            color = "red" if piece.player == 2 else "black"
            i = piece.get_row()
            j = piece.get_column() * 2 + 1 if i % 2 == 0 else piece.get_column() * 2
            tile = self.c.create_oval(j * self.col_width + 10, i * self.row_height + 10,
                                      (j + 1) * self.col_width - 10, (i + 1) * self.row_height - 10,
                                      fill=color)
            self.tiles.add(tile)
            self.c.tag_raise(tile)

        self._needsUpdate = False
        # make GUI updates board every second
        self.root.after(200, self.update_board)
        print("UI updated")

    def set_needs_update(self):
        self._needsUpdate = True
