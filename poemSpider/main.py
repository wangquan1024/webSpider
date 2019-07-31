import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

def get_poem(url):
    res = requests.get(url,headers)
    text = res.content.decode('utf-8')
    # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    contents_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in contents_tags:
        x = re.sub('<.*?>',"",content)
        contents.append(x.strip())
    
    poems = []
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            "title": title,
            "dynasty": dynasty,
            "author": author,
            "content": content
        }
        poems.append(poem)
    
    print(poems)

def main():
    for x in range(1,11):
        url = "https://www.gushiwen.org/default_{}.aspx".format(x)
        get_poem(url)

if __name__ == "__main__":
    main()