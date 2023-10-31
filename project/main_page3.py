import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QProgressBar


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(801, 599)
        self.initUI()
        self.setWindowTitle("Ossetian Language Quiz")
        self.points = 0
        self.id_of_dataBase = 0
        self.number_of_question = 1
        self.attemps = 3
        self.roundclose = False
        self.con = sqlite3.connect("DataBaseForMainWindow.sqlite")
        self.cur = self.con.cursor()
        self.Data = self.cur.execute("""SELECT * FROM BaseAlData""").fetchall()
        self.con.close()
        self.letters = self.Data[0 + self.id_of_dataBase][2]
        self.ans = self.Data[0 + self.id_of_dataBase][1]
        self.question = self.Data[0 + self.id_of_dataBase][0]
        self.question_label.setText(self.question)
        self.letter1.setText(self.letters[0])
        self.letter1.clicked.connect(lambda: self.on_button_click(self.letters[0]))

        self.letter2.setText(self.letters[1])
        self.letter2.clicked.connect(lambda: self.on_button_click(self.letters[1]))

        self.letter3.setText(self.letters[2])
        self.letter3.clicked.connect(lambda: self.on_button_click(self.letters[2]))

        self.letter4.setText(self.letters[3])
        self.letter4.clicked.connect(lambda: self.on_button_click(self.letters[3]))

        self.letter5.setText(self.letters[4])
        self.letter5.clicked.connect(lambda: self.on_button_click(self.letters[4]))

        self.letter_six.setText(self.letters[5])
        self.letter_six.clicked.connect(lambda: self.on_button_click(self.letters[5]))

        self.letter7.setText(self.letters[6])
        self.letter7.clicked.connect(lambda: self.on_button_click(self.letters[6]))

        self.letter8.setText(self.letters[7])
        self.letter8.clicked.connect(lambda: self.on_button_click(self.letters[7]))

        self.number_of_qwestion_label.setText(f"Вопрос {self.number_of_question} из 10")

        self.enter_button.clicked.connect(self.do_is)
        self.backspace_button.clicked.connect(self.backspase)

    def initUI(self):

        self.user_answer = QLineEdit(self)
        self.user_answer.setGeometry(220, 160, 381, 41)

        self.enter_button = QPushButton(self)
        self.enter_button.setText('Enter')
        self.enter_button.setGeometry(360, 290, 81, 31)

        self.backspace_button = QPushButton(self)
        self.backspace_button.setText('⌫')
        self.backspace_button.setGeometry(370, 330, 59, 31)

        self.question_label = QLabel(self)
        self.question_label.setGeometry(70, 30, 671, 91)

        self.letter1 = QPushButton(self)
        self.letter1.setGeometry(360, 250, 31, 31)

        self.letter2 = QPushButton(self)
        self.letter2.setGeometry(410, 250, 31, 31)

        self.letter3 = QPushButton(self)
        self.letter3.setGeometry(450, 290, 31, 31)

        self.letter4 = QPushButton(self)
        self.letter4.setGeometry(450, 330, 31, 31)

        self.letter5 = QPushButton(self)
        self.letter5.setGeometry(410, 370, 31, 31)

        self.letter_six = QPushButton(self)
        self.letter_six.setGeometry(360, 370, 31, 31)

        self.letter7 = QPushButton(self)
        self.letter7.setGeometry(320, 330, 31, 31)

        self.letter8 = QPushButton(self)
        self.letter8.setGeometry(320, 290, 31, 31)

        self.progress_of_dialog = QProgressBar(self)
        self.progress_of_dialog.setGeometry(270, 470, 271, 31)
        self.progress_of_dialog.setValue(0)

        self.number_of_qwestion_label = QLabel(self)
        self.number_of_qwestion_label.setGeometry(340, 430, 121, 31)
        self.number_of_qwestion_label.setObjectName("number_of_qwestion_label")

    def backspase(self):
        t = self.user_answer.text()
        if t:
            self.user_answer.setText(t[:-1])

    def do_is(self):
        if self.user_answer.text() == self.ans:
            QtWidgets.QMessageBox.information(self, "Success", "Поздравляю! Вы ответили правильно!")
            self.roundclose = True
        else:
            if self.attemps:
                QtWidgets.QMessageBox.warning(self, "Not success",
                                              f"""К сожалению вы ответили неправильно.
                                              У вас осталось: {self.attemps} попыток!""")
                self.attemps -= 1
                self.user_answer.setText("")
            else:
                QtWidgets.QMessageBox.warning(self, "Not success",
                                              """К сожалению вы потратили все попытки ответа на этот вопрос,
                                              но не стоит расстраиватся, постарайтесь ответить правильно на следующий)""")
                self.roundclose = True
        if self.roundclose:
            self.id_of_dataBase += 1
            self.letters = self.Data[0 + self.id_of_dataBase][2]
            self.ans = self.Data[0 + self.id_of_dataBase][1]
            self.question = self.Data[0 + self.id_of_dataBase][0]
            self.user_answer.setText("")
            self.question_label.setText(self.question)
            self.letter1.setText(self.letters[0])
            self.letter2.setText(self.letters[1])
            self.letter3.setText(self.letters[2])
            self.letter4.setText(self.letters[3])
            self.letter5.setText(self.letters[4])
            self.letter_six.setText(self.letters[5])
            self.letter7.setText(self.letters[6])
            self.letter8.setText(self.letters[7])
            self.progress_of_dialog.setValue(self.number_of_question * 10)
            self.number_of_question += 1
            self.attemps = 3
            self.number_of_qwestion_label.setText(f"Вопрос {self.number_of_question} из 10")
            self.roundclose = False

    def on_button_click(self, letter):
        self.user_answer.setText(self.user_answer.text() + letter)


if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    widget = MainWidget()
    window.setCentralWidget(widget)
    window.show()
    app.exec_()
