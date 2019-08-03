from selenium import webdriver

br = webdriver.Chrome()
br.get("https://www.baidu.com")

elem = br.find_element_by_id('kw')
# 返回标签名
print(elem.tag_name)
# 通过类名查找 找到第一个
# res = driver.find_element_by_class_name("result")
# print(res.text)

# res = driver.find_elements_by_class_name("result")
# print(res)
# driver.find_element_by_id()
# elements时查找所有元素
# driver.find_elements_by_id()

# res = driver.find_elements_by_css_selector(".result")
# print(res)
# driver.find_elements_by_css_selector()

# res = driver.find_element_by_tag_name("div")
# ress = driver.find_elements_by_tag_name("div")
# print(ress)

# res = driver.find_element_by_link_text("老男孩_百度百科")
# print(res.get_attribute("href"))

# 通过部分的链接标题 查找a标签
# res = driver.find_element_by_partial_link_text("老男孩_")
# print(res.get_attribute("href"))
# print(content)