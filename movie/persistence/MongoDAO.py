from pymongo import MongoClient   # 클래스 작성>MongoDAO, 객체생성> daummovie, 인스턴스 사용

class MongoDAO:
    reply_list = []  # MongoDB Document 를 담은 list 선언

    def __init__(self):
        # >> MongoDB Connection
        self.client = MongoClient('127.0.0.1', 27017)  # 클래스 객체 할당(ip, port)
        self.db = self.client['local']    # MongoDB의 'local' DB를 할당
        self.collection = self.db.get_collection('movie')  # 동적으로 collection 선택

    # MongoDB에 Insert
    def mongo_write(self, data):
        print('>> MongoDB WRITE DATA:)')
        self.collection.insert(data)  # JSON Type = Dict Type(Python)

    # MongoDB 에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id': 0, 'content': 1, 'score': 1}):
            self.reply_list.append([one['title'], one['content'], one['score']])  # dict 에서 value 와 score 만 추출
            return self.reply_list