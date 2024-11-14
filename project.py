# подключение необходимых библиотек
import sqlite3 as sql
import sys
from random import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTableWidget, QInputDialog
from PyQt6.QtGui import QFont, QPixmap
from database import DataBase

# объявление констант
WIDTH, HEIGHT = 1000, 800

DB = DataBase()


# создание класса, представляющий меню игры
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rules = Rules()
        self.results = Results()
        self.initUi()

    def initUi(self):
        # настройка атрибутов для формы
        self.setGeometry(200, 200, WIDTH, HEIGHT)
        self.setWindowTitle('Главное меню')
        self.setFont(QFont('Candara', 12))

        # создание содержимого формы
        self.header = QLabel('Игра Memory', self)
        self.header.setFont(QFont('Candara', 45))
        self.header.resize(800, 90)
        self.header.move(320, 30)

        # создание содержимого формы
        self.results_btn = QPushButton('Топ лучших результатов', self)
        self.results_btn.resize(300, 50)
        self.results_btn.move(350, 200)
        self.results_btn.clicked.connect(lambda _: self.results.show())

        # создание содержимого формы
        self.rules_btn = QPushButton('Правила игры', self)
        self.rules_btn.resize(300, 50)
        self.rules_btn.move(350, 280)
        self.rules_btn.clicked.connect(lambda _: self.rules.show())

        # создание содержимого формы
        self.start_game_btn = QPushButton('Начать игру', self)
        self.start_game_btn.resize(300, 50)
        self.start_game_btn.move(350, 360)
        self.start_game_btn.clicked.connect(self.show_choice_lvl())

        # создание содержимого формы
        self.img_memory1 = QPixmap('img/memory1.jpg')
        self.img_memory2 = QPixmap('img/memory2.jpg')

        # создание содержимого формы
        self.label_memory1 = QLabel(self)
        self.label_memory1.resize(256, 256)
        self.label_memory1.move(194, 480)
        self.label_memory1.setPixmap(self.img_memory1)

        # создание содержимого формы
        self.label_memory2 = QLabel(self)
        self.label_memory2.resize(256, 256)
        self.label_memory2.move(550, 480)
        self.label_memory2.setPixmap(self.img_memory2)

    def show_choice_lvl(self):
        self.dialog = QInputDialog(self)
        


class Rules(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # настройка атрибутов для формы
        self.setGeometry(200, 200, WIDTH, HEIGHT)
        self.setWindowTitle('Правила')
        self.setFont(QFont('Candara', 12))

        # создание содержимого формы
        self.header = QLabel('Правила игры', self)
        self.header.setFont(QFont('Candara', 45))
        self.header.resize(800, 90)
        self.header.move(320, 30)

        # создание содержимого формы
        self.rules_text = QLabel(DB.get_rules(), self)
        self.rules_text.resize(WIDTH - 40, HEIGHT - 500)
        self.rules_text.move(20, 110)
        self.rules_text.setWordWrap(True)


class Results(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # настройка атрибутов для формы
        self.setGeometry(200, 200, WIDTH, HEIGHT)
        self.setWindowTitle('Топ лучших результатов')
        self.setFont(QFont('Candara', 12))

        # создание содержимого формы
        self.header = QLabel('Топ лучших результатов', self)
        self.header.setFont(QFont('Candara', 45))
        self.header.resize(800, 90)
        self.header.move(185, 30)

        if DB.get_data_results():
            # создание содержимого формы
            self.table_widget = QTableWidget(self)
            self.table_widget.resize(WIDTH, HEIGHT - 170)
            self.table_widget.move(0, 170)
            self.table_widget.setHorizontalHeaderLabels(('ID', 'Пользователь', 'Кол-во попыток'))
            self.table_widget.setColumnCount(3)

            # заполнить таблицу рез-татов данными из базы данных
            DB.write_data_results(self.table_widget)
        else:
            self.null_results_label = QLabel('На этот момент ни чей результат не был зафиксирован', self)
            self.null_results_label.setFont(QFont('Candara', 25))
            self.null_results_label.resize(WIDTH - 40, 50)
            self.null_results_label.move(100, 250)
            self.null_results_label.setWordWrap(True)


class Game(QWidget):
    def __init__(self, size_x, size_y):
        super().__init__()
        self.initUi()

    def initUi(self):
        # настройка атрибутов для формы
        self.setGeometry(200, 200, WIDTH, HEIGHT)
        self.setWindowTitle('Игра Memory')
        self.setFont(QFont('Candara', 12))




# вызов главного окна приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
