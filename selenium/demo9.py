from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
# Chrome Options是一个配置chrome启动时属性的类
# 使用add_argument()方法添加
chromeOptions.add_argument('--proxy-server=http://180.118.247.3:9000')
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("http://httpbin.org/ip")