# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time

# 让selenium负责处理下载部分，这样可以处理ajax获得的数据
class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            # 如果有点击就继续点击，直到没有就退出
            while True:
                showMore = self.driver.find_element_by_class_name("show-more")
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass
        source = self.driver.page_source
        # 返回response让引擎接收
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
        return response 