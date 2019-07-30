from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Cookie": "JSESSIONID=ABAAABAAAIAACBI0608D729FE12B0D5D27124E629455782; WEBTJ-ID=20190724090734-16c2184ebb1c89-0adffb4a939b99-37647e02-1764000-16c2184ebb2df0; _ga=GA1.2.1489015748.1563930455; _gid=GA1.2.255071094.1563930455; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563930455; user_trace_token=20190724090735-6bd1ab07-adaf-11e9-82aa-525400f775ce; LGSID=20190724090735-6bd1ae50-adaf-11e9-82aa-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZ1ZdBZOvfOkwCkyruBI4GADm5YsHk5Us1R5rpLEITBG%26ck%3D8010.1.80.293.151.311.157.169%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26wd%3D%26eqid%3Dd023d9a80004ac45000000025d37af52; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190724090735-6bd1b005-adaf-11e9-82aa-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_code; X_HTTP_TOKEN=253cd4b78efb158f6050393651ec9fe25c26f7f272; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563930507; LGRID=20190724090826-8aa8ea01-adaf-11e9-82aa-525400f775ce; SEARCH_ID=e513f966d5f3482d9b251a266d363fb6",
    "Referer": "https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF?labelWords=sug&fromSearch=true&suginput=qianduan"
}

req = request.Request('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',headers=headers)
res = request.urlopen(req)
print(res.read().decode('utf-8'))

