# 자동차 클래스
class Car:
    __number = '54라 9538'  # __number 외부에서 수정하지 못하도록 __ 사용

    # 먼저 __new__ 실행, 다음 __init__ 실행됨.
    def __init__(self, number = '54라 9538') -> None: # self를 받으며 객체의 내부에서 사용할 속성을 초기화
        self.__number = number
        print('__init__') 

    ## __new__ : 클래스 자체를 받으며 할당. 쉽게 말하면 Car 클래스를 만드는 것. 안씀.
    # def __new__(cls):       #  버전 3.1에서 쓰면 오류
    #     print('__new__')
    #     return super().__new__(cls)   # 부모클래스(상속)
    
    def __str__(self) -> str:   # instance 객체 출력(print) 시 자동으로 실행되는 특수 method이다.
        return f'내 차 번호는 {self.__number} 입니다.'

    def get_number(self):
        return self.__number
    
    # 클래스 외부에서 변경X, 멤버변수로는 내부 조작O
    def set_number(self, number):
        self.__number = number

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '55오 555'   # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)


mycar = Car()   # 생성
print(mycar)
print(f'제차는요, 아이오닉이고, 번호가 {mycar.get_number()}')

mycar.__number =  '132거 8888'  # 외부에서는 멤버변수에 접근불가
print(mycar)


    