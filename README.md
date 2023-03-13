# studyPython
부경대 IoT 파이썬 학습 리포지토리


## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Stduio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력

```python
# desc : 콘솔출력 - 주석
print('Hello, Python!!') # 콘솔출력 함수
```
<img src="https://raw.githubusercontent.com/JuHyunLee99/basic-Python/main/images/console_print.PNG" width="780" />
실행화면

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
    - 흐름제어

```python
# 변수
val = 1

# 자료형
print(type(val))    # <class 'int'>

# 문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.')        # 파이는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.')   # 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')  # 파이는          3.142입니다.
```

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수

```python
# 가변인자 *args
# 매개변수 개수가 일정치 않은 경우
def adds(*args):
    result = 0
    for i in args:
        result += i
    return result
    
print(adds(1, 2, 3, 4))
```

```python
# 람사함수
# 함수 중에서 인라인으로 간결하게 만든 뒤 한번 사용하고 더 이상 사용하지 않을 함수를 만들 때 사용 
print((lambda x, y: x+y)(7, 4))
```
>**디버깅 F5**
- 오류를 찾거나 소스코드 이해를 위해 사용
- 중단점, 변수, 조사식
- F10 : 다음 행 실행
- F11

## 4일차
1. 파이썬 기본
    - 가상환경  
    : 글로버 버전과 다른 독립적인 가상의 환경
    - 객체지향 OOP(클래스)
    - 패키지, 모듈
        - math 모듈

가상환경 실행
```shell
PS C:\Source\studyPython> cd .\venv\Scripts\
PS C:\Source\studyPython\venv\Scripts> .\activate.ps1
```

## 5일차
1. 파이썬 기본
    - 패키지, 모듈 계속
        - ramdom 모듈
        - 파이썬 표준 라이브러리 urllib 패키지 내의 request 모듈
        - 외부 라이브러리 requests 패키지
    - 입출력 다시
        - 공공데이터포터 csv파일 읽기 (csv 라이브러리)
    - 예외처리

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속
2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/JuHyunLee99/studyPython/blob/main/Project/address_app.py)
<!-- HTML 주석
![실행화면](https://raw.githubusercontent.com/JuHyunLee99/studyPython/main/images/address_app.png)
-->
<img src="https://raw.githubusercontent.com/JuHyunLee99/studyPython/main/images/address_app.png" width="780" />
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성 : 파일메뉴 > 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)
        - json 라이브러리

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
        - BeautiifulSoup 크롤링

![실행화면](https://github.com/JuHyunLee99/studyPython/blob/main/images/jupyter_folium.png)

실행화면

## 9일차
1. 파이썬 응용
    - GUI 개발
        - Tkinter 소개
        - PyQt 소개, 설치

## 10일차
1. 파이썬 응용
    - GUI 개발
        - 위젯 계속
        - PyQT 다이얼로그

![실행화면](https://github.com/JuHyunLee99/studyPython/blob/main/images/dialog.png)

PyQt 실행화면

