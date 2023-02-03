# 예외처리
def add(a, b):
    return a+b

def mul(a, b):
    return a*b

def div(a, b):
    return a / b

try:
    x,y = int, input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)

except Exception as e:
    print (e)
    exit()
finally:
    print('계속되나요?')    # 이거 실행뒤 종료됨

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()
    
print('계산 테스트')

try:
    print(div(x, y))    # y = 0일 때 예외 발생
except ZeroDivisionError as e:      # 개발할 때는 별로 사용할 일 없음.
    print('0으로 나누면 안되요!')
except Exception as e:              # Exception은 except 중 젤 마지막에 있어야함.
    print(e)
finally:
    print('계산은 계속됩니다!!')
# except:
#     print('예외가 발생했습니다.')

print(add(x, y))
print(mul(x, y))

