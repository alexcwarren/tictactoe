import logging
import logging.config

import components.tictactoe_model as ttt_model
import components.tictactoe_view as ttt_view


class TicTacToe_Controller:
    def __init__(self, model, view):
        self.__setup_config()
        self.__model: ttt_model.TicTacToe_Model = model
        self.__view: ttt_view.TicTacToe_View = view
        self.__view.controller = self

    @property
    def model(self):
        return self.__model

    @property
    def view(self):
        return self.__view

    def __setup_config(self):
        logging.config.fileConfig(fname="log.conf", disable_existing_loggers=False)
        self.logger = logging.getLogger("Model")

    def get_current_player(self):
        return self.__model.current_player

    def get_grid(self):
        return self.__model.grid

    def update_grid(self, row: int, column: int):
        self.__model.update_grid(row, column)
        self.__view.render()

    def run(self):
        self.__view.render()
        self.__view.run()
