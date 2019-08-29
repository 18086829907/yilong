from bs4 import BeautifulSoup
with open('get1.html', 'r', encoding='gbk') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
token = soup.select('input[name="_token"]')[0]['value']
print(token)