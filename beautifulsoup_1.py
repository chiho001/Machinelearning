#파이썬으로 스크레이핑할 떄 쓰는 라이브러리는 Beautiful Soup
#최근 스크레이핑 라이브러리는 다운로드부터 HTML분석까지 모두 해주는 경우가 많은데, BeautifulSoup는 어디까지나 HTML XML을 분석해주는 라이브러리이다.
#BeautifulSoup 자체에는 다운로드 기능이 없으니 주의 해주세요.

from bs4 import BeautifulSoup
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""
# HTML 분석하기 --- (※3)
soup = BeautifulSoup(html,'html.parser') #BeautifulSoup 인스턴스 생성 ,html지정, parser의 종류 지정(HTML분석시에는 html.parser지정)
# 원하는 부분 추출하기 --- (※4)
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
# 요소의 글자 출력하기 --- (※5)
print("h1 = " + h1.string)
print("p  = " + p1.string)
print("p  = " + p2.string)