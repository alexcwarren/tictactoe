import components.tictactoe_model as ttt_model
import components.tictactoe_view as ttt_view


class TicTacToe_Controller:
    def __init__(self, model, view):
        self.__model: ttt_model.TicTacToe_Model = model
        self.__view: ttt_view.TicTacToe_View = view
        self.__view.controller = self

    @property
    def model(self):
        return self.__model

    @property
    def view(self):
        return self.__view

    def run(self):
        self.__view.run()
