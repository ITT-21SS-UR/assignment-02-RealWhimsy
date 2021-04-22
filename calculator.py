
import sys
from PyQt5 import uic, Qt

CLEAR = "Clear"
BACKSPACE = "Backspace"
EVALUATE = "Evaluate"

allowed_keys = "0123456789+-*/,."
app = Qt.QApplication(sys.argv)
win = uic.loadUi("calculator.ui")


def logging_decorator(func):
    def wrapper(arg):
        func(arg)
        print("Input: " + str(arg))
    return wrapper


@logging_decorator
def evaluate(arg=EVALUATE):
    expression = win.eval_text.toPlainText().replace(",", ".")  # replace ',' with '.'
    win.eval_text.setText(str(eval(expression)))


@logging_decorator
def backspace(arg=BACKSPACE):
    win.eval_text.setText(win.eval_text.toPlainText()[:-1])


@logging_decorator
def clear(arg=CLEAR):
    win.eval_text.setText("")


@logging_decorator
def add_input_to_text(user_input):
    win.eval_text.setText(win.eval_text.toPlainText() + str(user_input))


def set_click_listeners():
    win.button_0.clicked.connect(lambda: add_input_to_text(0))
    win.button_1.clicked.connect(lambda: add_input_to_text(1))
    win.button_2.clicked.connect(lambda: add_input_to_text(2))
    win.button_3.clicked.connect(lambda: add_input_to_text(3))
    win.button_4.clicked.connect(lambda: add_input_to_text(4))
    win.button_5.clicked.connect(lambda: add_input_to_text(5))
    win.button_6.clicked.connect(lambda: add_input_to_text(6))
    win.button_7.clicked.connect(lambda: add_input_to_text(7))
    win.button_8.clicked.connect(lambda: add_input_to_text(8))
    win.button_9.clicked.connect(lambda: add_input_to_text(9))

    win.button_multiply.clicked.connect(lambda: add_input_to_text('*'))
    win.button_divide.clicked.connect(lambda: add_input_to_text('/'))
    win.button_subtract.clicked.connect(lambda: add_input_to_text('-'))
    win.button_add.clicked.connect(lambda: add_input_to_text('+'))

    win.button_clear.clicked.connect(lambda: clear(CLEAR))
    win.button_backspace.clicked.connect(lambda: backspace(BACKSPACE))
    win.button_evaluate.clicked.connect(lambda: evaluate(EVALUATE))


def key_press_event(event):
    if Qt.QKeySequence(event.key()).toString() in allowed_keys:
        add_input_to_text(Qt.QKeySequence(event.key()).toString())

    # Key_Return = "Normal" Enter, Key_Enter = NumPad Enter
    elif event.key() == Qt.Qt.Key_Return or event.key() == Qt.Qt.Key_Enter:
        evaluate(EVALUATE)
    elif event.key() == Qt.Qt.Key_Backspace:
        backspace(BACKSPACE)


def override_key_press_event():
    win.keyPressEvent = key_press_event


if __name__ == "__main__":
    set_click_listeners()
    override_key_press_event()
    win.show()
    app.exec()



