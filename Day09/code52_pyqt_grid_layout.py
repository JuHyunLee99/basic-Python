# 박스레이아웃
import sys
from PyQt5.QtWidgets import *

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0)  # row, col = 0, 0
        grid.addWidget(QLabel('Author'), 1, 0) 
        grid.addWidget(QLabel('Review'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)   # 0행 1열
        grid.addWidget(QLineEdit(), 1, 1)   # 0행 1열
        grid.addWidget(QTextEdit(), 2, 1)   # 0행 1열
        grid.addWidget(QPushButton('OK'), 3, 1) 
        grid.addWidget(QPushButton('Cancle'), 4, 1) 

        # 필수 설정
        self.setWindowTitle('박스레이아웃')
        self.setGeometry(300,300,300,300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())

