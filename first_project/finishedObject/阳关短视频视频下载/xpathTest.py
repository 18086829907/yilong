from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
tree = etree.parse("video.html", parser=parser)
videoSrc = tree.xpath('//div[@id="vs"]/video/@src')
print(videoSrc)