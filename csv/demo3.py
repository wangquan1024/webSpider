import csv

with open('1.csv') as fp:
    # 创建一个render对象，reader是一个可迭代的对象
    f_csv = csv.reader(fp)
    for row in f_csv:
        print(row)

with open('2.csv') as fp:
    # 已字典的方式读取csv文件
    reader = csv.DictReader(fp)
    for row in reader:
        print({'name':row['name'],'sex': row['sex']})
