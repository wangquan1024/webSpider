from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 可以使用行为链在页面中完成一系列操作
br = webdriver.Chrome()
br.get("https://www.baidu.com")

# 获得百度的输入框标签
input_tag = br.find_element_by_id('kw')
# 获得输入框的提交按钮标签
submit_btn = br.find_element_by_xpath('//input[@id="su"]')

action = ActionChains(br)
# move_to需要时webelement元素
action.move_to_element(input_tag)
action.send_keys_to_element(input_tag,'python')
action.move_to_element(submit_btn)
action.click(submit_btn)
action.perform()