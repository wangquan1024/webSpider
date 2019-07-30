from urllib.request import Request,urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# python3中请求https时会默认开启ssh验证，所以需要关闭
headers = {
    'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
}

req = Request('http://www.douban.com/',headers=headers)

res = urlopen(req)
print(res.read().decode('utf-8'))