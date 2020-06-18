import requests
from bs4 import BeautifulSoup
import movie.persistence.MongoDAO as DAO

# 객체 생성
mDao = DAO.MongoDAO()


cnt = 0
page = 1
while True:

    url = 'https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('success')
    else:
        print('Wrong URL')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.review_info')

    if len(reply_list) == 0:
        print('마지막 페이지에요....')
        break
    print(page, 'page***********************************')
    for reply in reply_list:
        cnt += 1
        writer = reply.select('em.link_profile')[0].text.strip()
        score = reply.select('em.emph_grade')[0].text.strip()
        content = reply.select('p.desc_review')[0].text.strip()
        reg_date = reply.select('span.info_append')[0].text.strip()
        print('작성자', writer)
        print('평점', score)
        print('내용', content)
        index_val = reg_date.index(',')
        print('작성일자', reg_date[:index_val])
        print('==========================================')

        # MongoDB에 저장하기 위해 Dict Type 으로 변환!!
        data = {'content':content, 'writer':writer, 'score':score, 'reg_date':reg_date}
        #  내용, 작성자, 평점, 작성일자 MongoDB에 Save
        mDao.mongo_write(data)

    page += 1

print('수집한 영화댓글은 총{}건입니다.'.format(cnt))
