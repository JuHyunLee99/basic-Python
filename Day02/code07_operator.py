# 연산자
# 할당연산 assignment
# 2 = 1 (X)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(10 *10)
print(1024 / 2) # 소수나누기
print(1024 //2) # 정수나누기
print(2 // 3) 
print(1024 % 2) # 나머지 // 배수찾을 때 이용

# print(6 / 0) 오류: 무한대
# print(6 // 0)

print(2 ** 10)  # 2의 10제곱

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)
print(first, second)
print(first + ' ' + second)

print(first * 4)
# 문자열 연산은 +, * 만 존재 -, / 존재X

#문자열 길기
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) 인덱스 오류

# 파이썬에 인덱스 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])
print(current[-19:4])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)

# que[5] = 10 오류 
que.append(10)      # 맨 마지막에 추가
print(que)

que.insert(3,99)    # 특정 인덱스에 추가
print(que)

que.remove(99)      # 해당 값 삭제
print(que)

# 튜플은 요소의 추가, 수정, 삭제가 불가!
tup = (1, 2, 3, 4, 5)
# tup[1] = 9    오류
print(tup)

# 문자열 == 문자 리스트
title = 'python'
print(title[0])

# title[0] = 'P' # 문자열에서는 값변경 X
print('P' + title[1:])

text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you, {1}!!".format(2, 'Hey'))
# 최신식 문자열 모팻팅
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')

# 문자열 특정문자로 자르기 split()
full_name = 'Ju Hyun. LEE'
vals = full_name.split() # 스페이스
print(type(vals))
print(vals)

vals = full_name.split('.') # .으로 지정
print(vals)

# 문자열 특정단어 바꾸기 reokace()
print(full_name.replace('Ju Hyun.', 'Claire'))

# 문자열 공백 없애기
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|')
print(hi.rstrip() + '|')
print(hi.strip() + '|')

# 문자열 문자및 단어의 시작위치 찾기 
# index() 
print(full_name.index('H'))
# print(full_name.index('K'))   # 찾는 게 없으면 에러

# find()
print(full_name.find('H'))
print(full_name.find('K'))  # 찾는 게 없으면 -1
# index()보다 find()가 편함

#문자열에서 찾는 단어의 갯수
print(full_name.count('u')) # 2

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)

