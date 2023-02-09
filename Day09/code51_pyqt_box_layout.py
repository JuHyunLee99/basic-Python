# 박스레이아웃 레이아웃
import sys
from PyQt5.QtWidgets import *

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('OK')
        btnCancle = QPushButton('Cancle')

        hbox = QHBoxLayout()    # 수평박스
        hbox.addStretch(1)      # 양 쪽 빈 공간
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancle)
        hbox.addStretch(1)
        # stretch factor가 1로 같기 때문에 
        # 이 두 빈 공간의 크기는 창의 크기가 변화해도 항상 같다

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        # 위와 아래의 빈 공간의 크기는 항상 3:1을 유지

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('박스레이아웃')
        self.setGeometry(300,300,300,300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())

