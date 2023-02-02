# 클래스 생성
class Person:
#     pass        # 뭐할 지 생각나는 거 없을 때 pass 사용하면 오류 없음.
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self):     # __ 매직 메서드
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None:   # 색상 연한것: 매개변수 아직 사용안함 표시
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self):                  # self 무조건 기입
        print('걷습니다.')
    
    def run(self, option):    
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')   # self
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이(가)멈춥니다.')
    
    # 3. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성명은 {self.gender}입니다' 




# 생성자
juhyun = Person('이주현', 153, 'female')   # 객체의 instance 실체

# juhyun.name = '주현'
# juhyun.height = '153'
# juhyun.gender = 'female'
# juhyun.blood_type = 'RH+ B'

print(f'{juhyun.name}의 혈액형은 {juhyun.blood_type}')

juhyun.run('Fast')

# 1. 초기화 후 객체생성
# hong = Person('홍길동', 170, 'male')
hong = Person()
hong.run('Slow')

print('====================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)

#3. 생성자외 매직메서드(펑션) __str__
print(ashely)