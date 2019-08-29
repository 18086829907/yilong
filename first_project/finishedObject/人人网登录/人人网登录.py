import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
formdata = {
    'email':'18086829907',
    'icode':'origURL	http://www.renren.com/home',
    'domain':'renren.com',
    'key_id':'1',
    'captcha_type':'web_login',
    'password':'5a76a6568554a113c432e2128a2b6ec918002245fd9c74f791dc8d45ac0368cf',
    'rkey':'989e3881aff9ffbb691c3643103d3d2f',
    'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dq5RoRwPotEE8ps60VMke2E0A88cYDDg0If0EIAHkJWm%26wd%3D%26eqid%3Dd73fa756000f2504000000055d1e8279',
}
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201965628423'
s = requests.Session()
s.post(url=post_url, data=formdata, headers=headers)

get_url = 'http://www.renren.com/971351636/profile'
res = s.get(url=get_url, headers=headers)
res.encoding='utf8'
with open('人人网用户界面.html', 'w', encoding='utf8') as f:
    f.write(res.text)