import requests,os
from lxml import etree
from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

def parser_url(url):
    res = requests.get(url,headers)
    text = res.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='random_article']//img[@class!='gif']")
    for img in imgs:
        # 获取元素中的属性值
        img_url = img.get('data-original')
        alt = img.get('alt')
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        # 如果出现报错，可以在当前project下新建一个文件夹
        request.urlretrieve(img_url,'images/'+filename)
        

def main():
    for x in range(1,101):
        url="http://www.doutula.com/article/list/?page=%d" % x
        parser_url(url)

if __name__ == "__main__":
    main()