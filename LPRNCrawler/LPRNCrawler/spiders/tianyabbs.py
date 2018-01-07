#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

import scrapy

import sys
sys.path.append('/home/linhanqiu/LovePet-RealizeNotion/LPRNCrawler/LPRNCrawler')

from scrapy.contrib.loader import ItemLoader
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import CpsecspidersItem
import scrapy
import lxml.html as lh
import sys
import time
import os
from urllib.parse import  urljoin
from scrapy.contrib.spiders import CrawlSpider, Rule
from xml.dom.minidom import parse
import xml.dom.minidom


class tianyaBBSspider(CrawlSpider):

    # 爬虫名称，非常关键，唯一标示
    name = "tianya"

    # 域名限定
    allowed_domains = ["bbs.tianya.cn"]

    # 爬虫的爬取得起始url
    start_urls = [

        # 天涯论坛热帖榜  可以写多个用，分隔

        "http://bbs.tianya.cn/list.jsp?item=75&sub=2",

    ]
    baseurl = 'http://bbs.tianya.cn'

    def parse(self, response):
        # 选择器
        sel = Selector(response)
        item = CpsecspidersItem()
        # 文章url列表
        article_url = sel.xpath(
            '//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[1]/a/@href').extract()
        # 下一页地址
        next_page_url = sel.xpath("//div[@class='short-pages-2 clearfix']/div[@class='links']/a[last()]/@href").extract()

        for url in article_url:
            # 拼接url
            urll = urljoin(self.baseurl, url)
            # 调用parse_item解析文章内容
            request = scrapy.Request(urll, callback=self.parse_item)
            request.meta['item'] = item
            yield request

        if next_page_url[0]:
            # 调用自身进行迭代
            request = scrapy.Request(urljoin(self.baseurl, next_page_url[0]), callback=self.parse)
            yield request

    def parse_item(self, response):

        content = ''
        sel = Selector(response)
        item = response.meta['item']
        l = ItemLoader(item=CpsecspidersItem(), response=response)

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="post_head"]/h1/span/span/text()').extract()
        article_content = sel.xpath(
            '//div[@class="atl-main"]//div/div[@class="atl-content"]/div[2]/div[1]/text()').extract()
        article_author = sel.xpath('//span[@class="s_title"]/span/text()').extract()
        article_clik_num = sel.xpath('substring-after(//div[@class="atl-info"]/span[3]/text(),"：")').extract()
        article_reply_num = sel.xpath('substring-after(//div[@class="atl-info"]/span[4]/text(),"：")').extract()

        # 文章内容拼起来
        for i in article_content:
            content = content + i

        article_name = article_name
        content = content
        article_url = article_url
        article_author = article_author[0]
        click_num = article_clik_num[0]
        reply_num = article_reply_num[0]

        l.add_value('article_name', article_name)
        l.add_value('article_content', content)
        l.add_value('article_url', article_url)
        l.add_value('reply_num', reply_num)
        l.add_value('click_num', click_num)
        l.add_value('article_author', article_author)

        yield l.load_item()