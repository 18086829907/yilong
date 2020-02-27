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

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 定义一个父类，将元类和方法都定义在这个类中，方便创建简化版的子类
class Model(object, metaclass=ModelMetaClass):  # ModelMetaClass('Model', (object,) {})
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
    def save(self):
        fields = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))

        args_temp = list()
        for temp in args:
            # 如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = """insert into %s(%s) values (%s)""" % (self.__table__, ','.join(fields), ','.join(args_temp))

        print('SQL: %s' % sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')

u = User(uid=12345, name='Michael', email='test@orm.org', password='my_pwd')
u.save()
