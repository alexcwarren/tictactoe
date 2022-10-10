import pytest

import components.tictactoe_controller as controller
import components.tictactoe_model as model
import components.tictactoe_view as view
import tictactoe


@pytest.fixture
def app():
    return tictactoe.App(view=view.TicTacToe_TestView())


def test_app_model(app):
    assert isinstance(app.model, model.TicTacToe_Model)


def test_app_view(app):
    assert isinstance(app.view, view.TicTacToe_View)


def test_app_controller(app):
    assert isinstance(app.controller, controller.TicTacToe_Controller)


def test_app_controller_model(app):
    assert isinstance(app.controller.model, model.TicTacToe_Model)
    assert app.controller.model is app.model


def test_app_controller_view(app):
    assert isinstance(app.controller.view, view.TicTacToe_View)
    assert app.controller.view is app.view


def test_app_view_controller(app):
    assert isinstance(app.view.controller, controller.TicTacToe_Controller)
    assert app.view.controller is app.controller


def test_model_players(app):
    assert app.model.X == "X"
    assert app.model.O == "O"


def test_model_starting_player(app):
    assert app.model.current_player == "X"


def test_model_3x3_grid(app):
    assert len(app.model.grid) == 3
    assert all(len(row) == 3 for row in app.model.grid)


def test_model_start_empty_grid(app):
    assert all(all(cell == "" for cell in row) for row in app.model.grid)


def test_model_first_turn(app):
    app.model.update_grid(0, 1)
    assert app.model.grid[0][1] == "X"
    assert app.model.current_player == "O"


@pytest.mark.parametrize(
    "row, column, result",
    [(1, 1, "O"), (2, 2, "X"), (0, 0, "O"), (1, 0, "X")],
)
def test_model_more_turns(row: int, column: int, result: str, app):
    app.model.update_grid(row, column)
    assert app.model.grid[row][column] == result


def test_model_no_winner(app):
    assert app.model.winner == ""


def test_model_reset(app):
    assert any(any(cell != "" for cell in row) for row in app.model.grid)
    app.model.reset()
    assert all(all(cell == "" for cell in row) for row in app.model.grid)
    assert app.model.current_player == 'X'

def play_to_win(app, plays, winner):
    app.model.reset()
    for row,column in plays:
        app.model.update_grid(row, column)
    assert app.model.winner == winner

def test_model_X_wins_horizontally_first_row(app):
    plays = [(0,0), (1,0), (0,1), (1,1), (0,2)]
    play_to_win(app, plays, 'X')

def test_model_O_wins_vertically_second_column(app):
    plays = [(0,0), (0,1), (1,0), (1,1), (0,2), (2,1)]
    play_to_win(app, plays, 'O')

def test_model_X_wins_diagonally_topleft_bottomright(app):
    plays = [(0,0), (0,1), (1,1), (2,1), (2,2)]
    play_to_win(app, plays, 'X')