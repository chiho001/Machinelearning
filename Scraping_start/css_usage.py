#CSS 선택자
#목표
#HTML의 구조를 확인
#CSS 선택자
#웹브라우저(크롬이용)
#원하는 요소 선택하기
#HTML구조에서 Copy > Copy Selector 선택 시 선택 요소의 CSS 선택자가 클립보드에 복사

#CSS 선택자가 복사됩니다.
#mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(1) > a
#nth-child(n)이라는 것은 n번째에 있는 요소를 의미합니다.
#따라서 nth-child(7)이라는 것은 7번째에 있는 태그
#현재 페이지 좀더 분석하면 #mw-context-text 내부에 있는 ul 태그는 모두 작품과 관련된 태그

from bs4 import BeautifulSoup
import urllib.request as req8`
# 뒤의 인코딩 부분은 "저자:윤동주"라는 의미입니다.
# 따로 입력하지 말고 위키 문헌 홈페이지에 들어간 뒤에 주소를 복사해서 사용하세요.
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
# #mw-content-text 바로 아래에 있는
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# a 태그를 모두 선택합니다.
a_list = soup.select("#mw-content-text > div > ul:nth-child(6) > li > b > a")
for a in a_list:
    name = a.string
    print("-", name)
# #mw-context-text 바로 아래있는
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# a 태그를 모두 선택합니다.
