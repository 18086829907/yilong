import requests
response = requests.get('http://101.205.52.157:8000/random')
proxy = response.text
proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response= requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)