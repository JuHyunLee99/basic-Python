# 이미지 처리
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/cat.png')

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))  # 이미지 크기 정보 반환
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter)  # (Qt.AlignCenter)도 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300,300,300,300)
        
        self.showFullScreen()
        # self.setCenter()   


    def setCenter(self):
        qr = self.frameGeometry()   # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터 화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





