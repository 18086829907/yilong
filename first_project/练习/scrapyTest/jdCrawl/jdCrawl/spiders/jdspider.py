# -*- coding: utf-8 -*-
import scrapy
from jdCrawl.items import JdcrawlItem
from scrapy_splash import SplashRequest
import re
import random

script = """
function main(splash, args)
    splash.images_enabled = True   
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    splash.scroll_position={y=10000}
    assert(splash:wait(args.wait))
    return splash:html()
end
"""

class JdspiderSpider(scrapy.Spider):
    name = 'jdSpider'
    allowed_domains = ['jd.com']
    start_urls = [
        'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_71227&page=2&sort=sort_rank_asc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E4%B8%8A%E8%87%82%E5%BC%8F#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_71226&page=1&sort=sort_rank_asc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E6%89%8B%E8%85%95%E5%BC%8F#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_119532&page=1&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9197,12189&ev=1107_33710&page=1&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9197,12187&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=7#J_main',
        'https://list.jd.com/list.html?cat=9192,9197,12588&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=9#J_main',
        'https://list.jd.com/list.html?cat=9192,9197,12587&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=10#J_main',
        'https://search.jd.com/Search?keyword=%E5%88%B6%E6%B0%A7%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=1&wq=z&page=1&s=159&click=0',
        'https://search.jd.com/Search?keyword=%E5%91%BC%E5%90%B8%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=huxi&page=1&s=57&click=0',
        'https://list.jd.com/list.html?cat=9192,9197,12593&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=7#J_main',
        'https://search.jd.com/Search?keyword=%E6%B4%97%E9%BC%BB%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=x&page=1&s=54&click=0',
        'https://search.jd.com/Search?keyword=%E6%B4%97%E9%BC%BB%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=x&page=1&s=54&click=0',
        'https://search.jd.com/Search?keyword=%E4%B8%AD%E9%A2%91%E6%B2%BB%E7%96%97%E4%BB%AA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B8%AD%E9%A2%91zhi&page=1&s=53&click=0',
        'https://search.jd.com/Search?keyword=%E8%89%BE%E7%81%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=ai&page=1&s=55&click=0',
        'https://search.jd.com/Search?keyword=%E6%8B%94%E7%BD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=ba&page=1&s=57&click=0',
        'https://search.jd.com/Search?keyword=%E5%88%AE%E7%97%A7%E6%9D%BF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=guasha&page=1&s=55&click=0',
        'https://search.jd.com/Search?keyword=%E6%89%8B%E5%8A%A8%E8%BD%AE%E6%A4%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=s&page=1&s=56&click=0',
        'https://search.jd.com/Search?keyword=电动轮椅&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=电动lu&page=1&s=58&click=0',
        'https://list.jd.com/list.html?cat=9192,9197,12596&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=8#J_main',
        'https://search.jd.com/Search?keyword=护理床&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=hlihc&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=爬楼机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=pal&page=1&s=59&click=0',
        'https://search.jd.com/Search?keyword=助听器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=zhuti&page=1&s=59&click=0',
        'https://list.jd.com/list.html?cat=9192,12632,12634&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,13240&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12642&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12646&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?tid=1006319&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12635&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12637&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12638&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12640&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12636&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12641&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12633&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397%5F82294&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?tid=1001205&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12643&ev=3397%5F82262&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397_79362&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12634&ev=3397%5F82290&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79370&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F37790&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79374&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F82286&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,12644&ev=3397%5F79371&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,12632,13241&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=%E8%B6%85%E8%96%84%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%B6%85%E8%96%84%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page=1&s=59&click=0',
        'https://search.jd.com/Search?keyword=%E6%8C%81%E4%B9%85%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8C%81%E4%B9%85%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page=1&s=60&click=0',
        'https://search.jd.com/Search?keyword=%E7%B4%A7%E5%9E%8B%E9%81%BF%E5%AD%95%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%B4%A7%E5%9E%8B%E9%81%BF%E5%AD%95%E5%A5%97&stock=1&page=1&s=59&click=0',
        'https://search.jd.com/Search?keyword=%E9%AA%8C%E5%AD%95%E8%AF%95%E7%BA%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%AA%8C%E5%AD%95%E8%AF%95%E7%BA%B8&page=1&s=57&click=0',
        'https://search.jd.com/Search?keyword=%E9%AA%8C%E5%AD%95%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%AA%8C%E5%AD%95%E6%A3%92&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=%E6%8E%92%E5%8D%B5%E8%AF%95%E7%BA%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8E%92%E5%8D%B5%E8%AF%95%E7%BA%B8&page=1&s=59&click=0',
        'https://search.jd.com/Search?keyword=%E7%83%AD%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%83%AD%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&page=1&s=55&click=0',
        'https://search.jd.com/Search?keyword=%E5%86%B0%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%B0%E6%84%9F%E6%B6%A6%E6%BB%91%E6%B6%B2&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E6%9E%9C%E9%A6%99%E6%B6%A6%E6%BB%91%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%B6%A6%E6%BB%91%E6%B6%B2&page=1&s=60&click=0',
        'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6%E5%96%B7%E5%89%82&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page=1&s=56&click=0',
        'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6%E6%B9%BF%E5%B7%BE&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%BB%B6%E6%97%B6&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%BB%B6%E6%97%B6&page=1&s=51&click=0',
        'https://search.jd.com/Search?keyword=%E9%9C%87%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9C%87%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E6%89%8B%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E5%8A%A8%E9%A3%9E%E6%9C%BA%E6%9D%AF&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E9%98%B4%E8%87%80%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%80%92%E6%A8%A1&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E8%83%B8%E9%83%A8%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E9%83%A8&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%8D%8A%E8%BA%AB%E5%80%92%E6%A8%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%8D%8A%E8%BA%AB%E5%80%92%E6%A8%A1&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%AE%9E%E4%BD%93%E5%A8%83%E5%A8%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%AE%9E%E4%BD%93%E5%A8%83%E5%A8%83&page=1&s=61&click=0',
        'https://list.jd.com/list.html?cat=9192,9196,14697&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7%E6%8A%BD%E6%8F%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=3.def.0.T19&wq=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BB%BF%E7%9C%9F%E9%98%B3%E5%85%B7&page=1&s=61&click=0',
        'https://list.jd.com/list.html?cat=9192,9196,14701&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9196,12610&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=AV%E6%8C%AF%E5%8A%A8%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=AV&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E8%BD%AC%E7%8F%A0%E6%A3%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%BD%AC%E7%8F%A0%E6%A3%92&page=1&s=61&click=0',
        'https://list.jd.com/list.html?cat=9192,9196,14700&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=%E7%BC%A9%E9%98%B4%E7%90%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%A5%97%E8%A3%85%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A5%97%E8%A3%85%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E7%9D%A1%E8%A3%99%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%9D%A1%E8%A3%99%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&page=1&s=53&click=0',
        'https://search.jd.com/Search?keyword=%E4%B8%81%E5%AD%97%E8%A3%A4%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1&s=51&click=0',
        'https://search.jd.com/Search?keyword=%E9%94%81%E7%B2%BE%E7%8E%AF&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%94%81%E7%B2%BE%E7%8E%AF&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E5%90%8E%E5%BA%AD&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%90%8E%E5%BA%AD&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%94%A8%E5%93%81SM&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%88%90%E4%BA%BA%E7%94%A8%E5%93%81SM&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E8%9B%8B%E7%99%BD%E7%B2%89&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=%E7%BB%B4%E7%94%9F%E7%B4%A0&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%BB%B4%E7%94%9F%E7%B4%A0&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=%E8%9E%BA%E6%97%8B%E8%97%BB&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%9E%BA%E6%97%8B%E8%97%BB&page=3&s=60&click=0',
        'https://search.jd.com/Search?keyword=%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=gai&stock=1&page=1&s=57&click=0',
        'https://search.jd.com/Search?keyword=%E6%B0%A8%E7%B3%96&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&stock=1&page=1&s=59&click=0',
        'https://search.jd.com/Search?keyword=%E5%84%BF%E7%AB%A5%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&stock=1&page=1&s=56&click=0',
        'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97259&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97260&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,12163&ev=6684%5F97261&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6121&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6118&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9200&ev=4874%5F6142&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9207&ev=4874%5F8136&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/search?keyword=%E6%B6%A6%E8%82%A0%E9%80%9A%E4%BE%BF&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&cid2=9193&cid3=9207&page=1&s=106&click=0',
        'https://search.jd.com/search?keyword=%E5%85%BB%E8%83%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%85%BB%E8%83%83&cid2=9193&cid3=9207&page=1&s=56&click=0',
        'https://list.jd.com/list.html?cat=9192,9194,12171&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=2#J_main',
        'https://search.jd.com/search?keyword=%E5%AD%95%E5%A6%87%E9%92%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%AD%95%E5%A6%87%E9%92%99&cid2=9194&page=1&s=61&click=0',
        'https://search.jd.com/Search?keyword=%E9%94%8C%E7%A1%92%E5%AE%9D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%94%8C%E7%A1%92%E5%AE%9D&stock=1&page=1&s=53&click=0',
        'https://list.jd.com/list.html?cat=9192,9193,9205&ev=4874%5F85734&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9205&ev=4874%5F20494&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,9205&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F8264&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F85618&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9193,12162&ev=4874%5F85619&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/search?keyword=%E6%B6%A6%E5%96%89%E7%B3%96&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%B6%A6%E5%96%89%E7%B3%96&cid2=9193&cid3=12170&stock=1&page=1&s=52&click=0',
        'https://list.jd.com/list.html?cat=9192,9193,12170&ev=exbrand%5F9476&sort=sort_totalsales15_desc&trans=1&JL=2_1_0#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9193,12170&ev=exbrand%5F121636&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,12180&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=%E7%87%95%E7%9B%8F&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%87%95%E7%9B%8F&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=%E5%8D%B3%E9%A3%9F%E7%87%95%E7%AA%9D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&wtype=1&page=1&s=58&click=1',
        'https://list.jd.com/list.html?cat=9192,9195,9229&ev=2314_85552&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,9229&ev=2314%5F85553&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F8396&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F6136&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F71115&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,9230&ev=1107%5F85650&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107%5F85672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107_85675&sort=sort_totalsales15_desc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E5%86%B3%E6%98%8E%E5%AD%90#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9195,12185&ev=1107_82704&sort=sort_totalsales15_desc&trans=1&JL=3_%E5%88%86%E7%B1%BB_%E8%83%96%E5%A4%A7%E6%B5%B7#J_crumbsBar',
        'https://list.jd.com/list.html?cat=9192,9195,12613&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://list.jd.com/list.html?cat=9192,9195,12186&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main',
        'https://search.jd.com/Search?keyword=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&page=1&s=55&click=0',
        'https://search.jd.com/Search?keyword=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C%20%E7%BE%8E%E7%9E%B3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C%20%E7%BE%8E%E7%9E%B3&page=1&s=54&click=0',
        'https://search.jd.com/Search?keyword=%E6%8A%A4%E7%90%86%E6%B6%B2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%8A%A4%E7%90%86%E6%B6%B2&page=1&s=56&click=0',
        'https://search.jd.com/Search?keyword=%E4%BC%B4%E4%BE%A3%E7%9B%92&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BC%B4%E4%BE%A3%E7%9B%92&page=1&s=58&click=0',
        'https://search.jd.com/Search?keyword=%E4%BD%93%E6%A3%80%E5%8D%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BD%93%E6%A3%80%E5%8D%A1&page=3&s=57&click=0'
    ]

    def start_request(self):
        for start_url in self.start_urls:
            yield SplashRequest(start_url, dont_filter=True, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': random.randint(1,10)})
    def parse(self, response):
        liList = response.xpath('//ul[contains(@class, "gl-warp")]/li')
        for li in liList:
            item = JdcrawlItem()
            item['type_1'] = response.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[1]/a/text()').extract_first()
            item['type_2'] = response.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[2]//span/text()').extract_first()
            item['type_3'] = response.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[3]//span/text()').extract_first()
            item['type_4'] = response.xpath('//div[@id="J_crumbsBar"]/div/div/div/div[4]//em/text()').extract_first()
            try:
                item['type_search'] = response.xpath('//div[@id="J_crumbsBar"]/div/div/div[2]/strong/text()').extract_first().strip('"')
            except AttributeError:
                item['type_search'] = None
            # 商品图片
            item['sptp'] = 'https:' + li.xpath('./div/div[contains(@class,"p-img")]/a/img/@src|./div/div[contains(@class,"p-img")]/a/img/@data-lazy-img').extract_first()
            # 评论数量
            try:
                item['plsl'] = str(float(
                    li.xpath('./div/div[contains(@class,"p-commit")]/strong/a/text()').extract_first().strip('\n+').split('万')[0]) * 10000)
            except (IndexError, AttributeError) as e:
                try:
                    item['plsl'] = li.xpath('./div/div[contains(@class,"p-commit")]/strong/a/text()').extract_first().strip('\n+')
                except AttributeError as e:
                    item['plsl'] = None
            # 店铺名称
            item['dpmc'] = li.xpath('./div/div[contains(@class,"p-shop")]/span/a/@title').extract_first()
            # 商品图标
            item['sptb'] = li.xpath('./div/div[contains(@class,"p-icons")]/descendant::i/text()').extract_first()
            # 访问每个商品的详情页
            item['innerUrl'] = 'https:' + li.xpath('./div/div[1]/a/@href').extract_first()
            # 发送请求
            yield SplashRequest(item['innerUrl'], dont_filter=True, callback=self.parse_inner, endpoint='execute', meta={'item': item.copy()}, args={'lua_source': script, 'wait': random.randint(1,10)})
        next_url = response.xpath('//a[contains(text(),"下一页")]/@href').extract_first()
        if not next_url:
            return
        else:
            base_url = 'https://list.jd.com'
            yield SplashRequest(base_url + next_url, dont_filter=True, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': random.randint(1,10)})

    def parse_inner(self, response):
        item = response.meta.get('item')
        item['pinpai'] = response.xpath('//ul[@id="parameter-brand"]/li/a/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "品牌")]/a/text()').extract_first()  # 品牌
        item['spmc'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品名称")]/text()').extract() if '：' in x]
        item['spbh'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品编号")]/text()').extract() if '：' in x]
        item['huohao'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "货号")]/text()').extract() if '：' in x]
        item['dianpu'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "店铺")]/text()').extract() if '：' in x]
        item['spmz'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品毛重")]/text()').extract() if '：' in x]
        item['spcd'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "商品产地")]/text()').extract() if '：' in x]
        item['gcjk'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "国产/进口")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "国别")]/text()').extract()if '：' in x]
        item['dianyuan'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "电源：")]/text()').extract() if '：' in x]
        item['fenlei'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "分类")]/text()').extract() if '：' in x]
        item['leibie'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "类别")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "药品类别")]/text()').extract()if '：' in x]
        item['tese'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "特色")]/text()').extract() if '：' in x]
        item['texing'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "特性")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "特点")]/text()').extract()if '：' in x]
        item['jiawei'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "价位")]/text()').extract() if '：' in x]
        item['guige'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "规格")]/text()|//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"规格")]/following-sibling::td/text()').extract()if '：' in x]
        item['chicun'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "尺寸")]/text()').extract() if '：' in x]
        item['yuanliao'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "原料")]/text()').extract() if '：' in x]
        item['shuliang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "数量")]/text()').extract() if '：' in x]
        item['yongtu'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "用途")]/text()').extract() if '：' in x]
        item['xingzhi'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "性质")]/text()').extract() if '：' in x]
        item['chima'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "尺码")]/text()').extract() if '：' in x]
        item['qunchang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "裙长")]/text()').extract() if '：' in x]
        item['mianliao'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "面料")]/text()').extract() if '：' in x]
        item['houdu'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "厚度")]/text()').extract() if '：' in x]
        item['lingxiang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "领型")]/text()').extract() if '：' in x]
        item['lxys'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "流行元素")]/text()').extract() if '：' in x]
        item['syjj'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用季节")]/text()').extract() if '：' in x]
        item['sfyd'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "是否有兜")]/text()').extract() if '：' in x]
        item['sycj'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用场景")]/text()').extract() if '：' in x]
        item['syrq'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用人群")]/text()').extract() if '：' in x]
        item['fzs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "分子筛")]/text()').extract() if '：' in x]
        item['dmfs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "调码方式")]/text()').extract() if '：' in x]
        item['jygn'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "记忆功能")]/text()').extract() if '：' in x]
        item['clbw'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "测量部位")]/text()').extract() if '：' in x]
        item['znbj'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "智能警报")]/text()').extract() if '：' in x]
        item['cdfs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "充电方式")]/text()').extract() if '：' in x]
        item['ylfw'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "压力范围")]/text()').extract() if '：' in x]
        item['gzms'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "工作模式")]/text()').extract() if '：' in x]
        item['ylms'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "压力模式")]/text()').extract() if '：' in x]
        item['zhongliang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "重量")]/text()').extract() if '：' in x]
        item['sybw'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用部位")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "部位")]/text()').extract()if '：' in x]
        item['dyfs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "电源方式")]/text()').extract() if '：' in x]
        item['syzt'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用症状")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "症状")]/text()').extract()if '：' in x]
        item['baozhuang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "包装")]/text()|//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"包装")]/following-sibling::td/text()').extract()if '：' in x]
        item['lmbs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "蓝帽标识")]/text()').extract() if '：' in x]
        item['kuanshi'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "款式：")]/text()').extract() if '：' in x]
        item['sfkwc'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "是否可外穿")]/text()').extract() if '：' in x]
        item['xingtai'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "形态")]/text()').extract() if '：' in x]
        item['xingzhuang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "形状")]/text()').extract() if '：' in x]
        item['syfs'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用方式")]/text()').extract() if '：' in x]
        item['fengge'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "风格")]/text()').extract() if '：' in x]
        item['caizhi'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "材质")]/text()').extract() if '：' in x]
        item['xiuchang'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "袖长")]/text()').extract() if '：' in x]
        item['sydx'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用对象")]/text()').extract() if '：' in x]
        item['xgrd'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "选购热点")]/text()').extract() if '：' in x]
        item['sylx'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "适用类型")]/text()').extract() if '：' in x]
        item['ypjx'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "药品剂型")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "剂型")]/text()|//ul[contains(@class, "parameter2")]/li[contains(text(), "产品类型")]/text()').extract()if '：' in x]
        item['syff'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "使用方法")]/text()').extract() if '：' in x]
        item['zycf'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "成份") or contains(text(), "成分")]/text()').extract()if '：' in x]
        item['gongxiao'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "功效")]/text()').extract() if '：' in x]
        item['gongneng'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "功能")]/text()').extract() if '：' in x]
        item['kzlx'] = [x.split('：')[-1] for x in response.xpath('//ul[contains(@class, "parameter2")]/li[contains(text(), "控制类型")]/text()').extract() if '：' in x]
        item['spsp'] = response.xpath('//video/@src').extract_first()
        item['ylqxzczbh'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "医疗器械注册证编号或者备案凭证编号")]/../dd/text()').extract_first()
        item['ylqxmc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "医疗器械名称")]/../dd/text()').extract_first()
        item['xinghao'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "型号")]/../dd/text()').extract_first()
        item['zcrhzbarxx'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "注册人或者备案人信息")]/../dd/text()').extract_first()
        item['scqy'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "生产企业")]/../dd/text()').extract_first()
        item['scxkzhbapzbh'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "生产许可证或者备案凭证编号")]/../dd/text()').extract_first()
        item['gxyjs'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "高血压警示")]/../dd/text()').extract_first()
        item['yybb'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "语音播报")]/../dd/text()').extract_first()
        item['jyfs'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "加压方式")]/../dd/text()').extract_first()
        item['jygnc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "记忆功能（次）")]/../dd/text()').extract_first()
        item['clfw'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量范围")]/../dd/text()').extract_first()
        item['sfzdgb'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "是否自动关闭")]/../dd/text()').extract_first()
        item['clff'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量方法")]/../dd/text()').extract_first()
        item['clsj'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量时间")]/../dd/text()').extract_first()
        item['cljd'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "测量精度")]/../dd/text()').extract_first()
        item['cpcc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品尺寸（cm）")]/../dd/text()').extract_first()
        item['xsfs'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "显示方式")]/../dd/text()').extract_first()
        item['jgjzc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "结构及组成")]/../dd/text()').extract_first()
        item['syfw'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "适用范围")]/../dd/text()').extract_first()
        item['tqms'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "通气模式")]/../dd/text()').extract_first()
        item['yqnd'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "氧气浓度")]/../dd/text()').extract_first()
        item['yqll'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "氧气流量")]/../dd/text()').extract_first()
        item['gonglv'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "功率")]/../dd/text()').extract_first()
        item['whklsfkt'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化颗粒是否可调")]/../dd/text()').extract_first()
        item['whlsfkt'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化量是否可调")]/../dd/text()').extract_first()
        item['jjz'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "禁忌症")]/../dd/text()').extract_first()
        item['zctj'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "贮藏条件")]/../dd/text()').extract_first()
        item['ysjsm'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "压缩机寿命")]/../dd/text()').extract_first()
        item['whkldxfb'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "雾化粒大小分布")]/../dd/text()').extract_first()
        item['rongliang'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "容量")]/../dd/text()').extract_first()
        item['gdgzms'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "工作模式")]/../dd/text()').extract_first()
        item['zlbcc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "治疗板尺寸")]/../dd/text()').extract_first()
        item['cpjz'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品净重（kg）")]/../dd/text()').extract_first()
        item['zdzz'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最大载重（kg）")]/../dd/text()').extract_first()
        item['zuokuan'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "座宽（cm）")]/../dd/text()').extract_first()
        item['zdh'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "折叠后长*宽*高（cm）")]/../dd/text()').extract_first()
        item['lcc'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "前/后轮尺寸（cm）")]/../dd/text()').extract_first()
        item['ltlx'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "轮胎类型")]/../dd/text()').extract_first()
        item['zxzwbj'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最小转弯半径（cm）")]/../dd/text()').extract_first()
        item['ppds'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "爬坡度数（°）")]/../dd/text()').extract_first()
        item['dclx'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "电池类型")]/../dd/text()').extract_first()
        item['dcrl'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "电池容量（AH）")]/../dd/text()').extract_first()
        item['llcdsj'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "理论充电时间（H）")]/../dd/text()').extract_first()
        item['zdsl'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "最大速率（KM/H）")]/../dd/text()').extract_first()
        item['edxh'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "额定续航（KM）")]/../dd/text()').extract_first()
        item['ypspm'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "药品商品名")]/../dd/text()').extract_first()
        item['yptym'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "药品通用名")]/../dd/text()').extract_first()
        item['pzwh'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "批准文号")]/../dd/text()').extract_first()
        item['cpgg'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "产品规格")]/../dd/text()').extract_first()
        item['yfyl'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "用法用量")]/../dd/text()').extract_first()
        item['yxq'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "有效期")]/../dd/text()').extract_first()
        item['syzgnzz'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "适用症/功能主治")]/../dd/text()').extract_first()
        item['bzgg'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "包装规格")]/../dd/text()').extract_first()
        item['knsfaphgl'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "库内是否按批号管理")]/../dd/text()').extract_first()
        item['knsfagysgl'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "库内是否按供应商管理")]/../dd/text()').extract_first()
        item['blfy'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "不良反应")]/../dd/text()').extract_first()
        item['bzq'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "保质期")]/../dd/text()|//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"保质期")]/following-sibling::td/text()').extract_first()
        item['gongyong'] = response.xpath('//div[@class="Ptable-item"]/dl/dl[*]//dt[contains(text(), "功用")]/../dd/text()').extract_first()
        item['synl'] = response.xpath('//*[@id="specifications"]/table/tbody/tr/td[contains(text(),"适用年龄")]/following-sibling::td/text()').extract_first()
        # 商品详情图片
        try:
            spxqtp1 = response.xpath('//div[@id="J-detail-content"]/style/text()').extract_first()
            pat = r'(//img.*?(jpg|gif|png))'
            re_img = re.compile(pat, re.S)
            spxqtp1List = re_img.findall(spxqtp1)  # 商品详情图片列表
            spxqtp1Url = [re.sub('https:https:', 'https:', i) for i in ['https:' + x[0] for x in spxqtp1List]]
            spxqtp2Url = []
        except TypeError:
            spxqtp1Url = []
            spxqtp2Url = [re.sub('https:https:', 'https:', i) for i in ['https:' + x for x in response.xpath('//div[@id="J-detail-content"]//img/@src').extract()]]
        item['spxqtp'] = []
        item['spxqtp'].extend(spxqtp1Url)
        item['spxqtp'].extend(spxqtp2Url)
        yield item