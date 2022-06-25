import sys
from PyQt5.QtWidgets import QApplication
from notepad import MainWindow
from login import LoginForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Login")
    form = LoginForm()
    form.show()
    window = MainWindow()

    app.exec_()
