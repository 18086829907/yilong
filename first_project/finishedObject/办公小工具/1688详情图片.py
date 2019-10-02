import re
import urllib.request
import urllib.parse
import os
import time
# p = '<p><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/796/356/11483653697_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/746/056/11514650647_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/062/177/11448771260_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/459/446/11483644954_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/880/176/11483671088_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/237/446/11514644732_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/752/776/11514677257_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/575/356/11514653575_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/115/956/11514659511_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/336/656/11514656633_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/830/296/11514692038_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/331/086/11483680133_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/343/476/11514674343_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/244/867/11448768442_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/388/746/11514647883_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/564/567/11448765465_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/715/957/11448759517_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/642/686/11514686246_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;" data-spm-anchor-id="a261y.7663282.descBanner.i0.5920774dLk6ujH"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/237/956/11483659732_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/612/386/11483683216_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br></p>'
p = '<p><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/299/846/12215648992_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/138/642/12144246831_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="https://cbu01.alicdn.com/img/ibank/2019/366/714/12181417663_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px; zoom: 1;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/264/852/12144258462_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/557/804/12181408755_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/407/456/12215654704_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/398/204/12181402893_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/843/324/12181423348_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/125/162/12144261521_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/631/624/12181426136_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/521/486/12215684125_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/315/462/12144264513_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/599/246/12215642995_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/117/114/12181411711_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/418/156/12215651814_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/676/756/12215657676_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/604/876/12215678406_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/984/276/12215672489_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/640/924/12181429046_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br><img alt="undefined" src="//cbu01.alicdn.com/cms/upload/2011/821/721/127128_1301427272.png" data-lazyload-src="//cbu01.alicdn.com/img/ibank/2019/794/666/12215666497_2104162502.jpg" max-width="990" style="visibility: visible; max-width: 990px;"><br><br></p>'
pat = 'src="(.*?)"'
obj = re.compile(pat)
result = obj.findall(p)
n = 0
for res in result:
    # dirname = r'G:\PS\酷派新衣\1购物\2详情页\产品详情图'+'\童装女童春秋款工装裤套装2019新款秋季个性字母印花工装裤两件套'
    dirname = r'G:\PS\酷派新衣\1购物\2详情页\产品详情图'+'\男童女童秋冬款皮毛一体外套2019新款洋气韩版宽松毛毛绒衣中大童'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    # 图片的名字叫啥
    filename = str(n) + '.' + res.split('/')[-1].split('.')[-1]
    filepath = os.path.join(dirname, filename)
    n += 1
    if not 'https:' in res:
        res = 'https:' + res
    if not 'png' in res:
        print('%s图片正在下载...' % filename)
        urllib.request.urlretrieve(res, filepath)
        print('%s图片下载结束...' % filename)
        time.sleep(1)
