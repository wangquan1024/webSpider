import requests
from lxml import etree

HEADERS = {
     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
BASE_URL = "https://www.dytt8.net"

def getdetailurl(url):
    res = requests.get(url,headers=HEADERS)
    text = res.content.decode('gbk',"ignore")
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls 

def parse_detail_page(url):
    movie = {}
    res = requests.get(url,headers=HEADERS)
    text = res.content.decode('gbk',"ignore")
    html = etree.HTML(text)
    title = html.xpath("//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoom = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoom.xpath(".//img/@src")
    movie['cover'] = imgs[0]
    movie['screenshot'] = imgs[1]
    
    def parse_info(info,rule):
        return info.replace(rule,'').strip()

    infos = zoom.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith('◎译　　名'):
            info = parse_info(info,'◎译　　名')
            movie['name'] = info
        elif info.startswith('◎片　　名'):
            info = parse_info(info,'◎片　　名')
            movie['realname'] = info
        elif info.startswith('◎年　　代'):
            info = parse_info(info,'◎年　　代')
            movie['year'] = info
        elif info.startswith('◎导　　演'):
            info = parse_info(info,'◎导　　演')
            movie['director'] = info
        elif info.startswith('◎主　　演'):
            info = parse_info(info,'◎主　　演')
            actors = [info]
            for itemIndex in range(index+1,len(infos)):
                actor = infos[itemIndex].strip()
                if actor.startswith('◎标　　签'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith('◎简　　介'):
            info = parse_info(info,'◎简　　介')
            for itemIndex in range(index+1,len(infos)):
                profile = infos[itemIndex].strip()
                if profile.startswith('【下载地址】'):
                    break
                movie['profile'] = profile
    download_url = zoom.xpath(".//table//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download'] = download_url
    return movie

def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,8):
        movies = []
        url = base_url.format(x)
        movie_detail = getdetailurl(url)
        for detail in movie_detail:
            movie = parse_detail_page(detail)
            print(movie)
            movies.append(movie)

def main():
    spider()

if __name__ == "__main__":
    main()