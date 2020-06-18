# 다음에서 뉴스 한건의 기사와 내용을 수집

import requests
from bs4 import BeautifulSoup

# url은 내가 수집하고 싶은 데이터가 위치한 웹사이트 주소를 가리킴!
url = 'https://news.v.daum.net/v/20200615160826651'
# url 주소를 이용해서 해당 웹페이지의 모든 소스코드를 불러와서 resp에 저장
resp = requests.get(url)

# resp에 status_code가 200이면 성공, 나머지는 실패
if resp.status_code == 200:
    print('success')
else:
    print('Wrong URL')
# requests는 소스코드지만 전부 가져오는거고 거기서 원하는 내용은 추출 불가!
# 원하는 내용만 추출하려면 beautifulsoup을 사용해야함
# beautifulsoup에 input으로 resp의 값(웹사이트의 소스코드 전체)을 전달
# soup에 웹사이트의 소스코드 전체가 저장
# soup.select()를 이용하여 원하는 정보만 추출
soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.select('h3.tit_view') # (태그+선택자)
contents = soup.select('div#harmonyContainer p')
# soup.select()는 무조건 return을 list type으로 변환
# [val1, val2, val3, ...]
# ex) contents[1]

print(title[0].text)
print('-------------------------------------------------------------')
print(contents)

text = ''
for i in contents:
    text += i.text

print(text)

#list 1건식 꺼내서 더하면
