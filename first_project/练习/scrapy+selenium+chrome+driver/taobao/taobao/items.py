import scrapy

class TaobaoItem(scrapy.Item):
    picture = scrapy.Field()
    price = scrapy.Field()
    # salesVolume = scrapy.Field()
    # title = scrapy.Field()
    # shop = scrapy.Field()
    # address = scrapy.Field()

