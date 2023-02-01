# 함수
# 함수만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴X
# 3. 파라미터X 리턴O
# 4. 파라미터X 리턴X

# 함수정의
def add(x, y):
    result = x + y
    print(result)
    return      # return 생략가능

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def hello():
    print('Hello~!!!')
    return

def hello2():
    msg = 'Hello, Hello'
    return msg

# 매개변수 개수가 일정치 않은 경우
def adds(*args):
    result = 0
    for i in args:
        result += i

    return result

# 함수호출
add(1024, 5)
sub(1024, 1000)
mul(512, 2)
div(108, 10)

hello()
print(hello2())

print(adds(1, 2, 3, 4))
print(adds(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
