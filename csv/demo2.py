import csv

# 将python中字典数据保存为csv文件
headers = ['class','name','sex']

rows = [
    {'class': 1,'name':'jack','sex':'male'},
    {'class': 2,'name':'lucy','sex':'female'},
    {'class': 3,'name':'lily','sex':'female'}
]

with open('2.csv','w',encoding='utf-8') as fp:
    # 创建一个DictWriter对象，参数为一个文件对象fp，一个表头headers
    writer = csv.DictWriter(fp,headers)
    # 必须调用writerheader函数才能写入表头
    writer.writeheader()
    writer.writerows(rows)