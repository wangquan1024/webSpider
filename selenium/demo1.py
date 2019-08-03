from selenium import webdriver

# 创建实例
browser = webdriver.Chrome()
# 请求百度首页
browser.get("http://www.baidu.com")
# 获取网页源码
print(browser.page_source)
browser.close()
