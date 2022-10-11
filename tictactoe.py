import logging
import logging.config

import components.tictactoe_controller as ttt_controller
import components.tictactoe_model as ttt_model
import components.tictactoe_view as ttt_view


class App:
    def __init__(
        self, model=ttt_model.TicTacToe_Model(), view=ttt_view.TicTacToe_GUIView()
    ):
        self.__setup_logger()
        self.logger.debug("Creating app")
        self.model: ttt_model.TicTacToe_Model = model
        self.view: ttt_view.TicTacToe_View = view
        self.controller = ttt_controller.TicTacToe_Controller(self.model, self.view)

    def __setup_logger(self):
        logging.config.fileConfig(fname="log.conf", disable_existing_loggers=False)
        self.logger = logging.getLogger("App")

    def start(self):
        self.logger.debug("Starting app")
        self.controller.run()


if __name__ == "__main__":
    App().start()
