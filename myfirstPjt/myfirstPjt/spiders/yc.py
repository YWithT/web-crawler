# -*- coding: utf-8 -*-
import scrapy
from myfirstPjt.items import MyfirstpjtItem


class YcSpider(scrapy.Spider):
    # 爬虫名
    name = "yc"
    # 允许的域名
    allowed_domains = ["sina.com.cn"]
    # 起始网址
    start_urls = ['http://www.sina.com.cn/']

    # def __init__(self, myurl=None, *args, **kwargs):
    #     super(YcSpider, self).__init__(*args, **kwargs)
    #     # 输出要爬的网址，对应值为接收到的参数
    #     print("要爬取的网址为：%s" % myurl)
    #     self.start_urls = ["%s" % myurl]

    def parse(self, response):
        item = MyfirstpjtItem()
        item["title"] = response.xpath("/html/head/title/text()")
        print(item["title"])
