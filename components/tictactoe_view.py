import abc


class TicTacToe_View(abc.ABC):
    def __init__(self):
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        import components.tictactoe_controller as ttt_controller

        self.__controller: ttt_controller = controller


class TicTacToe_TestView(TicTacToe_View):
    def __init__(self):
        super().__init__()


class TicTacToe_GUIView(TicTacToe_View):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Running...")
