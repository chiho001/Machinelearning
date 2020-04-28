from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#urlopen으로 데이터 가져오기
res = req.urlopen(url)

#Beautifulsoup으로 분석하기
soup = BeautifulSoup(res,"html.parser")
#원하는 데이터 추출하기
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)





###############################
# from bs4 import BeautifulSoup
# html = """
# <html><body>
#   <ul>
#     <li><a href="http://www.naver.com">naver</a></li>
#     <li><a href="http://www.daum.net">daum</a></li>
#   </ul>
# </body></html>
# """
# #HTML 분석하기
# soup = BeautifulSoup(html,'html.parser')
# #find_all 메서드로 추출하기
# links = soup.find_all("a")
# #링크 목록 출력하기
# for a in links:
#     href = a.attrs['href']
#     text = a.string
#     print(text,">",href)
