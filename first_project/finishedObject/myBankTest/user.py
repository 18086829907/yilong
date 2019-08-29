class User(object):
    def __init__(self, name, idCard, phone, card, journal):
        self.name = name
        self.phone = phone
        self.idCard = idCard
        self.card = card #卡对象
        self.journal = journal #日志对象