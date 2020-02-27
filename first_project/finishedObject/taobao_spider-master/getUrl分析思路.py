urlBase = 'https://s.taobao.com/search?'
page1 = 'ie=utf8&initiative_id=staobaoz_20200202&stats_click=search_radio_all%3A1&js=2&imgfile=&q=%E5%A5%B3%E7%94%A8%E6%80%A7%E7%8E%A9%E5%85%B7&suggest=0_1&_input_charset=utf-8&wq=%E5%A5%B3%E7%94%A8&suggest_query=%E5%A5%B3%E7%94%A8&source=suggest'
page2 = 'data-key=s&data-value=132&ajax=true&_ksTS=1580613373484_1162&callback=jsonp1163&ie=utf8&initiative_id=staobaoz_20200202&stats_click=search_radio_all%3A1&js=2&imgfile=&q=%E5%A5%B3%E7%94%A8%E6%80%A7%E7%8E%A9%E5%85%B7&suggest=0_1&_input_charset=utf-8&wq=%E5%A5%B3%E7%94%A8&suggest_query=%E5%A5%B3%E7%94%A8&source=suggest&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s=88'
parseList1 = sorted(page1.split('&'))
parseLsit2 = sorted(page2.split('&'))

identical = []
Different = []
for parse in parseLsit2:
    if parse in parseList1:
        # print('相同参数有：{}'.format(i))
        identical.append(parse)
    if parse not in parseList1:
        # print('不同参数有：{}'.format(i))
        Different.append(parse)

print('相同参数，全部取：',sorted(identical))
print('不同参数，要取页码相关，不取json相关（）：',sorted(Different))

# 页码相关：页码，起始值，结束值，展现量
#   页码 = 自定义的传参（从零开始的正整数：0,1,2...）
#   展现量 = 结束值-起始值
#   起始值 = 页码 * 展现量
#   结束值 = 起始值 + 展现量
# 特别说明：
#   出现页码相关的参数，需要跳转到宝贝列表页的第2页或第3页，才会出现相关参数

# 通过分析
#   展现量 = 结束值-起始值 = 132 - 88 = 44
#   s：起始值 = page * 44
#   data-key：起始值 = s
#   data-value：结束值 = s + 44

finished_parse = ['_input_charset=utf-8', 'ie=utf8', 'imgfile=', 'initiative_id=staobaoz_20200202', 'js=2', 'q=%E5%A5%B3%E7%94%A8%E6%80%A7%E7%8E%A9%E5%85%B7', 'source=suggest', 'stats_click=search_radio_all%3A1', 'suggest=0_1', 'suggest_query=%E5%A5%B3%E7%94%A8', 'wq=%E5%A5%B3%E7%94%A8', '_ksTS=1580613373484_1162', 'bcoffset=4', 'callback=jsonp1163', 'data-key=s', 'data-value=132', 'ntoffset=4', 'p4ppushleft=1%2C48', 's=88']

finished_url = urlBase + '&'.join(finished_parse)
print(finished_url)

