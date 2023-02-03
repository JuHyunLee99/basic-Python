# 글자 인코딩
# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode() -> 모든 나라언어를 다 표현가능

# 파일 만들기 # 파일/폴더 경로 # 절대경로: 경로 다 적는것 '/', '\' 둘 다 가능
# file = open('C:/DEV/Temp/Bank/sample01.txt', 'w', encoding = 'utf-8')  # 파일 쓰기로 만듦

# 상대 경로 # '.': 자기폴더  '..': 부모폴더
file = open('./Day05/../Day04/sample06.txt', 'w', encoding = 'utf-8')  # 파일 쓰기로 만듦

# 'w': 쓰기모드 'a': 추가모드
# 'utf-8' : 인코딩, 안하면 한글안됨.

file.write('안녕하세요~\n')
file.write('두번재 파일이다!!\n')
file.write('절대경로에 파일이 생성 될겁니다.')

file.close()    # 파일 닫기
print('sample01.txt가 생성되었습니다.')


