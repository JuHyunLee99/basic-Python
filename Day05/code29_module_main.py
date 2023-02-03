import code28_module_name

print(f'code29_module_name : {__name__}')   # __main__

# C int main(void) 동일
if __name__ == '__main__':         
    print('main을 실행합니다.')
    
# 임포트한 모듈의 print는 실행안됨
# code28_module_name : code28_module_name
# code29_module_name : __main__
# main을 실행합니다