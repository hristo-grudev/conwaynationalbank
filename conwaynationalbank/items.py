import scrapy


class ConwaynationalbankItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
