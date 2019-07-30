from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
# 初始化生产一个XPath对象
html = etree.HTML(text)
# 解析对象输出代码
result = etree.tostring(html,encoding='utf-8')
print(result.decode('utf-8'))