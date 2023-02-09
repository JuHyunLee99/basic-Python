# 윈도우 창 닫기 앱
# 2023.02.09
# JHL

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼
        # QPushButton(버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯): 푸시버튼 만듬
        btn = QPushButton('Quit', self) # btn : QPushButton 클래스의 instance
        btn.move(320, 170)
        btn.resize(btn.sizeHint())  # sizeHint() : 버튼을 적절한 크기로 설정하도록 도와줌.
        # 버튼 (btn)을 클릭하면 'clicked' 시그널이 만들짐
        # instance() 메서드는 현재 인스턴스를 반환
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결
        btn.clicked.connect(QCoreApplication.instance().quit)

        
        # 버튼 툴팁
        btn.setToolTip('이거 누르면 그냥 꺼져요. <b>조심</b>하세요!!!')


        # GUI 화면 설정
        self.setWindowTitle('Quit Button')
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # setGeometry() : 창의 위치와 크기 설정, (x, y, w, h)
        self.setGeometry(900, 200, 400, 200)    # move(),resize()를 하나로 합쳐놓은 것
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
