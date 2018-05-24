# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['www.taobao.com/']
    start_urls = ['https://zhidao.baidu.com/question/473852248.html']

    def parse(self, response):
	    fname=response.url.split('/')[-1]
	    with open(fname,'wb') as f:
		    f.write(response.body)
	    self.log("Saved file %s." % fname)
		

