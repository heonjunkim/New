import requests
from bs4 import BeautifulSoup

cnt = 0
for page in range(1, 6):
    list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p={}'.format(page)
    resp = requests.get(list_url)

    if resp.status_code != 200:
        print('WARNING: 잘못된 URL 접근!!')


    soup = BeautifulSoup(resp.text, 'html.parser')
    board_list =soup.select('tbody#bbsResult >tr > td > a:not(.name_more)')



print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'.format(cnt))



