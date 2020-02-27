from pymysql import connect
import sys


class Info_idGrade_idUnit:
    def __init__(self):
        self.grade = {'小学一年级上册': 1,'小学一年级下册': 2,'小学二年级上册': 3,'小学二年级下册': 4,'小学三年级上册': 5,'小学三年级下册': 6,'小学四年级上册': 7,'小学四年级下册': 8,'小学五年级上册': 9,'小学五年级下册': 10,'小学六年级上册': 11,'小学六年级下册': 12,'初中一年级上册': 13,'初中一年级下册': 14,'初中二年级上册': 15,'初中二年级下册': 16,'初中三年级上册': 17,'初中三年级下册': 18,'高中一年级上册': 19,'高中一年级下册': 20,'高中二年级上册': 21,'高中二年级下册': 22,'高中三年级上册': 23,'高中三年级下册': 24,'大学一年级上册': 25,'大学一年级下册': 26,'大学二年级上册': 27,'大学二年级下册': 28,'大学三年级上册': 29,'大学三年级下册': 30,'大学四年级上册': 31,'大学四年级下册': 32,'博士一年级上册': 33,'博士一年级下册': 34,'博士二年级上册': 35,'博士二年级下册': 36,'博士三年级上册': 37,'博士三年级下册': 38,'博士四年级上册': 39,'博士四年级下册': 40}
        self.unit ={'Unit_1':1,'Unit_2':2,'Unit_3':3,'Unit_4':4,'Unit_5':5,'Unit_6':6,'Unit_7':7}

class operation_sql(Info_idGrade_idUnit):
    def __init__(self, grade, unit, word_dict, sentence_dict):
        super().__init__()
        self.id_grade = self.grade[grade]
        self.id_unit = self.unit[unit]
        self.word_dict = word_dict
        self.sentence_dict = sentence_dict

        self.conn = connect(host='localhost', port=3306, user='root', password='135cylpsx', database='english_learn', charset='utf8')
        self.cursor = self.conn.cursor()

    def inserWord(self):
        # sql字段解释：id占位, 年级id, 单词/句子类型id, 单元id, 单词/句子, 翻译
        sql = """insert into word_and_sentence value (0, %s, 1, %s, %s, %s)"""
        for key,value in self.word_dict.items():
            self.cursor.execute(sql, [self.id_grade, self.id_unit, key, value])


    def inserSentence(self):
        # sql字段解释：id占位, 年级id, 单词/句子类型id, 单元id, 单词/句子, 翻译
        sql = """insert into word_and_sentence value (0, %s, 2, %s, %s, %s)"""
        for key,value in self.sentence_dict.items():
            self.cursor.execute(sql, [self.id_grade, self.id_unit, key, value])

class InsertInto(operation_sql):
    def __init__(self, grade, unit, word_dict, sentence_dict):
        super().__init__(grade, unit, word_dict, sentence_dict)

    def run(self):
        self.inserWord()
        self.inserSentence()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def run(myGrade, myUnit):
    sys.path.append('../data_word_sentence')
    model_word_sentence = __import__(myGrade)
    app = getattr(model_word_sentence, 'application')
    word_dict, sentence_dict = app(myUnit)
    inser = InsertInto(myGrade, myUnit, word_dict, sentence_dict)
    inser.run()

def main():
    run('小学四年级上册', 'Unit_1')

if __name__ == '__main__':
    main()