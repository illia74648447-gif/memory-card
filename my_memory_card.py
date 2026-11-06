from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import shuffle
from time import sleep


app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question("Яка столиця Франції?", "Париж", "Київ", "Мадрид", "Берлін")
]


current_question = -1

window = QWidget()
window.show()
window.resize(800, 600)
window.setWindowTitle("Memory Card")

title = QLabel("Переклади англіською слово автомобіль")
ans_btn1 = QRadioButton("Bus")
ans_btn2 = QRadioButton("Car")
ans_btn3 = QRadioButton("Taxi")
ans_btn4 = QRadioButton("Ship")
answer_button = QPushButton("Відповідь")

radio_group = QButtonGroup()
radio_group.addButton(ans_btn1)
radio_group.addButton(ans_btn2)
radio_group.addButton(ans_btn3)
radio_group.addButton(ans_btn4)

answers = [ans_btn1, ans_btn2, ans_btn3, ans_btn4]

t_line = QVBoxLayout()
l_1 = QHBoxLayout()
l_2 = QHBoxLayout()
l_3 = QHBoxLayout()
l_4 = QHBoxLayout()

l_1.addWidget(title, alignment=Qt.AlignCenter)

l_2.addWidget(ans_btn1, alignment=Qt.AlignCenter)
l_2.addWidget(ans_btn2, alignment=Qt.AlignCenter)

l_3.addWidget(ans_btn3, alignment=Qt.AlignCenter)
l_3.addWidget(ans_btn4, alignment=Qt.AlignCenter)

l_4.addWidget(answer_button, alignment=Qt.AlignCenter)

t_line.addLayout(l_1)
t_line.addLayout(l_2)
t_line.addLayout(l_3)
t_line.addLayout(l_4)

window.setLayout(t_line)
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    title.setText(q.question)
    answer_button.setText("Відповідь")

def show_correct(res):
    title.setText(res)
    answer_button.setText("Наступне запитання")

def next_question():
    global current_question
    current_question += 1
    if current_question >= len(questions_list):
        current_question = 0

    q = questions_list[current_question]
    ask(q)

def click_OK():
    if answer_button.text() == "Відповідь":
        if answers[0].isChecked():
            show_correct("Правильно!")
        else:
            if ans_btn1.isChecked() or ans_btn2.isChecked() or ans_btn3.isChecked() or ans_btn4.isChecked():
                show_correct("Неправильно!")
            else:
                title.setText("Обери варіант відповіді!")
                QTimer.singleShot(1000, lambda: title.setText(questions_list[current_question].question))
                return
    else:
        radio_group.setExclusive(False)
        ans_btn1.setChecked(False)
        ans_btn2.setChecked(False)
        ans_btn3.setChecked(False)
        ans_btn4.setChecked(False)
        radio_group.setExclusive(True)
        next_question()


answer_button.clicked.connect(click_OK)
next_question()

app.exec_()
