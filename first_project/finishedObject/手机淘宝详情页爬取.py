import requests
import re
import hashlib
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

#手动获取COOKIE
# cookies="t=7e5a9afd5d4cf99a0ca99af5e8abdb37; cookie2=1250b25120a54cd4535eb20ab1ddd19b; v=0; _tb_token_=fb579eaede3d8; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=5911c9eb818cfd951783d52c9991d179_1566378987359; _m_h5_tk_enc=8185cc5772c5ace6760c65f0dc52edf7; _fbp=fb.1.1566368545066.341569925; cna=P76cFXUbqX4CAW5TM415UVrd; isg=BPz8C30qjdMxqLkI0H4Z9RfszZpuXaLs39R1PtZ9COfKoZwr_gVwr3IDg4l88th3"
cookies = "WAPFDFDTGFG = % 2B4cMKKP % 2B8PI % 2BP7EeiFpO7 % 2BzlTjoUDd1dNO2bho0 % 3D;_w_tb_nick = chenyilong11223344;imewweoriw = 36hb66TPIemxYuqxi4ZY8CqlLYyhwGXe49uPvQ0Xpy8 % 3D;ockeqeudmj = m % 2BNHSJU % 3D;_cc_ = UIHiLt3xSw % 3D % 3D;_l_g_ = Ug % 3D % 3D;_nk_ = chenyilong11223344;_tb_token_ = e3b713b96533e;cookie1 = AQXNkEcByQbVHLxkQinxcTpDACjvH96Lk5B5s3P9BPw % 3D;cookie17 = UNGWOj8tyRkFRA % 3D % 3D;cookie2 = 108fb8bf83bca09ae704aebaad0d5a79;csg = d4a0063b;dnk = chenyilong11223344;lgc = chenyilong11223344;munb = 3107993908;sg = 480;sgcookie = 3pUxaQIMA5aD9Rx8sL7XLPaumUzyLCK7QTn8c2FoJ25j;skt = e43a797a970dcae8;t = 3d7f2a65436e24c8708d7a96338ba291;tracknick = chenyilong11223344;uc1 = ;cookie21 = WqG3DMC9FxUx;existShop = false;cookie14 = UoTbmhDe6IXlEw % 3D % 3D;cookie15 = VT5L2FSpMGV7TQ % 3D % 3D;uc3 = ;vt3 = F8dByuqgW % 2BZiY6rSB1I % 3D;id2 = UNGWOj8tyRkFRA % 3D % 3D;nk2 = AHLS8Y5LyU5l90wPTRq55bjC;lg2 = VT5L2FSpMGV7TQ % 3D % 3D;uc4 = ;nk4 = 0 % 40AhyE9023wScqnDBNV9pA2IUwDD3MGDDFIy3RaGQ % 3D;id4 = 0 % 40UgbuMZlAOXYe5wdN6BkX5P1OUNuK;unb = 3107993908;hng = CN % 7Czh - CN % 7CCNY % 7C156;cna = XXpVFhgUQRsCAavSqbCLYLVW;isg = BNXVALruJOtC3gCe8fIBCKi67tWP0onkQZG1QVd6kcybrvWgHyKZtONMfDQYtaGc;ucn = center;l = ArW1YQ2sy3S3fD3Ip4o8rVS7xSpvMmlE;enc = LajRPoqSWAzP % 2BGiS9gJUrMjvsWR3MZRlNxMrqsacSz % 2Fjiwp % 2BJdGIfuTrnDlNoMi72rwPBNF5e9z % 2FIcqwX32qsQ % 3D % 3D;thw = cn"
#从COOKIE里面获取token和时间戳
cookie_list = cookies.split(';')
cookie_dict={cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookie_list}
h5_tk = cookie_dict['_m_h5_tk'].split('_')[0]
t=cookie_dict['_m_h5_tk'].split('_')[1]
# h5_token : token  ; t  时间戳
# 签名是根据 token + 时间戳  +appkey+ 传进去的参数
def sign(data,t):
    appKey='12574478'
    strs = h5_tk+"&"+t+"&"+appKey+"&"+data
    # r.token + "&" + c + "&" + u + "&" + n.data
    m = hashlib.md5(strs.encode(encoding='utf-8')).hexdigest()
    return  m


d = '{"item_num_id":"544895066973"}'
page_url="https://h5api.m.taobao.com/h5/mtop.wdetail.getitemdescx/4.9/?jsv=2.4.11&appKey=12574478&t={0}&sign={1}&api=mtop.wdetail.getItemDescx&v=4.9&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22item_num_id%22%3A%22544895066973%22%7D"

sing_url = page_url.format(t,sign(d,t))
print(sing_url)
response = requests.get(sing_url,headers=headers, cookies=cookie_dict)
response=response.content.decode('utf-8')
images = re.findall(r'mtopjsonp2\((.+?)\)', response)
images=json.loads(images[0])
images_list=images["data"]["pages"]
for i in images_list:
    with open("//") as f:
        f.write(i)
