import requests
from bs4 import BeautifulSoup
# 제목
# 내용
# 작성일자
# 작성자

url = 'http://news.sarangbang.com/talk/bbs/free/163757?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dfree'

resp = requests.get(url)

if resp.status_code != 200:
    print('WARNING: 잘못된 URL 접근!!')

soup = BeautifulSoup(resp.text, 'html.parser')


title = soup.select('h3.tit_view')[0].text.strip()
writer = soup.select('a.name_more')[0].text.strip()
reg_dt = soup.select('span.tit_cat')[1].text.strip()[:10]  # 구조가 같을때만 하는것, 다르면 다르케 해줘야함
# 년월일만 시간제외[:10]< 파이썬에서 배운것
contents = soup.select('div.bbs_view p')
content = ''
for i in contents:
    content += i.text.strip()

print('TITLE▶▶▶▶▶▶', title)
print('WRITER▶▶▶▶▶▶', writer)
print('REGIDATE▶▶▶▶▶▶',reg_dt)
print('CONTENTS▶▶▶▶▶▶', content)

