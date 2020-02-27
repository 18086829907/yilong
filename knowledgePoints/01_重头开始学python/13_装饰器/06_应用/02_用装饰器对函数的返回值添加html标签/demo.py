def add_td(func):
    def inner_func():
        return '<td>'+func()+'</td>'
    return inner_func

def add_h1(func):
    def inner_func():
        return '<h1>'+func()+'</h1>'
    return inner_func

@add_td
@add_h1
def get_str():
    return 'haha'

print(get_str())