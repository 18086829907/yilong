import re


def main():
    while True:
        email = input('请输入邮箱：')
        res = re.match(r'[a-zA-Z0-9_]{4,20}@.{2,3}\..{2,3}$', email)    #不要使用\w，因为包含匹配中文，\是转义符
        if res:
            print('输入正确，您的邮箱号为：{}'.format(res.group()))
            break
        else:
            print('不符合正确的邮箱格式，请重新输入')


if __name__ == '__main__':
    main()

