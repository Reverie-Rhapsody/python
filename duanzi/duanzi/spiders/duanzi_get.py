import scrapy
from scrapy.loader import ItemLoader
from duanzi.items import DuanziItem

class DuanziSpider(scrapy.Spider):
	name = 'duanzi'
	star_turl = ['http://www.budejie.com/text/']
	#total_page = 1

	def parse(self, response):
		#lies = response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li')
		lies = response.css('div.j-r-list >ul >li')
		#filename = 'duanzi.txt'
		#l = ItemLoader(item = DuanziItem(), response = response)
		#with open (filename,'w') as file_object:
		for li in lies:
				#username = li.css('a.u-user-name::text').extract_first()
				#l.add_css('username', 'a.u-user-name::text')
				#file_object.write(username+'\n')
				#content = '\n'.join(li.css('div.j-r-list-c-desc a::text').extract())
				#l.add_css('content', 'div.j-r-list-c-desc a::text')
				#return l.load_item()
				#file_object.write(content+'\n')
				#yield DuanziItem(username = username, content = content)
				#if current_page < self.total_page:
				#yield scrapy.Request(self.start_urls[0]+f'{current_page+1}')