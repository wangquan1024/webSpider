# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        post_data = dict(
            # 填写账号
            login="",
            # 填写密码
            password="",
            authenticity_token=authenticity_token,
            utf8=utf8,
            commit=commit
        )
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        if response.url == "https://github.com/":
            print('登陆成功')
        else:
            print('登陆失败')
