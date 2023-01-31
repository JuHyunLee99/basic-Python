# 자료형
#None 값이 없는 값
None

print(None)
print(0 == None)    #False
print('' == None)   #False

#숫자형
#type() : 자료형 반환 함수
val = 3
print(type(val))    #int

val = 3.14
print(type(val))    #float

val = 'Hello'
print(type(val))    #string

val = 0b1010
print(type(val))    #int

val =  12.334546564334243432543543
print(type(val))    #float

val = 4_520_000
print(val)  #4520000

val = 3_099.99
print(val)  #3099.99

#문자열
val = 'Life is short, You need Pyton.'
print(val)
print(type(val))

val = 'Hell\nWorld!'    # \n escape 문자
print(val)
val = 'Hell\tWorld!'    # \t 탭
print(val)
val = 'Hell\t\bWorld!'    # \b 
print(val)

val = '''Life is short,
You need Python'''      # ''' ''' : 탈출문자 \n 보다 편함
print(val)

# "",'' 같음. 보통 ''사용권장
# 문자'를 출력하는 경우에는 ""가 더 편함
# ''을 쓸 경우  특수문자 \' 사용
val = "Hi, I'm 'Juhyun'"
print(val)

val = 'Hi, I\'m \'Juhyun\''
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))   # bool

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1))  # 1 == True
print(bool(0))  # 0 == Flase
print(bool(3))  # 1이외 값은 True라고 하지 말것
