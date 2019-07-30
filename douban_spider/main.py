import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}

res = requests.get("https://movie.douban.com/cinema/nowplaying/wuhan/",headers=headers)
text = res.text

# 将抓取得数据按照一定的规则进行提取
# xpath返回时lists
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies=[]
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    img = li.xpath(".//img/@src")[0]
    movie = {
        "title":title,
        "score":score,
        "duration":duration,
        "region":region,
        "director":director,
        "actors":actors,
        "img":img
    }
    movies.append(movie)

print(movies)