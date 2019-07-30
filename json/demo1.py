import json

# 将python对象编码成json字符串

obj = [
    {
        'name': 'jack',
        'age': 18
    },
    {
        'name': 'lucy',
        'age': 20
    }
]

obj1 = [
    {
        'name': '杰克',
        'age': 18
    },
    {
        'name': '露西',
        'age': 20
    }
]

res = json.dumps(obj)
# ensure_ascii默认为True会使用acsii编码
res1 = json.dumps(obj1,ensure_ascii=False)
print(res)
print(res1)