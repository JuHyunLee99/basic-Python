# 이미지 처리
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 텍스트 에디트
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        # 상태바
        self.statusBar()
        # 액션 - 파일열기
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onClicked)
        # 메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # 파일 메뉴
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)    # 파일메뉴에 액션(파일열기) 추가

        # 필수설정
        self.setWindowTitle('파일다이얼로그 위젯')
        self.setGeometry(300,300,300,300)       
        self.show()

    def onClicked(self):    # FileDialog, 파일 열고, 텍스트 읽기, 텍스트 에디트에 텍스트 set
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')

        if fname[0]:    # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')   # 'rt' : 읽는데 텍스트만 읽음
            with file:
                data = file.read()
                self.textEdit.setText(data)

            file.close()
        
        QMessageBox.about(self,'성공','로드했습니다')

    def closeEvent(self, event) -> None:    # # 프로그램 종료
        reply = QMessageBox.question(self, '종류', '정말 종료하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # QMessageBox.question(slef, 제목, 내용, 버튼종류(yes, no), 기본선택 no)

        if reply == QMessageBox.Yes:
            event.accept()  # 프로그램 종료
        else:
            event.ignore()  # 그대로 프로그램 계속 진행
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





