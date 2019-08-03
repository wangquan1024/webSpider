from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 借助执行javascript打开一个新的网页
driver.execute_script("window.open('https://www.douban.com')")
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)
print(driver.page_source)

# driver.switch_to_window切换网页
# driver.window_handles是一个列表，里面装的都是句柄