import urllib.request
import urllib.parse
import execjs
#定义百度翻译v2transapi接口
post_url = 'https://fanyi.baidu.com/v2transapi' #在fiddler中请求窗口，URL列，复制对应接口的url
# 输入需要翻译的单词
quert = input('请输入您想查询的单词：')
# 打开百度翻译v2transapi接口的js文件
with open('baidusign.js') as f:
  jsCode = f.read()
# 将查询的单词传入js代码并用python调用js代码中的e函数，传输参数e函数的参数quert，获得返回值sign
# 注意：如果fiddler中抓取到的POST请求中有sign，即WebForm中有sign
#      需要用谷歌F12去捕获ajax响应的js文件，并分析js代码，找到类似baidusign.js的代码
sign = execjs.compile(jsCode).call('e', quert)
#伪造post参数,参数获取的方式：fiddler.v2transapi接口.Inspectors.Request.WebForms
data_form = {
  'from': 'en',
  'query': quert,
  'sign': sign,
  'simple_means_flag': 3,
  'to': 'zh',
  'token': '2062ab7729a8cb504cbc1913b24a5173',
  'transtype': 'realtime',
}
#预处理post参数
data_form = urllib.parse.urlencode(data_form).encode()
#伪造头部信息，头部信息获取方式：fiddler.v2transapi接口.Inspectors.Request.Raw,注意不要复制第一排，即POST http://...
headers = {
  'Host': 'fanyi.baidu.com',
  'Connection': 'keep-alive',
  # 'Content-Length': '121', //此条也要注释掉，这个是返回的内容长度，服务器会自动算返回文本的长度
  'Accept': '*/*',
  'Origin': 'https://fanyi.baidu.com',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
  # 'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'BAIDUID=0BD6A8EB50BB9073779F057D56426E59:FG=1; BIDUPSID=0BD6A8EB50BB9073779F057D56426E59; PSTM=1554281453; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=ZiY1EzM2hQWDN4bDFtME1kfmFBOENUMTRld1VxcDd3UWFmbnpPQUxVOGd2Q05kSVFBQUFBJCQAAAAAAAAAAAEAAACK0jWGwfrBvNPqMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAv~FwgL~xcSE; CHINA_PINYIN_SWITCH=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561847780,1561849112,1561873096,1561882295; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1561883366; yjs_js_security_passport=7909d1a932a5b58e24257dd1b0a3ec14f5d6e9d4_1561883368_js',
}
request = urllib.request.Request(url=post_url, headers=headers)
response = urllib.request.urlopen(request, data_form)
print(response.read().decode())