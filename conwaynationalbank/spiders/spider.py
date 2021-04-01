import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import ConwaynationalbankItem
from itemloaders.processors import TakeFirst


class ConwaynationalbankSpider(scrapy.Spider):
	name = 'conwaynationalbank'
	start_urls = ['http://www.conwaynationalbank.com/news_events_au.cfm']

	def parse(self, response):
		post_links = response.xpath('//div[@class="content_home"]/child::node()').getall()
		description = []
		title = ''
		for el in post_links:
			tag = el[1:3]
			br = el[5:7]
			if tag == 'h3' and br != 'br':
				if len(description) > 2:
					description = [p.strip() for p in description]
					description = ' '.join(description).strip()
					item = ItemLoader(item=ConwaynationalbankItem(), response=response)
					item.default_output_processor = TakeFirst()
					item.add_value('title', title)
					item.add_value('description', description)
					yield item.load_item()
				title = remove_tags(el)
				description = []
			else:
				description.append(remove_tags(el))
