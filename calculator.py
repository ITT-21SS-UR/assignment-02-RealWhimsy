
import sys
from PyQt5 import uic, Qt


app = Qt.QApplication(sys.argv)
win = uic.loadUi("calculator.ui")


def backspace():
    win.eval_text.setText(win.eval_text.toPlainText()[:-1])


def clear():
    win.eval_text.setText("")


def evaluate():
    win.eval_text.setText(str(eval(win.eval_text.toPlainText())))


def logging_decorator(func):
    def wrapper(arg):
        func(arg)
        print("Input: " + str(arg))
    return wrapper


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

    win.button_clear.clicked.connect(lambda: clear())
    win.button_backspace.clicked.connect(lambda: backspace())
    win.button_evaluate.clicked.connect(lambda: evaluate())


if __name__ == "__main__":
    set_click_listeners()
    win.show()
    app.exec()



