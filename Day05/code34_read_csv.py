# 공공데이터포터 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv

fileName = 'busanbus.csv'
dirName = 'C:/Source/studyPython/'
fullPath = dirName + fileName

file = open(fullPath, 'r', encoding='utf-8')
# 'r' : 읽기모드, 파일을 읽어올 때 사용

reader = csv.reader(file, delimiter=',')    # delimiter 구분자
next(reader)    # next(): 다음 요소로 패스, 제목 줄 패스
# next(reader) 없으면 데이터가 아닌 제목도 출력됨

for line in reader:
    print(line)

file.close()    # 반드시 받아주세요!

# 결과: 리스트 형식