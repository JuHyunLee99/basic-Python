# 구구단 프로그램

for x in range(2, 10):
    print(f'{x}단')

    for y in range(1, 10):
        print(f'{x} X {y} = {x*y:>2}', end=' ')

# 디버깅 F5
# 중단점, 변수, 조사식 
# F10 다음 행 실행