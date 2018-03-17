import scrapy
from getimage.items import ImageItem

class ImageSpider(scrapy.Spider):
	name = 'Image'
	start_urls = ['http://www.meizitu.com/a/5501.html']

	def parse(self,response):
		yield ImageItem(image_urls = response.css('div#picture img::attr(src)').extract())