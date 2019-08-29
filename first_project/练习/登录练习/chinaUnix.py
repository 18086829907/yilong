import urllib.request
import urllib.parse

url = 'http://account.chinaunix.net/login/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

post_data = {
    'username':	'cd028cylpsx',
    'password':	'135cylpsx',
    '_token':	'eSqhJNCz0B2Is8AeaNXGKxcWMDabM2tT2JtNyiyR',
    '_t': '1562234602689',
}
post_data = urllib.parse.urlencode(post_data).encode()

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, post_data).read()
print(response)
with open('chianUnix.html', 'wb') as f:
    f.write(response)