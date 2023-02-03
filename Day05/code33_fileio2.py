# 파일 읽어오기
file = open('./Day05/sample01.txt', 'r', encoding = 'utf-8')    # 'r': 읽기 모드

# read()    전체 다 읽어오는 함수
# readline() 한줄 읽어오는 함수
# readlines() 모든 줄 다 읽는 함수
while True:
    text = file.readline()

    if not text: break

    print(text,end='')


file.close()    # 파일을 open하면 무조건 close 해야함