import sys
import random
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
        painter.setRenderHint(QPainter.Antialiasing)
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        painter.setPen(QColor(255, 255, 0))
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(x, y, diameter, diameter)
    
    def draw_circle(self):
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
  