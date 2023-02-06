# 패키지 내 불러오기
from urllib.request import Request, urlopen
# 파이썬 표준 라이브러리 urllib 패키지 내의 request 모듈 가져오기
# Request 클래스

# 인터넷이란 네트워크를 통한 request and response
req = Request('https://www.naver.com')    #생성자
res = urlopen(req)
print(res.status)   # 200



