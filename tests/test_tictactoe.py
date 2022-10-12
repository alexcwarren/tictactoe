import pytest

import components.tictactoe_controller as controller
import components.tictactoe_model as model
import components.tictactoe_view as view
import tictactoe

PLAYER_X: str = "X"
PLAYER_O: str = "O"
TIE: str = "TIE"


@pytest.fixture
def app():
    return tictactoe.App(view=view.TicTacToe_TestView())


# App


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


# Model


def test_model_players(app):
    assert app.model.playerX == PLAYER_X
    assert app.model.playerO == PLAYER_O


def test_model_starting_player(app):
    assert app.model.current_player == PLAYER_X


def test_model_3x3_grid(app):
    assert len(app.model.grid) == 3
    assert all(len(row) == 3 for row in app.model.grid)


def test_model_start_empty_grid(app):
    assert all(all(cell == "" for cell in row) for row in app.model.grid)


def test_model_first_turn(app):
    app.model.update_grid(0, 1)
    assert app.model.grid[0][1] == PLAYER_X
    assert app.model.current_player == PLAYER_O


@pytest.mark.parametrize(
    "row, column, result",
    [(1, 1, PLAYER_O), (2, 2, PLAYER_X), (0, 0, PLAYER_O), (1, 0, PLAYER_X)],
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
    assert app.model.current_player == PLAYER_X


def play_to_end(app, plays, winner):
    app.model.reset()
    for row, column in plays:
        app.model.update_grid(row, column)
    assert app.model.winner == winner


def test_model_X_wins_horizontally_first_row(app):
    plays = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    play_to_end(app, plays, PLAYER_X)


def test_model_O_wins_horizontally_second_row(app):
    plays = [(0, 0), (1, 1), (2, 0), (1, 0), (0, 1), (1, 2)]
    play_to_end(app, plays, PLAYER_O)


def test_model_X_wins_horizontally_third_row(app):
    plays = [(2, 0), (1, 1), (2, 2), (0, 1), (2, 1)]
    play_to_end(app, plays, PLAYER_X)


def test_model_X_wins_vertically_first_column(app):
    plays = [(2, 0), (2, 1), (0, 0), (1, 1), (1, 0)]
    play_to_end(app, plays, PLAYER_X)


def test_model_O_wins_vertically_second_column(app):
    plays = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 2), (2, 1)]
    play_to_end(app, plays, PLAYER_O)


def test_model_X_wins_vertically_third_column(app):
    plays = [(0, 2), (0, 0), (2, 2), (1, 1), (1, 2)]
    play_to_end(app, plays, PLAYER_X)


def test_model_X_wins_diagonally_topleft_bottomright(app):
    plays = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    play_to_end(app, plays, PLAYER_X)


def test_model_O_wins_diagonally_bottomleft_topright(app):
    plays = [(0, 0), (2, 0), (2, 2), (1, 1), (0, 1), (0, 2)]
    play_to_end(app, plays, PLAYER_O)


def test_model_tie(app):
    plays = [(0, 0)]
    play_to_end(app, plays, TIE)


# Controller


def test_controller_get_grid(app):
    assert app.controller.get_grid() == app.model.grid
    app.model.reset()


def test_controller_get_current_player(app):
    assert app.controller.get_current_player() == PLAYER_X


@pytest.mark.parametrize(
    "row, column, player",
    [(0, 0, PLAYER_X), (1, 1, PLAYER_O), (2, 2, PLAYER_X), (1, 0, PLAYER_O)],
)
def test_controller_update_grid(row: int, column: int, player: str, app):
    app.controller.update_grid(row, column)
    assert app.controller.get_grid()[row][column] == player
