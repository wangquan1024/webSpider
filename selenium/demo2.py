from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
# 关闭当前页面
browser.close()
# 关闭浏览器
browser.quit()