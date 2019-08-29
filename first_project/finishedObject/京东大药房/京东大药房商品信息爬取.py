
#大药房 -> 中西药品 -> 滋补
url = 'https://list.jd.com/list.html?cat=9192,12632,12634&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
urls = []
for i in range(1, 206):
    urls.append(url.format(i))

for i in urls:
    print(i)

