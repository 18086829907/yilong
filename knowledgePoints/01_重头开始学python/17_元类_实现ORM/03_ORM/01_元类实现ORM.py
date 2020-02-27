# ORM，对象-关系映射
#   即，用对象操作关系型数据库

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        # 判断是否需要保存
        for k,v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            if isinstance(v, tuple):
                # print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password/应的对象引用/类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class User(object, metaclass=ModelMetaClass):  # ModelMetaClass('User',(object,),{'uid':('uid', 'int unsigned'), ...})
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')
    # 当指定元类之后，以上类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     'uid': ('uid', 'int unsigned')
    #     'name': ('username', 'varchar(30)')
    #     'email': ('email', 'varchar(30)')
    #     'password': ('password', 'varchar(30)')
    # }
    # __table__ = 'User'
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)  # 等价于self.name=value,添加一个实例属性,但是如果直接用self.name=value,是表示一个实例属性的变量名为name,而不是name里面的值作为变量名。如果最终想用name中的值作为变量名，则需要用到setattr()

    def save(self):
        fields = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))  # 等价于 从self.k中获取值，但是如果写self.k，是表示一个实例属性的变量名为k，而不是k里面的值作为变量名。如果最终想用k中的值作为变量名，则需要用到getattr()

        sql = 'insert into %s(%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))


        print('SQL: %s' % sql)

u = User(uid=12345, name='Michael', email='test@orm.org', password='my_pwd')
u.save()
print('有bug，最终生成的sql语句没有带引号')

# 总结：
#   class User中的类属性可以理解为建表，因此类属性中的value[0]表示的是数据库的列名
#   User()实例化时，所传入的值，是插入到数据库的value