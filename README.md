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

![실행화면](https://raw.githubusercontent.com/JuHyunLee99/studyPython/main/images/address_app.png)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성 : 파일메뉴 > 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)
        - json 라이브러리

# 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
    - 자료구조 추가
    - 윈폼 개발(GUI)
    - 응용 학습

