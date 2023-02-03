# 다중입력
# x, y = input('두 영단어를 입력하세요 > ').split()
# # split(',')
# print(x)
# print(y)

# 완전 다중입련(개수가 몇개든지 상관없음)
# 중요!!!

inputs = list(map(str, input('단어를 입력하세요(개수상관X) > ').split()))   # map() : 자료형 바꿈
print(inputs)