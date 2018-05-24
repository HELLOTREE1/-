# -*- coding: utf-8 -*-
# -*-coding:utf-8-*-
#获得股票列表：东方财富网http://quote.eastmoney.com/stocklist.html
#获取个股信息：百度股票https://gupiao.baidu.com/stock/
#            个股https://gupiao.baidu.com/stock/sz002439.html
import scrapy
import re
# import urllib2
import random

class StocksSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ['http://quote.eastmoney.com/stocklist.html']
    custom_settings = {'DOWNLOAD_DELAY': 0.2, 'CONCURRENT_REQUESTS_PER_IP': 4, 'DOWNLOADER_MIDDLEWARES': {}, }
    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + \
                     re.findall('\>.*\<', name)[0][1:-1]})
        yield infoDict


