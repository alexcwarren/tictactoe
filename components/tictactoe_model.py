class TicTacToe_Model:
    __X: str = "X"
    __O: str = "O"
    __PLAYERS = [__O, __X]

    @property
    def X(self):
        return TicTacToe_Model.__X

    @property
    def O(self):
        return TicTacToe_Model.__O

    def __init__(self):
        self.__turn: int = 0
        self.__current_player: str = ""
        self.__grid: list[list[int]] = []
        self.__winner: str = ""
        self.reset()

    @property
    def current_player(self):
        return self.__current_player

    @property
    def grid(self):
        return self.__grid

    @property
    def winner(self):
        return self.__winner

    def update_grid(self, row: int, col: int):
        self.__grid[row][col] = self.__current_player
        self.__check_winner()
        self.__next_player()

    def reset(self):
        self.__turn = 0
        self.__next_player()
        self.__clear_grid()
        self.__winner = ""

    def __clear_grid(self):
        self.__grid = [["" for _ in range(3)] for _ in range(3)]
    
    def __check_winner(self):
        def check_winner_horizontally():
            for player in TicTacToe_Model.__PLAYERS:
                for row in self.__grid:
                    if all(cell == player for cell in row):
                        self.__winner = player
                        return True
            return False

        def check_winner_vertically():
            for player in TicTacToe_Model.__PLAYERS:
                for column in range(len(self.__grid)):
                    if all(row[column] == player for row in self.__grid):
                        self.__winner = player
                        return True
            return False

        def check_winner_diagonally():
            return False
        
        if check_winner_horizontally():
            return
        if check_winner_vertically():
            return
        if check_winner_diagonally():
            return

    def __next_player(self):
        self.__turn += 1
        self.__current_player = self.__PLAYERS[self.__turn % len(self.__PLAYERS)]
