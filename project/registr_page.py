from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(801, 599)
        self.initUI()
        self.setWindowTitle("Registration Window")
        self.enter_name_button.clicked.connect(self.register_user)

    def initUI(self):
        self.enter_name_button = QPushButton(self)
        self.enter_name_button.setGeometry(250, 360, 291, 111)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.enter_name_button.setFont(font)
        self.enter_name_button.setText("Играть")

        self.enter_name_label = QLabel(self)
        self.enter_name_label.setGeometry(330, 220, 131, 41)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.enter_name_label.setFont(font)
        self.enter_name_label.setText("Введите имя пользователя")

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(230, 280, 331, 51)
        self.username_input.setText("")
        self.username_input.setObjectName("lineEdit")

        self.leader_board_label = QLabel(self)
        self.leader_board_label.setGeometry(270, 30, 251, 81)

        font = QFont()
        font.setPointSize(16)

        self.username_input.setFont(font)

        font = QFont()
        font.setPointSize(11)

        self.leader_board_label.setFont(font)
        self.leader_board_label.setText("Leader:")

    def register_user(self):
        username = self.username_input.text()
        if username:
            with open("players.txt", "a", encoding="utf-8") as file:
                file.write(username + "\n")
                QtWidgets.QMessageBox.information(self, "Success", "User registered successfully!")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a username!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    registration_window = RegistrationWindow()
    registration_window.show()
    sys.exit(app.exec_())

