import sys
import sqlite3
from PyQt5.QtGui import QFont
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QProgressBar
global correct_answers, points
correct_answers = 0
points = 0

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

        self.about_program_button = QPushButton(self)
        self.about_program_button.setGeometry(670, 555, 121, 31)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_program_button.setFont(font)
        self.about_program_button.setText("О программе")
        self.about_program_button.clicked.connect(self.about_program)

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

    def about_program(self):
        self.second_form = SecondForm(self)
        self.second_form.show()

    def register_user(self):
        username = self.username_input.text()
        if username:
            with open("players.txt", "a", encoding="utf-8") as file:
                file.write(username + "\n")
                QtWidgets.QMessageBox.information(self, "Success", "User registered successfully!")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a username!")
        mainwindow = MainWidget()
        mainwindow.show()
        self.close()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 700, 400)
        self.setWindowTitle('about program')
        self.lbl = QLabel(self)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl.setFont(font)
        self.lbl.setGeometry(20, 20, 20, 30)
        self.lbl.setText("""1. Регистрация и начало игры
Чтобы начать играть, зарегистрируйтесь
После регистрации, откроется окно самой игры, в котором:
    ♦ В верхней части экрана, вам будет задан вопрос в формате "Напишите..."
    ♦ В середине экрана перед вами будет поле ввода ответа
    ♦ Также, в середине экрана будут находиться кнопки с буквами, нажав на которые
    их значение добавится в поле ввода ответа
    ♦ Рядом с ними будут находиться кнопки backspace("⌫") и "Enter", выполняющие
    соответственные функции
    ♦ У вас будет всего 3 попытки ответа на вопрос
3. Подсказка
При ответе, вы можете использовать подсказку, которая будет показывать количество
букв в ответе, но использовав подсказку, количесто баллов, которые вы получите после
ответа на вопрос - уменишится на 1 
4. Система оценивания
При правильном ответе на вопрос, без использования подсказки, вы получаете 2 балла
Использовав подсказку, вы получаете 1 балл
Потратив 3 попытки ответа, вы получаете - 0 баллов""")
        self.lbl.adjustSize()


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(801, 599)
        self.initUI()
        self.setWindowTitle("Ossetian Language Quiz")
        self.id_of_dataBase = 0
        self.number_of_question = 1
        self.correct_answers = correct_answers
        self.points = 0
        self.attemps = 3
        self.usehint = True
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

        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.number_of_qwestion_label.setFont(font)
        self.number_of_qwestion_label.setText(f"Вопрос {self.number_of_question} из 10")

        self.points_label.setText(f"Очки: {self.points}")

        self.enter_button.clicked.connect(self.do_is)
        self.backspace_button.clicked.connect(self.backspase)
        self.hint_button.clicked.connect(self.hint)

    def initUI(self):

        self.user_answer = QLineEdit(self)
        self.user_answer.setReadOnly(True)
        self.user_answer.setGeometry(220, 160, 381, 41)


        self.points_label = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_label.setFont(font)
        self.points_label.setGeometry(650, 0, 81, 41)


        self.enter_button = QPushButton(self)
        self.enter_button.setText('Enter')
        self.enter_button.setGeometry(360, 290, 81, 31)

        self.backspace_button = QPushButton(self)
        self.backspace_button.setText('⌫')
        self.backspace_button.setGeometry(370, 330, 59, 31)

        self.hint_button = QPushButton(self)
        self.hint_button.setText('Подсказка')
        self.hint_button.setGeometry(650, 50, 75, 23)

        self.question_label = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.question_label.setFont(font)
        self.question_label.setGeometry(70, 30, 580, 91)

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
        self.number_of_qwestion_label.setGeometry(340, 430, 151, 31)


    def backspase(self):
        t = self.user_answer.text()
        if t:
            self.user_answer.setText(t[:-1])

    def do_is(self):
        if self.user_answer.text().lower() == self.ans:
            if self.usehint == True:
                self.points += 2
            else:
                self.points += 1
            QtWidgets.QMessageBox.information(self, "Success", "Поздравляю! Вы ответили правильно!")
            self.correct_answers += 1
            self.roundclose = True
        else:
            self.attemps -= 1
            if self.attemps:
                QtWidgets.QMessageBox.warning(self, "Not success",
                                              f"""К сожалению вы ответили неправильно.
                                              У вас осталось: {self.attemps} попыток!""")
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
            self.usehint = True
            self.points_label.setText(f"Очки: {self.points}")
            points = self.points

    def hint(self):
        QtWidgets.QMessageBox.information(self, f"hint for {self.number_of_question} question",
                                          f"Подсказка: слово состоит из {len(self.ans)} букв")
        self.usehint = False

    def on_button_click(self, letter):
        self.user_answer.setText(self.user_answer.text() + letter)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    registration_window = RegistrationWindow()
    registration_window.show()
    sys.exit(app.exec_())
