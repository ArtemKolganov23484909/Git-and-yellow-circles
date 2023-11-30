import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button = self.findChild(QPushButton, 'button')
        self.button.clicked.connect(self.draw_circle)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 0))
        diameter = 50  # Задайте случайный диаметр здесь
        x = (self.width() - diameter) / 2
        y = (self.height() - diameter) / 2
        painter.drawEllipse(x, y, diameter, diameter)

    def draw_circle(self):
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
