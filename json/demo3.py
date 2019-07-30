import json

jsonData = '''{
    "a": 1,
    "b": 2
}
'''

# json.loads 可以解析json字符串
# text = json.loads(jsonData)
# print(text)

with open('obj.json','r',encoding='utf-8') as fp:
    txt = json.load(fp)
    print(txt)