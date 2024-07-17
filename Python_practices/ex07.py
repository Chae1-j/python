import sys
# 파일 입출력 활용
"""
open : 파일 객체를 여는 명령어 <> close(자원 점유 해제)
"""
# 파일 디렉토리 다루기


# ------------------------------------------------------- 실습 ------------------------------------------------------
# 표준 출력을 파일로 변경하여 구구단을 파일에 저장하는 코드 작성
for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))

f = open('b.text')

# 2. 바탕화면에 python 폴더 생성 후 파일 생성
"""
txt = "Hello, World"

f = open('test.txt', 'w')
f.write(txt)
f.close 

import os
os.mkdir('test') # 기본 경로에 생성됨
os.getcwd()

os.mkdir('바탕화면 경로 적기~')
r = open('절대경로 입력', 'w')
os.chdir()

"""
