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
