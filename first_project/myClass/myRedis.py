import redis
class MyRedis(object):
    def __init__(self, password, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=password)
    #设置字符串
    def set(self, key, value):
        self.__redis.set(key, value)
    #设置哈希
    def hset(self, key, field, value):
        self.__redis.hset(key, field, value)
    #设置列表
    def lpush(self, key, *args):
        for value in args:
            self.__redis.lpush(key, value)
    #设置列表
    def rpush(self, key, *args):
        for value in args:
            self.__redis.lpush(key, value)
    #设置集合
    def sadd(self, key, *args):
        for value in args:
            self.__redis.sadd(key, value)

    def get(self, key):
        if self.__redis.exists(key):
            value = self.__redis.get(key).decode('utf-8')
            return value
        else:
            return False

    def hget(self, key, field):
        if self.__redis.exists(key):
            value = self.__redis.hget(key, field)
            return value
        else:
            print('can’t find the key!')

    def lrange(self, key, start, end):
        if self.__redis.exists(key):
            value = self.__redis.lrange(key, start, end)
            return value
        else:
            print('can’t find the key!')

    def smembers(self, key):
        if self.__redis.exists(key):
            value = self.__redis.smembers(key)
            return value
        else:
            print('can’t find the key!')

if __name__ == '__main__':
    r = MyRedis('135cylpsx4848@')
    r.set('str3', 'guoguo')
    r.hset('hash3', 'name', 'duoduo')
    r.rpush('lis5', 'a', 'b', 'c', 'd')
    r.lpush('lis5', 'a', 'b', 'c', 'd')
    r.sadd('set3', 'a', 'b', 'c', 'd')
    print(r.get('str3'))
    print(r.hget('hash3', 'name'))
    print(r.lrange('lis3', 0, -1))
    print(r.smembers('set3'))