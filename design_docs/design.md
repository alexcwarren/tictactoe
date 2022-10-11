# Tic-Tac-Toe Design {#title}

### Table of Contents

- [Model](#model)
- [View](#view)
- [Controller](#controller)
- [App Class](#app)
- [Testing](#testing)

### Description {#description}

- This will be an MVC application
- A 3-by-3 grid of cells
- Each cell starts empty
- Each cell, when pressed, changes (permanently) to the symbol of the current player

## Model {#model}

- Must track the following state
- current player: `X` or `O`
- value of each cell: ` `, `X`, or `O`
- winner (hidden until win condition triggered): ` `, `X`, or `O`

### Model Relationships

- None (**Model** knows nothing about **View** or **Controller**)

```python
class Model:
    def __init__(self):
        self.__data = None
    
    def get_state(self):
        return self.__data
    
    def update_state(self, input):
        self.__data = self.process_input(input)
    
    def __process_input(self, input):
        ...
        return data
```

## View {#view}

- Shall display current player and grid of cells (based on state in Model)
    - Update queries **Controller** for current state of **Model**
- Win condition changes the winning line of symbols to be *green* in color and displays `Player <X/O> Wins!`

```python
class View:
    def __init__(self):
        self.__controller = None
    
    @property
    def controller(self):
        return self.__controller
    
    @controller.setter
    def controller(self, controller):
        import ctrlr

        self.__controller: ctrlr.Controller = controller
    
    def run(self):
        self.display()  # mainloop
    
    def get_state(self):
        current_state = self.controller.get_state()
        ...
    
    def handle_input(self, input):
        self.__controller.update_state(input)
    
    def render(self):
        self.get_data()
        # Change view based on current data
        ...
```

### View Relationships

- Asks **Controller** for information (from **Model**)
- Tells **Controller** input received

## Controller {#controller}

- Initializes everything
- **Controller** is called by View when input is provided (i.e. a cell is pressed)
- **View** tells **Controller** which cell was pressed (via row and column)
- **Controller** passes this info to **Model** to update its state for that cell
    - **Model** changes the cell at the given position to the symbol of the current player and changes current player to the next player
- **View** (observing the Model) is then told to update what it displays

```python
import model
import view


class Controller:
    def __init__(self, model, view):
        self.__model: model.Model = model
        self.__view: view.View = view
        self.__view.controller = self
    
    def run(self):
        self.__view.render()
        self.__view.run()
    
    def get_state(self):
        return self.__model.get_state()
    
    def update_state(self, input):
        self.__model.update_state(input)
        self.__view.render()
```

### Controller Relationships

- **Controller** receives input from **View**
- **Controller** passes input to **Model**
- **Controller** tells **View** to update

## App Class {#app}

```python
import logging
import logging.config

import model
import view
import controller


class App:
    def __init__(self, model, view, debug=False):
        self.__setup_logger(debug)

        self.model: model.Model = model
        self.view: view.View = view
        self.controller: controller.Controller = controller.Controller(self.model, self.view)
    
    def __setup_logger(self, debug):
        logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
    
    def start(self):
        self.controller.run()


if __name__ == "__main__":
    App(model.Model(), view.View()).start()
```

## Testing MVC {#testing}

- Requires a different **View** class (since **View** is not tested, at least programatically)

### TestView Class

```python
class TestView(View):
    def __init__(self):
        super().__init__()
```

### Test

```python
import pytest

import model
import view
import controller


@pytest.fixture
def app():
    return App(model.Model(), view.TestView())

def test_model_process_input(app):
    assert app.model.__process_input(...) == ...

def test_model_state(app):
    app.model.update_state(...)
    assert app.model.get_state() == ...

def test_view_controller(app):
    assert isinstance(app.view.controller, controller.Controller)

def test_controller_state(app):
    app.controller.update_state(...)
    assert app.controller.get_state() == ...
```

[Back to top](#title)