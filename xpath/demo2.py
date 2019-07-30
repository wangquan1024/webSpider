from lxml import etree

# 指定HTMLparser可以修复HTML文件中缺失的声明信息
html=etree.parse('lagou.html',etree.HTMLParser())
result = etree.tostring(html,encoding='utf-8')

print(result.decode('utf-8'))

# 使用xpath()函数来过滤出当前想要的节点