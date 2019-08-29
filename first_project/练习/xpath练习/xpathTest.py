# from lxml import etree
import re
# parser = etree.HTMLParser(encoding="utf8")
# tree = etree.parse("textinner.html", parser=parser)
# css = tree.xpath('//div[@id="J-detail-content"]//img/@src')
# css = str(css)
#


url = '''
.ssd-module-wrap{position:relative;margin:0 auto;width:750px;text-align:left;background-color:#fff}.ssd-module-wrap .ssd-module,.ssd-module-wrap .ssd-module-heading{width:750px;position:relative;overflow:hidden}.ssd-module-wrap .ssd-module{background-repeat:no-repeat;background-position:left top;background-size:100% 100%}.ssd-module-wrap .ssd-module-heading{background-repeat:no-repeat;background-position:left center;background-size:100% 100%}.ssd-module-wrap .ssd-module-heading .ssd-module-heading-layout{display:inline-block}.ssd-module-wrap .ssd-module-heading .ssd-widget-heading-ch{float:left;display:inline-block;margin:0 6px 0 15px;height:100%}.ssd-module-wrap .ssd-module-heading .ssd-widget-heading-en{float:left;display:inline-block;margin:0 15px 0 6px;height:100%}.ssd-module-wrap .ssd-widget-pic,.ssd-module-wrap .ssd-widget-text,.ssd-module-wrap .ssd-widget-line,.ssd-module-wrap .ssd-widget-rectangle,.ssd-module-wrap .ssd-widget-circle,.ssd-module-wrap .ssd-widget-triangle,.ssd-module-wrap .ssd-widget-table{position:absolute;overflow:hidden}.ssd-module-wrap .ssd-widget-rectangle{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.ssd-module-wrap .ssd-widget-table table{width:100%;height:100%}.ssd-module-wrap .ssd-widget-table td{position:relative;white-space:pre-line;word-break:break-all}.ssd-module-wrap .ssd-widget-pic img{display:block;width:100%;height:100%}.ssd-module-wrap .ssd-widget-text{line-height:1.5;word-break:break-all}.ssd-module-wrap .ssd-widget-text span{display:block;overflow:hidden;width:100%;height:100%;padding:0;margin:0;word-break:break-all;word-wrap:break-word;white-space:normal}.ssd-module-wrap .ssd-widget-link{position:absolute;left:0;top:0;width:100%;height:100%;background:transparent;z-index:100}.ssd-module-wrap .ssd-cell-text{position:absolute;top:0;left:0;right:0;width:100%;height:100%;overflow:auto}.ssd-module-wrap .M15578338281352{width:750px; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t29602/80/1248589892/305327/c70c9687/5cda8dbcN449e530c.jpg); height:765px}
.ssd-module-wrap .W15578338281352I0{z-index:6; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:420px; left:565px; width:178px; font-family:microsoft yahei; height:320px}
.ssd-module-wrap .W15578338281352I1{z-index:5; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:420px; left:379px; width:178px; font-family:microsoft yahei; height:320px}
.ssd-module-wrap .W15578338281352I2{z-index:4; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:420px; left:192px; width:178px; font-family:microsoft yahei; height:320px}
.ssd-module-wrap .W15578338281352I3{z-index:3; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:418px; left:-6px; width:191px; font-family:microsoft yahei; height:322px}
.ssd-module-wrap .W15578338281352I4{z-index:2; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:66px; left:504px; width:246px; font-family:microsoft yahei; height:344px}
.ssd-module-wrap .W15578338281352I5{z-index:1; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:66px; left:252px; width:246px; font-family:microsoft yahei; height:344px}
.ssd-module-wrap .W15578338281352I6{z-index:0; color:#000000; font-weight:normal; letter-spacing:0px; text-decoration:none; font-size:14px; line-height:1.5; font-style:normal; background-color:transparent; top:66px; left:9px; width:233px; font-family:microsoft yahei; height:344px}
.ssd-module-wrap .M15556370392061{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/30944/6/12987/298349/5cb922baE81d8ae6c/0591b4eebc369b9b.jpg); height:934px}
.ssd-module-wrap .M155563704533419{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/39240/5/268/267642/5cb922b9Ef8b54d92/ee9450832b97d702.jpg); height:1291px}
.ssd-module-wrap .M155563704497918{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/39235/34/222/231530/5cb922b8E6bf15cd6/ea64042c404409be.jpg); height:948px}
.ssd-module-wrap .M155563704470617{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/31574/19/13078/197611/5cb922b8E26743fa6/4748508c95ed2f5c.jpg); height:942px}
.ssd-module-wrap .M155563704449016{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/30348/21/13156/338187/5cb922baEd2d108dc/49d83e97ee3d03cb.jpg); height:948px}
.ssd-module-wrap .M155563704431215{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/38715/31/272/232434/5cb922b9E844b8e4a/f7ecd5055c5d3a75.jpg); height:586px}
.ssd-module-wrap .M155563704410414{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/34124/8/5763/472052/5cc004ecE5da4da38/fdebc4263977f03f.jpg); height:600px}
.ssd-module-wrap .M155563704394113{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/39833/17/272/338187/5cb922baE7e071641/d60e32400fc7b8e8.jpg); height:1135px}
.ssd-module-wrap .M155563704377012{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/34012/2/4979/194645/5cb922b5Ee6182937/45403ad3c768f60b.jpg); height:815px}
.ssd-module-wrap .M155563704360011{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/32753/4/13007/260583/5cb922b9E71550f33/73d401ea441f0c28.jpg); height:758px}
.ssd-module-wrap .M155563704340710{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/36021/14/3559/210090/5cb922b8Eb9c860b1/43f112c4634f29a0.jpg); height:640px}
.ssd-module-wrap .M15556370432239{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/39672/1/276/237986/5cb922b9Edc7bac94/5986df8c2db672f0.jpg); height:1403px}
.ssd-module-wrap .M15556370430498{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/32331/25/12855/357517/5cb922baEdd6b1534/b7d41e5b8b8178c4.jpg); height:1516px}
.ssd-module-wrap .M15556370426826{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/15464/12/15795/168498/5cb922b5E23b1da60/41c29d197d34b03a.jpg); height:731px}
.ssd-module-wrap .M15556370425155{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/34156/1/3572/277745/5cb922b9Ed74d608b/5c7385118ab0d4f2.jpg); height:836px}
.ssd-module-wrap .M15560186581191{width:750px; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/37415/7/4125/48350/5cbd58f8E72651d5d/7503aa9eccef4e43.png); height:134px}
.ssd-module-wrap .M155563724229520{width:750px; background-color:#e9e9e9; background-size:100% 100%; height:421px}
.ssd-module-wrap .W155563724229520I0{border-radius:0px; z-index:4; top:108px; left:562px; width:188px; height:313px}
.ssd-module-wrap .W155563724229520I1{border-radius:0px; z-index:3; top:108px; left:375px; width:187px; height:313px}
.ssd-module-wrap .W155563724229520I2{border-radius:0px; z-index:2; top:108px; left:188px; width:187px; height:313px}
.ssd-module-wrap .W155563724229520I3{border-radius:0px; z-index:1; top:108px; left:0px; width:188px; height:313px}
.ssd-module-wrap .W155563724229520I4{border-radius:0px; z-index:0; top:0px; left:0px; width:750px; height:108px}
.ssd-module-wrap .M15556376390021{width:750px; background-color:#b3b3b3; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/33047/39/5058/76720/5cb925a5E48216a88/2c9bf4baa89b3aa5.jpg); height:548px}
.ssd-module-wrap .M155563724243323{width:750px; background-color:#e9e9e9; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t1/82284/23/3123/479653/5d15a9e1E6cbd4076/671fcf722c7f53b4.jpg); height:1035px}
.ssd-module-wrap .M155563724247224{width:750px; background-color:#cbcbcb; background-size:100% 100%; background-image:url(//img30.360buyimg.com/sku/jfs/t8824/8/1925280907/32804/a1637b1a/59c0dddeN663ddb96.jpg); height:100px}
'''
# url = '.ssd-module-wrap{position:relative;margin:0 auto;width:750px;text-align:left;background-color:#fff}.ssd-module-wrap .ssd-module,.ssd-module-wrap .ssd-module-heading{width:750px;position:relative;overflow:hidden}.ssd-module-wrap .ssd-module{background-repeat:no-repeat;background-position:left top;background-size:100% 100%}.ssd-module-wrap .ssd-module-heading{background-repeat:no-repeat;background-position:left center;background-size:100% 100%}.ssd-module-wrap .ssd-module-heading .ssd-module-heading-layout{display:inline-block}.ssd-module-wrap .ssd-module-heading .ssd-widget-heading-ch{float:left;display:inline-block;margin:0 6px 0 15px;height:100%}.ssd-module-wrap .ssd-module-heading .ssd-widget-heading-en{float:left;display:inline-block;margin:0 15px 0 6px;height:100%}.ssd-module-wrap .ssd-widget-pic,.ssd-module-wrap .ssd-widget-text,.ssd-module-wrap .ssd-widget-line,.ssd-module-wrap .ssd-widget-rectangle,.ssd-module-wrap .ssd-widget-circle,.ssd-module-wrap .ssd-widget-triangle,.ssd-module-wrap .ssd-widget-table{position:absolute;overflow:hidden}.ssd-module-wrap .ssd-widget-rectangle{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.ssd-module-wrap .ssd-widget-table table{width:100%;height:100%}.ssd-module-wrap .ssd-widget-table td{position:relative;white-space:pre-line;word-break:break-all}.ssd-module-wrap .ssd-widget-pic img{display:block;width:100%;height:100%}.ssd-module-wrap .ssd-widget-text{line-height:1.5;word-break:break-all}.ssd-module-wrap .ssd-widget-text span{display:block;overflow:hidden;width:100%;height:100%;padding:0;margin:0;word-break:break-all;word-wrap:break-word;white-space:normal}.ssd-module-wrap .ssd-widget-link{position:absolute;left:0;top:0;width:100%;height:100%;background:transparent;z-index:100}.ssd-module-wrap .ssd-cell-text{position:absolute;top:0;left:0;right:0;width:100%;height:100%;overflow:auto}.ssd-module-wrap .M15514099345691{width:750px; background-color:#e9e9e9; background-size:100% 100%; height:400px}'
# url = '''
# //img30.360buyimg.com/sku/jfs/t1/8023/1/9854/445336/5c186cbbEe17531ab/f51186a676c03fab.jpg
# //img30.360buyimg.com/sku/jfs/t1/8023/1/9854/445336/5c186cbbEe17531ab/f51186a676c03fab.gif
# //img30.360buyimg.com/sku/jfs/t1/8023/1/9854/445336/5c186cbbEe17531ab/f51186a676c03fab.gifbuyimg.com/sku/jfs/t1/8023/1/9854/445336/5c186cbbEe17531ab/f51186a676c03fab.gif
# '''
pat = r'(//img.*?(jpg|gif|png))'
re_img = re.compile(pat, re.S)
imgList = re_img.findall(url)
# print(imgList)
imglis = []
for item in imgList:
    imglis.append(item[0])
print(imglis)


