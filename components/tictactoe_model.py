import logging
import logging.config
import logging.handlers


class TicTacToe_Model:
    __SIZE: int = 3
    __PLAYER_X: str = "X"
    __PLAYER_O: str = "O"
    __PLAYERS: list[str] = [__PLAYER_O, __PLAYER_X]
    __TIE: str = "TIE"

    @property
    def playerX(self):
        return TicTacToe_Model.__PLAYER_X

    @property
    def playerO(self):
        return TicTacToe_Model.__PLAYER_O

    def __init__(self):
        self.__setup_config()
        self.logger.debug("Creating model")
        self.__turn: int = 0
        self.__current_player: str = ""
        self.__grid: list[list[int]] = []
        self.__num_empty_cells: int = 0
        self.__winner: str = ""
        self.__is_game_over: bool = False
        self.reset()

    @property
    def current_player(self):
        return self.__current_player

    @property
    def grid(self):
        return self.__grid

    @property
    def winner(self):
        if self.__winner == TicTacToe_Model.__TIE:
            return self.__winner
        return f"Player {self.__winner} wins!"

    @property
    def is_game_over(self):
        return self.__is_game_over

    def __setup_config(self):
        logging.config.fileConfig(fname="log.conf", disable_existing_loggers=False)
        self.logger = logging.getLogger("Model")

    def update_grid(self, row: int, column: int):
        if self.__grid[row][column] != "":
            raise Exception(
                f'Cell [{row}][{column}] already populated with "{self.__grid[row][column]}"'
            )
        if self.__is_game_over:
            return
        self.__grid[row][column] = self.__current_player
        self.__num_empty_cells -= 1
        if self.__num_empty_cells <= 0:
            self.__tie_game()
            return
        self.__check_winner()
        self.__next_player()

    def reset(self):
        self.__turn = 0
        self.__next_player()
        self.__clear_grid()
        self.__num_empty_cells = TicTacToe_Model.__SIZE**2
        self.__winner = ""
        self.__is_game_over = False

    def __clear_grid(self):
        self.__grid = [
            ["" for _ in range(TicTacToe_Model.__SIZE)]
            for _ in range(TicTacToe_Model.__SIZE)
        ]

    def __check_winner(self):
        if self.__check_winner_horizontally():
            self.__is_game_over = True
            return
        if self.__check_winner_vertically():
            self.__is_game_over = True
            return
        if self.__check_winner_diagonally():
            self.__is_game_over = True
            return

    def __tie_game(self):
        self.__winner = TicTacToe_Model.__TIE
        self.__is_game_over = True

    def __check_winner_horizontally(self):
        for player in TicTacToe_Model.__PLAYERS:
            for row in self.__grid:
                if all(cell == player for cell in row):
                    self.__winner = player
                    return True
        return False

    def __check_winner_vertically(self):
        for player in TicTacToe_Model.__PLAYERS:
            for column in range(len(self.__grid)):
                if all(row[column] == player for row in self.__grid):
                    self.__winner = player
                    return True
        return False

    def __check_winner_diagonally(self):
        for player in TicTacToe_Model.__PLAYERS:
            indices_range = [i for i in range(len(self.__grid))]
            if all(self.__grid[n][n] == player for n in indices_range) or all(
                self.__grid[n][m] == player
                for n, m in zip(indices_range, reversed(indices_range))
            ):
                self.__winner = player
                return True
        return False

    def __next_player(self):
        self.__turn += 1
        self.__current_player = self.__PLAYERS[self.__turn % len(self.__PLAYERS)]
