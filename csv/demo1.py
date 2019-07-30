import csv

headers = ['class','name','sex']

rows = [
    (1,'jack','male'),
    (2,'lucy','female'),
    (3,'lily','female')
]

with open('1.csv','w',encoding='utf-8') as fp:
    # 创建writer对象
    writer = csv.writer(fp)
    writer.writerow(headers)
    writer.writerows(rows)