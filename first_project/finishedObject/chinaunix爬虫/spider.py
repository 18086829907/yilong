import requests
from bs4 import BeautifulSoup
import time
#伪造头
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
#get请求登录页面
get1_url = 'http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F'
s = requests.Session()
get1_res = s.get(url=get1_url, headers=headers)
#保存为本地html方便测试bs4
# with open('get1.html', 'w', encoding='gbk') as f:
#     f.write(get1_res.text)
#解析登录页面获取token值
soup = BeautifulSoup(get1_res.text, 'lxml')
_token = soup.select('input[name="_token"]')[0]['value']
#from表单中_t值的分析思路
#是否存在与html中
#   否：肯定是通过ajax动态加载js代码生成的
#       抓包分析js代码
#           在js中搜索_t
#               发现 'ajax':function(e){ e.data["_t"] = (new Date).getTime()}
#                   确定_t是13位时间戳
#                       在python中用time.time()创造一个13位时间戳来伪造_t值
date = str(time.time()).split('.')
new_date = date[0]+date[-1][:3]
_t = new_date
#post请求登录
post_url = 'http://account.chinaunix.net/login/login'
post_data = {
    'username':'18086829907',
    'password':'135cylpsx',
    '_token': _token,
    '_t': new_date,
}
post_res = s.post(url=post_url, headers=headers, data=post_data)
#访问登录后的页面
get2_url = 'http://bbs.chinaunix.net/home.php?mod=space&uid=69937883&do=profile'
get2_res = s.get(url=get2_url, headers=headers)
#保存登录后的界面
with open('get2.html', 'w', encoding='gbk') as f:
    f.write(get2_res.text)