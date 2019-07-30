import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

ALL_DATA = []

def get_weather(url):
    res = requests.get(url,headers=HEADERS)
    text = res.content.decode('utf-8')
    # html5lib可以以浏览器的方式解析标签，容错性最好
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find_all('div',class_='conMidtab')[0]
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            td = tr.find_all('td')
            if index == 0:
                city_td = td[1]
                max_temp = td[4]
            elif index > 0:
                city_td = td[0]
                max_temp = td[3]
            city = list(city_td.stripped_strings)[0]
            max_temperature = list(max_temp.stripped_strings)[0]
            ALL_DATA.append({'city':city,'max_temperature':max_temperature})


    
def main():
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml#",
        "http://www.weather.com.cn/textFC/db.shtml#",
        "http://www.weather.com.cn/textFC/hd.shtml#",
        "http://www.weather.com.cn/textFC/hz.shtml#",
        "http://www.weather.com.cn/textFC/hn.shtml#",
        "http://www.weather.com.cn/textFC/xb.shtml#",
        "http://www.weather.com.cn/textFC/xn.shtml#",
        "http://www.weather.com.cn/textFC/gat.shtml#"
    ]
    for url in urls:
        get_weather(url)
    print(ALL_DATA)

if __name__ == "__main__":
    main()