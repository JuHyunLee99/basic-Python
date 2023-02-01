# 람다함수
def add(x, y):
    return x + y

print(add(7, 4))

# 함수 중에서 인라인으로 간결하게 만든 뒤 한번 사용하고 더 이상 사용하지 않을 함수를 만들 때 람사함수 사용
print((lambda x, y: x+y)(7, 4))
# 지금은 사용하지 말자
