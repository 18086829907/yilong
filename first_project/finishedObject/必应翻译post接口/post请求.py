import requests
import json
import jsonpath

def EToZh(word):
    url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=48654C3FB7894B0C8B61C29E875AD977&IID=translator.5038.17'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
    formdata = {'fromLang':'auto-detect','text':word,'to':'zh-Hans',}
    res = requests.post(url=url, data=formdata, headers=headers)
    res.encoding = 'utf8'
    obj = json.loads(res.text)
    translation = jsonpath.jsonpath(obj, '$[0].translations[0].text')[0]
    return translation

if __name__ == '__main__':
    word = input('请输入您需要查询的英文：')
    translation = EToZh(word)
    print(translation)
