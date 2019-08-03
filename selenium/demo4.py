from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

br = webdriver.Chrome()
# br.get("https://www.baidu.com")

# input_tag = br.find_element_by_id('kw')
# # 往表单内输入
# input_tag.send_keys('python')
# time.sleep(5)
# # 清除表单内输入
# input_tag.clear()

# .click()可以点击单选框

# 处理下拉选框的话需要从selenium.webdriver.support.select引入Select

# # 通过索引选择
# Select(br.find_element_by_name("storeDeclare.cityLine")).select_by_index("3")
# 通过value值选择
# Select(br.find_element_by_name("storeDeclare.cityLine")).select_by_value("3线")
# 通过文本值选择
# Select(br.find_element_by_name("storeDeclare.cityLine")).select_by_visible_text("3线")