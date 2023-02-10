# 상태바 메뉴바 만들기
# 2023.02.09
# JHL

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 액션 - 종료
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)  # 액션(아이콘, 라벨, 부모, 위치할 부모 위젯)
        actExit.setShortcut('Ctrl+Q')   # 단축키 지정
        actExit.setStatusTip('앱 종료') # 마우스 올렸을 때 상태팁
        actExit.triggered.connect(qApp.quit)    # 이 동작을 선택했을 때, 생성된 (triggered)시그널이 
        # QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시킴.

        # 액션 - 저장
        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        # 메뉴바
        menubar = self.menuBar()    # 메뉴바 생성
        menubar.setNativeMenuBar(False) # mac native menu bar를 사용X
        filemenu = menubar.addMenu('&File') # 'File 메뉴 만들기     # '&'는 단축기 설정해줌. F 앞에 있으므로 Alt+F
        filemenu.addAction(actExit)     # 'File 메뉴에 actExit 동작 추가

        # 툴바
        toolbar = self.addToolBar('MainToolBar')    # 툴바 타이틀은 없어도 됨
        toolbar.addAction(actSave)  # 툴바에 액션 추가
        toolbar.addAction(actExit)


        #상태바 
        now = QDate.currentDate()   # 현재 날짜 반환
        time = QTime.currentTime()  # 현재 시간 반환

        # statusBar(): 최초 호출함으로써 상태바 만듬. 그 다음 호출부터는 상태바 객체를 반환
        # showMessage(): 상태바에 보여질 메세지를 설정 
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString())    # toSting() 날짜를 문자열로 
  

        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        self.setWindowIcon(QIcon('./Day09./iot.png'))
        self.resize(400,200)
        # 창을 화면 가운데로 띄우기
        self.setCenter()    

        self.show()

    def setCenter(self):
        qr = self.frameGeometry()   # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터 화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())