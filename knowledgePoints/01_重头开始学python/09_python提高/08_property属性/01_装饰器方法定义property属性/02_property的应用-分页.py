class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10  # 定义一页显示的条数

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = (self.current_page) * self.per_items
        return val

if __name__ == '__main__':
    page = Pager(2)
    print(page.start)
    print(page.end)