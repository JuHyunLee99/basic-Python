#모듈 사용
# math는 class로 안된 모듈임
import math as m    # as m : math를 간단히 m으로 사용

# code22_person는 우리가 만든 class인 모듈
import code22_person as p

from code23_car import Car  # 쓰고 싶은 것만 골라 쓸 수 있음

print(m.pi)
print(m.tan(0))
print(m.ceil(3.1))   # 올림
print(2 ** 10)
print(m.pow(2, 10))  # 제곱

# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')    
print(me)

#
mycar = Car()
print(mycar)