# -*- coding: utf-8 -*-
import scrapy,re
from sfw_spider.items import NewhouseSpiderItem,EsfSpiderItem

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            # not(@class)排除有class的
            td = tr.xpath(".//td[not(@class)]")
            province_text = td[0].xpath(".//text()").get()
            if province_text == '其它':
                continue
            province_text = re.sub(r'\s','',province_text)
            if province_text:
                province =  province_text
            city_links = td[1].xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建新房的url
                url_module = city_url.split("//")
                scheme = url_module[0]
                domain = url_module[1]
                if 'bj' in domain:
                #     # newHouse_url = 'https://newhouse.fang.com/house/s/'
                #     # esf_url = 'https://esf.fang.com/'
                    continue
                else:
                    newHouse_url = scheme + '//' + 'newhouse.' + domain + 'house/s/'
                # 构建二手房的url
                    esf_url =  scheme + '//' + 'esf.' + domain
                print(esf_url)
                # meta是一个字典，它的主要作用是用来传递数据的，meta = {‘key1’:value1}，如果想在下一个函数中取出value1, 只需得到上一个函数的meta[‘key1’]即可，
                # 因为meta是随着Request产生时传递的，下一个函数得到的Response对象中就会有meta，即response.meta. 
                # yield scrapy.Request(url=newHouse_url,callback=self.parse_newhouse,meta={"info":(province,city)})
            
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={"info":(province,city)})
                break
            break
    
    def parse_newhouse(self,response):
        province,city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            div = li.xpath(".//div[@class='clearfix']/h3")
            # 将广告过滤掉
            if div:
                continue
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip() 
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            rooms = list(filter(lambda x:x.endswith('居'),house_type_list))
            area = li.xpath(".//div[contains(@class,'house_type')]/text()").getall()
            area = re.sub(r'\s|－','',area[-1])
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = li.xpath(".//div[@class='address']//span[@class='sngrey']//text()").get()
            if not district_text:
                district = ''
            else:
                district_text = district_text.strip()
                district = re.search(r'\[(.+)\]',district_text).group(1)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r'\s|广告',"",price)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            origin_url = 'https:'+ origin_url
            item = NewhouseSpiderItem(province=province,city=city,name=name,price=price,
            rooms=rooms,address=address,district=district,sale=sale,origin_url=origin_url)
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            # 要去掉过滤
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url,callback=self.parse_newhouse,meta={"info":(province,city)},dont_filter=True)
            
    def parse_esf(self,response):
        province,city = response.meta.get('info')
        dls = response.xpath("//div[contains(@class,'shop_list')]//dl")
        for dl in dls:
            div = dl.xpath(".//div[@class='clearfix']/h3")
            if div:
                continue
            item = EsfSpiderItem(province=province,city=city)
            name = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            item['name'] = name
            infos = dl.xpath(".//p[@class='tel_shop']//text()").getall()
            infos = list(map(lambda x:re.sub(r'\s|\|',"",x),infos))
            for info in infos:
                if '厅' in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '㎡' in info:
                    item['area'] = info
                elif '年' in info:
                    item['year'] = info
            item['address'] = dl.xpath(".//p[@class='add_shop']//span/text()").get()
            item['unit'] = dl.xpath(".//dd[@class='price_right']//span[last()]/text()").get()
            price_number = dl.xpath(".//dd[@class='price_right']//span/b/text()").get()
            price_unit = dl.xpath(".//dd[@class='price_right']//span/text()").get()
            if price_number and price_unit:
                item['price'] = price_number + price_unit
            yield item

        next_url = response.urljoin(response.xpath("//div[@class='page_al']/p[1]/a/@href").get())
        print(next_url)
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse_esf, meta={'info': (province, city)},dont_filter=True)
            
