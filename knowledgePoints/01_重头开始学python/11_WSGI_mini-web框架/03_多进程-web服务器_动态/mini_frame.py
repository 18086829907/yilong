import time

def login():
    return 'welcome login...time:%s' % time.ctime()

def register():
    return 'welcome register...time:%s' % time.ctime()

def center():
    return 'welcome center...time:%s' % time.ctime()

def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    elif file_name == '/center.py':
        return center()
    else:
        return 'not found you page'