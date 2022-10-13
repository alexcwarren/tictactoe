import abc
import logging
import logging.config
import tkinter as tk
from functools import partial


class TicTacToe_View(abc.ABC):
    SIZE = 3

    def __init__(self):
        self.__setup_config()
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        import components.tictactoe_controller as ttt_controller

        self.__controller: ttt_controller = controller

    def __setup_config(self):
        logging.config.fileConfig(fname="log.conf", disable_existing_loggers=False)
        self.logger = logging.getLogger("View")

    def render(self):
        pass


class TicTacToe_TestView(TicTacToe_View):
    def __init__(self):
        super().__init__()


class TicTacToe_GUIView(tk.Tk, TicTacToe_View):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.font = "Arial"
        self.MINWIDTH = "400"
        self.MINHEIGHT = "400"
        self.minsize(self.MINWIDTH, self.MINHEIGHT)
        self.geometry(f"{self.MINWIDTH}x{self.MINHEIGHT}")
        # Center horizontally in column 0
        self.columnconfigure(0, weight=1)
        self.__build_menu_bar()
        self.__build_board()
        self.__is_game_over: bool = False

    def __build_menu_bar(self):
        pass

    def __build_board(self):
        self.board_frame = tk.Frame(self)
        self.board_frame_row = 0
        self.board_frame.rowconfigure(self.board_frame_row, weight=1, minsize=50)
        self.board_frame.grid(row=self.board_frame_row, column=0)
        self.current_player_label = tk.Label(self.board_frame)
        self.current_player_label.grid(row=0, column=0)

        self.grid_frame = tk.Frame(self)
        self.grid_frame_row = self.board_frame_row + 1
        self.grid_frame.grid(row=self.grid_frame_row, column=0)
        self.grid: list[tk.Button] = []
        self.button_minwidth = 100
        self.button_minheight = 100
        for row in range(self.SIZE):
            self.grid_frame.rowconfigure(row, weight=1, minsize=self.button_minheight)
            button_row = []
            for column in range(self.SIZE):
                if row == 0:
                    self.grid_frame.columnconfigure(
                        column, weight=1, minsize=self.button_minwidth
                    )
                cell_pressed = partial(self.__cell_pressed, row=row, column=column)
                button = tk.Button(
                    self.grid_frame, font=self.__get_font(size=24), command=cell_pressed
                )
                button.grid(row=row, column=column, sticky=tk.NSEW)
                button_row.append(button)
            self.grid.append(button_row)

        self.winner_frame = tk.Frame(self)
        self.winner_frame_row = self.grid_frame_row + 1
        self.winner_frame.grid(row=self.winner_frame_row, column=0)
        self.winner_label = tk.Label(self.winner_frame)
        self.winner_label.grid(row=0, column=0)

    def __cell_pressed(self, row: int, column: int):
        self.grid[row][column]["text"] = self.controller.get_current_player()
        self.controller.update_grid(row, column)
        self.grid[row][column].config(state=tk.DISABLED)

    def __get_font(self, size: int):
        return f"{self.font} {size}"

    def get_current_player(self):
        return f"Current Player: {self.controller.get_current_player()}"

    def run(self):
        self.mainloop()

    def end_game(self):
        self.__is_game_over = True
    
    def new_game(self):
        #TODO
        pass
    
    def __disable_play(self):
        for row in self.grid:
            for cell in row:
                cell.config(state=tk.DISABLED)

    def render(self):
        if self.__is_game_over:
            self.winner_label["text"] = self.controller.get_winner()
            self.__disable_play()
        else:
            self.current_player_label["text"] = self.get_current_player()
