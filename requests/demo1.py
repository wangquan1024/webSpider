import requests

# requests直接调用get或者post方法就可以了
# res = requests.get("https://www.baidu.com") 
# text和content的区别在于content时byte类型
# print(res.text)
# print(res.content)
# print(res.url)
# 返回的表头的状态
# print(res.status_code)
# 返回表头的编码方式
# print(res.encoding)

params = {
    "wd": '中国'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

res = requests.get("https://www.baidu.com/s",params=params,headers=headers)
print(res.content.decode('utf-8'))
