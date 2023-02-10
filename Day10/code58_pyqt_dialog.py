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
        # 버튼
        self.btnDlg = QPushButton('Dialog', self)
        self.btnDlg.move(20, 20)
        self.btnDlg.clicked.connect(self.onClicked)

        # 라인에디트
        self.txtInput = QLineEdit(self)
        self.txtInput.move(20, 50)
        

        # 필수설정
        self.setWindowTitle('다이얼로그')
        self.setGeometry(300,300,300,300)       
        self.show()
 
    def onClicked(self):
        # 다이얼로그
        text, ok = QInputDialog.getText(self, '인풋다이얼로그', '이름을 적으세요') # 튜블 형태로 반환

        if ok:  # ok클릭하면 라인에티트에 text 삽입
            self.txtInput.setText(text)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





