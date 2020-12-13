import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def style(self):
        self.setGeometry(300, 300, 300, 300)
        self.pushButton = QPushButton(self)
        self.pushButton.move(100, 100)
        self.pushButton.setFixedHeight(100)
        self.pushButton.setFixedWidth(100)
        self.pushButton.setText("Круг")
        self.setWindowTitle('Жёлтые круги')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Form.style(self)
        self.pushButton.clicked.connect(self.press)
        self.do_paint = False

    def press(self):
        name, ok_pressed = QInputDialog.getInt(self, "Введите количество",
                                               "Сколько кругов?")
        if ok_pressed:
            self.do_paint = True
            self.name = name

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        for i in range(self.name):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = randint(0, 400), randint(0, 300)
            d = randint(1, 50)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())