# 스타일
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        # 라벨 위젯 만들기
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet('color: red;'             # 글자색
                              'border-style: solid;'    # 경계선
                              'border-width: 5px;'      # 경계선 두께
                              'border-color: #FA8072;'  # 경계선 색
                              "border-radius: 10px")     # 모서리 필렛

        lbl_green = QLabel('green')
        lbl_green.setStyleSheet('color: green;'            
                              'border-style: dashed;'    
                              'border-width: 5px;'      
                              'border-color: #7FFFD4' )

        # QVBoxLayout(): 세로로 / QHBoxLayout() 가로로 위치
        vbox = QVBoxLayout()    # 세로 구분짓는 수직 박스 레이아웃
        vbox.addWidget(lbl_red) # 위젯 추가
        vbox.addWidget(lbl_green) # 위젯 추가

        self.setLayout(vbox)  # 전체 레이아웃에 vbox를 추가

        # 기본설정 - 사이즈, show() 필수!!
        self.setWindowTitle('스타일 꾸미기')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())