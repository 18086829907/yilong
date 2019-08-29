from django.db import models

# Create your models here.

class myManager(models.Manager):
    def createCommodity(self, picture, commodityName, commodityAttr, price, discount, originalPrice, advantage,  policy,  isDelete=False):
        commodity = self.model()
        commodity.picture = picture
        commodity.commodityName = commodityName
        commodity.commodityAttr = commodityAttr
        commodity.price = price
        commodity.discount = discount
        commodity.originalPrice = originalPrice
        commodity.advantage = advantage
        commodity.policy = policy
        commodity.isDelete = isDelete
        commodity.save()
        return commodity

class Wheel(models.Model):
    picture = models.CharField(max_length=150, db_column='轮播图片')
    commodityName = models.CharField(max_length=20, db_column='商品名字')
    trackId = models.CharField(max_length=20, db_column='跳转id')
    isDelete = models.BooleanField(default=False, db_column='是否删除')
    def __str__(self):
        return self.commodityName
    class Meta:
        db_table = 'Wheel'
        ordering = ['id']

class Commodity(models.Model):
    myComObjects = myManager()
    picture = models.CharField(max_length=100, db_column='商品图片')
    commodityName = models.CharField(max_length=100, db_column='商品名字')
    commodityAttr = models.CharField(max_length=100, db_column='商品属性')
    price = models.FloatField(db_column='商品价格')
    discount = models.FloatField(db_column='商品折扣')
    originalPrice = models.FloatField(db_column='商品原价')
    advantage = models.CharField(max_length=20, db_column='商品优势')
    policy = models.CharField(max_length=20, db_column='商品政策')
    isDelete = models.BooleanField(default=False, db_column='是否删除')
    lastTime = models.DateTimeField(auto_now=True, db_column='修改时间') #时间类型，自动保存最后一次修改数据的时间，比如修改学生名字，修改的时间会自动保存到lastTime中
    createTime = models.DateTimeField(auto_now_add=True, db_column='创建时间') #时间类型，创建学生对象时自动记录当前时间
    def __str__(self):
        return self.commodityName
    class Meta:
        db_table = 'Commodity'
        ordering = ['id']