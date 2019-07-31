import re

text = 'aetdfa123'

# *匹配子表达式零次或者多次
# res = re.match('\w*',text)
# print(res.group())

# +匹配子表达式一次或者多次
# res = re.match('a+',text)
# print(res.group())

# ？匹配子表达式零次或者一次
# res = re.match('a?',text)
# print(res.group())

# ^表示某子表达式开始
# res = re.match('^a',text)
# print(res.group())

# $表示某子表达式结束
# res = re.match('3$',text)
# print(res.group())

# 标记一个子表达式的开始和结束位置
# res = re.search('(\w{3})',text)
# print(res.group(1))