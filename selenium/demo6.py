from selenium import webdriver

br = webdriver.Chrome()
br.get("https://www.baidu.com")

# 获取所有cookie
for cookie in br.get_cookies():
    print(cookie)

print("+++"*40)
# 根据key值获取
print(br.get_cookie('PSTM'))
# 删除某个cookie
br.delete_cookie('PSTM')
print("+++"*40)
# 删除所有cookie
print(br.get_cookie('PSTM'))
br.delete_all_cookies()