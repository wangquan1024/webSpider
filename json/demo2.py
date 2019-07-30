import json

# json.dump会将python对象编码，然后存储到本地中
obj = [
    {
        'name': '杰克',
        'age': 18
    },
    {
        'name': '露西',
        'age': 20
    }
]

# with方式打开一个文件后，会自动帮我们关闭文件，不需要手动操作
with open('obj.json','w',encoding='utf-8') as fp:
    json.dump(obj,fp,ensure_ascii=False)