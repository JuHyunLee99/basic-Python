# 체크박스, 라디오버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cbShowTitle = QCheckBox('Show Title', self)
        cbShowTitle.move(20,20)
        cbShowTitle.toggle()    # 체크 박스의 상태를 변경/ 실행 결과 체크박스 체크되있음
        # signal 종류 stateChanged: 체크박스의 상태가 바뀔 때 신호 발생
        # connect() 매개함수 -> 슬록함수
        cbShowTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국', self)
        cbKorea.move(20,60)
        cbKorea.stateChanged.connect(self.changeKorea)

        rbMale = QRadioButton('남성', self)
        rbMale.move(150,20)
        rbMale.setChecked(True)     # 버튼의 선택 여부를 설정
        rbFemale = QRadioButton('여성', self)
        rbFemale.move(150,40)

        # 필수 설정
        self.setWindowTitle('버튼')
        self.setGeometry(300,300,300,300)
        self.show()

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked:  # Qt.Checked도 사용가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크해제')
    
    def changeKorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 머지?')
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())

