# Car클래스를 상속한 제네시스 클래스
from code37_car import Car

# Child class
class Genesis(Car): # 클래스 Car를 상속받음

    def __init__(self, name, color, 
                plate_number, product_year) -> None:
        super().__init__()      # super() : 부모 클래스 뜻함.

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!')

    def set_name(self, name):
        self.__name = name
    

    # 메서드 재정의(오버라이드) : 부모클래스의 메서드를 자식 클래스에서 다시 재정의 하는 것.
    def get_name(self):
        return self.__name

    def run(self):  
        return f'{self.__name}이(가) 달립니다.'
    
    def stop(self):
        return f'{self.__name}이(가) 멈춥니다.'

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
# gv80.set_name('팔공이')
print(f'이차의 이름은 {gv80.get_name()}입니다.')
print(gv80.run())
print(gv80.stop())

