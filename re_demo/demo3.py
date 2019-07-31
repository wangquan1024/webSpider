import re

text = 'a1234'

# match方法是从第一个字符开始匹配
# res = re.match('1',text)
# print(res.group())

# search方法从字符串中查找
# res = re.search('1',text)
# print(res.group())

# group分组，返回一个包含所有小组字符串的元组
# 从1开始才是第一个
# line = "Cats are smarter than dogs"
# res = re.match(r'(.*) are (.*?) .*',line)
# print(res.group())
# print(res.group(1))
# print(res.group(2))

# sub检索和替换
# 第一个参数是正则字符串，第二个参数是替换字符串，第三个参数是原始字符串
# phone = "2004-959-559 # 这是一个电话号码"
# res = re.sub('#.*$',"",phone)
# print(res)

