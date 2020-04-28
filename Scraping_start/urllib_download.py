
########################################################################################################################
# urlopen()파일으로 저장
import urllib.request

#URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
# 다운로드
mem = urllib.request.urlopen(url).read() # png파일의 url 리소스를 엽니다. 그리고read()함수로 데이터를 읽어들임.
#파일로 저장하기
#밑에서 f는 open함수가 리턴하는 객체 file object를 뜻한다.
with open(savename, mode="wb") as f:
    f.write(mem) #다운로드한 바이너리 데이터를 파일에 저장
print("저장되었다")

########################################################################################################################
# #라이브러리 읽어 들이기
# request.urlretrieve()
# import urllib.request
# #URL과 저장 경로 지정하기
# url = "http://uta.pw/shodou/img/28/214.png"
# savename = "test.png"
# #다운로드
# urllib.request.urlretrieve(url,savename)
# print("저장완료!")



########################################################################################################################
# from selenium import webdriver
# USER = "<아이디>"
# PASS = "<비밀번호>"
# # PhantomJS 드라이버 추출하기 --- (※1)
# browser = webdriver.PhantomJS()
# browser.implicitly_wait(3)
# # 로그인 페이지에 접근하기 --- (※2)
# url_login = "https://nid.naver.com/nidlogin.login"
# browser.get(url_login)
# print("로그인 페이지에 접근합니다.")
# # 텍스트 박스에 아이디와 비밀번호 입력하기 --- (※3)
# e = browser.find_element_by_id("id")
# e.clear()
# e.send_keys(USER)
# e = browser.find_element_by_id("pw")
# e.clear()
# e.send_keys(PASS)
# # 입력 양식 전송해서 로그인하기 --- (※4)
# form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
# form.submit()
# print("로그인 버튼을 클릭합니다.")
# # 쇼핑 페이지의 데이터 가져오기 --- (※5)
# browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
# # 쇼핑 목록 출력하기 --- (※6)
# products = browser.find_elements_by_css_selector(".p_info span")
# print(products)
# for product in products:
#     print("-", product.text)