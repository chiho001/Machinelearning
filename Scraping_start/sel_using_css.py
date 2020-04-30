from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#CSS 선택자로 추출
print(soup.select_one("li:nth-of-type(8)").string)

