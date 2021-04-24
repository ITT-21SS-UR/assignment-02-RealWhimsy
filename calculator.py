
import sys
from PyQt5 import uic, Qt
from enum import Enum

CLEAR = "Clear"
BACKSPACE = "Backspace"
EVALUATE = "Evaluate"

ALLOWED_KEYS = "0123456789+-*/,."
app = Qt.QApplication(sys.argv)
win = uic.loadUi("calculator.ui")


class InputType(Enum):
    """
    enum used to differentiate between the two input methods
    """
    BUTTON = 1
    KEYBOARD = 2


def logging_decorator(func):
    def wrapper(arg, input_type):
        func(arg, input_type)

        # check how the input was entered and print accordingly
        if input_type == InputType.KEYBOARD:
            print("Keyboard Input: " + str(arg))
        elif input_type == InputType.BUTTON:
            print("Button clicked: " + str(arg))
        else:
            print("Input Type did not match any valid value!")
    return wrapper


@logging_decorator
def evaluate(arg, input_type):
    # replace ',' with '.'
    expression = win.eval_text.toPlainText().replace(",", ".")

    try:
        win.eval_text.setText(str(eval(expression)))
    except (SyntaxError, NameError):
        print("No valid statement. Please check your input!")


@logging_decorator
def backspace(arg, input_type):
    win.eval_text.setText(win.eval_text.toPlainText()[:-1])


@logging_decorator
def clear(arg, input_type):
    win.eval_text.setText("")


@logging_decorator
def add_input_to_text(user_input, input_type):
    win.eval_text.setText(win.eval_text.toPlainText() + str(user_input))


def set_click_listeners():
    """
    sets the click listeners for all buttons
    """
    win.button_0.clicked.connect(lambda: add_input_to_text(0, InputType.BUTTON))
    win.button_1.clicked.connect(lambda: add_input_to_text(1, InputType.BUTTON))
    win.button_2.clicked.connect(lambda: add_input_to_text(2, InputType.BUTTON))
    win.button_3.clicked.connect(lambda: add_input_to_text(3, InputType.BUTTON))
    win.button_4.clicked.connect(lambda: add_input_to_text(4, InputType.BUTTON))
    win.button_5.clicked.connect(lambda: add_input_to_text(5, InputType.BUTTON))
    win.button_6.clicked.connect(lambda: add_input_to_text(6, InputType.BUTTON))
    win.button_7.clicked.connect(lambda: add_input_to_text(7, InputType.BUTTON))
    win.button_8.clicked.connect(lambda: add_input_to_text(8, InputType.BUTTON))
    win.button_9.clicked.connect(lambda: add_input_to_text(9, InputType.BUTTON))
    win.button_decimal.clicked.connect(lambda: add_input_to_text(".", InputType.BUTTON))

    win.button_multiply.clicked.connect(lambda: add_input_to_text('*', InputType.BUTTON))
    win.button_divide.clicked.connect(lambda: add_input_to_text('/', InputType.BUTTON))
    win.button_subtract.clicked.connect(lambda: add_input_to_text('-', InputType.BUTTON))
    win.button_add.clicked.connect(lambda: add_input_to_text('+', InputType.BUTTON))

    win.button_clear.clicked.connect(lambda: clear(CLEAR, InputType.BUTTON))
    win.button_backspace.clicked.connect(lambda: backspace(BACKSPACE, InputType.BUTTON))
    win.button_evaluate.clicked.connect(lambda: evaluate(EVALUATE, InputType.BUTTON))


def key_press_event(event):
    """
    checks for key presses and reacts accordingly
    """

    if Qt.QKeySequence(event.key()).toString() in ALLOWED_KEYS:
        add_input_to_text(Qt.QKeySequence(event.key()).toString(), InputType.KEYBOARD)

    # Key_Return = "Normal" Enter, Key_Enter = NumPad Enter
    elif event.key() == Qt.Qt.Key_Return or event.key() == Qt.Qt.Key_Enter:
        evaluate(EVALUATE, InputType.KEYBOARD)
    elif event.key() == Qt.Qt.Key_Backspace:
        backspace(BACKSPACE, InputType.KEYBOARD)


def override_key_press_event():
    win.keyPressEvent = key_press_event


def add_background_color():
    """
    Adds some background color to the buttons
    """
    win.button_0.setStyleSheet("background-color: lightblue")
    win.button_1.setStyleSheet("background-color: lightblue")
    win.button_2.setStyleSheet("background-color: lightblue")
    win.button_3.setStyleSheet("background-color: lightblue")
    win.button_4.setStyleSheet("background-color: lightblue")
    win.button_5.setStyleSheet("background-color: lightblue")
    win.button_6.setStyleSheet("background-color: lightblue")
    win.button_7.setStyleSheet("background-color: lightblue")
    win.button_8.setStyleSheet("background-color: lightblue")
    win.button_9.setStyleSheet("background-color: lightblue")
    win.button_decimal.setStyleSheet("background-color: lightblue")
    win.button_evaluate.setStyleSheet("background-color: orange")
    win.button_clear.setStyleSheet("background-color: red")


if __name__ == "__main__":
    set_click_listeners()
    add_background_color()
    override_key_press_event()
    win.show()
    app.exec()
