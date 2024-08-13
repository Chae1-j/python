# 파이썬의 외부모듈
""""
- 외부모듈 참조 : 파이썬패키지 인덱스(PyPl)
- 외부모듈 설치하기
    1. 패키지 관리자 사용 (PIP) : console에서 pip install 설치파일
    2. 주피터 노트북 환경에서 설치 : 명령어 앞 ! 를 붙여 설치
    3. anaconda Navigator에서 설치 가능 : 환경설정 가능
    4. 일반 사용자 개발 모듈도 사용가능 ( git 등..)
"""
# 외부 모듈의 종류와 활용법
"""
- pymysql : pip install pymysql, MySQL을 파이썬에서 사용
    > 모듈 import, dusruf wjdqh wjddml(서버 주소:localhost, 127.0.0.1, 포트번호: 3306(마이sql의 기본 번호), 아이디, 비밀번호)
    ex) conn = pymysql.connect ( host='localhost', port=3306, user='root', passwd='<PASSWORD>', db='test') 
- 웹 크롤링 : beautifulSoup, pip install beautifulsoup4, 웹크롤링은 컴퓨터 소프트웨어 기술로 웹사이트들에서 원하는 정보를
추출하는 것을 말함
    > urllib 모듈로 웹 페이지 가져오기 : 응답과 요청(request)
"""

#----------------------------------------------------실습--------------------------------------------------------------
#1. beautifulSoup 모듈을 활용하여 급상승 검색어를 가져오는 웹 크롤링 코드 작성
import bs4
#import urllib from urllib.request import Request, urlopen
import urllib.request
url = "https://naver.com"
web_page = urllib.request.urlopen(url)

html_text = bs4.BeautifulSoup(web_page.read(),'html.parser')
print(html_text)
print(web_page.read())

a = html_text.find_all('li', class_='ah_item')
for i in a:
    print(i.text)