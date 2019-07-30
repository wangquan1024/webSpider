import requests

proxy = {"http": "114.230.69.193:9999"}

# 代理只需填写proxies这个字段即可
res = requests.get("http://httpbin.org/ip",proxies=proxy)
print(res.content.decode('utf-8'))