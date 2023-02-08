# 외부 패키지 requests를 사용
import requests # HTTP를 사용하기 위해 쓰여지는 라이브러리

res = requests.get('https://naver.com')
print(res.status_code)
print('================')
print(res.content)


