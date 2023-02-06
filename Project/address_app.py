# 주소록앱
# 2023-02-06
# Juhyun.LEE
class Contact:
    #생성자 선언 - 이름, 전번, 이메일, 주소
    def __init__(self, name, phone_number, e_mail, addr) -> None:
        self.__name = name
        self.__phone_number = phone_number
        self.__e_mail = e_mail
        self.__addr = addr

    # __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_number}\n'
                   f'이메일 : {self.__e_mail}\n'
                   f'주  소 : {self.__addr}')
        return str_res

def run():
    temp = Contact('이주현', '010-9466-2399', 
                    'juhyun.lee0829@daum.net','경남 양산시 ...')
    print(temp)

if __name__ == '__main__':
    print('주소록앱 시작합니다.')
    run()


