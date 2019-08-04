from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LagouSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.position = []
    
    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parser_url(source)
            WebDriverWait(self.driver,timeout=10).until(
                # 参数是一个元组
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']//span[last()]"))
            )
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']//span[last()]")
            if "pager_next_disabled" in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()
            time.sleep(1)
       
        
    
    def parser_url(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
    
    def request_detail_page(self,url):
        # self.driver.get(url) 
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parser_detail_page(source)
        # 关闭当前页面
        self.driver.close()
        # 切换到工作列表页
        self.driver.switch_to_window(self.driver.window_handles[0])
    
    def parser_detail_page(self,source):
        html = etree.HTML(source)
        WebDriverWait(self.driver,timeout=10).until(
            # 参数是一个元组
            # 此处的xpath只能选取节点，不能选取到文本信息
            EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']//h4[@class='company']"))
        )
        company = html.xpath("//div[@class='job-name']//h4[@class='company']/text()")[0]
        position = html.xpath("//div[@class='job-name']//h2[@class='name']/text()")[0]
        salary = html.xpath("//dd[@class='job_request']//span[@class='salary']/text()")[0]
        job = {
            'company': company,
            'position': position,
            'salary': salary
        }
        self.position.append(job)
        print(self.position)
        print("++="*30)
        
def main():
    t= LagouSpider()
    t.run()

if __name__ == "__main__":
    main()
