import requests

data = {
    "first": "true",
    "pn": 1,
    "kd": "前端工程师"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Cookie": "JSESSIONID=ABAAABAAAIAACBI0608D729FE12B0D5D27124E629455782; WEBTJ-ID=20190724090734-16c2184ebb1c89-0adffb4a939b99-37647e02-1764000-16c2184ebb2df0; _ga=GA1.2.1489015748.1563930455; _gid=GA1.2.255071094.1563930455; user_trace_token=20190724090735-6bd1ab07-adaf-11e9-82aa-525400f775ce; LGUID=20190724090735-6bd1b005-adaf-11e9-82aa-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; LGSID=20190724230347-3ccf1d83-ae24-11e9-a4f1-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DY3QvcS1zyL65H1rgqf1iaC2hOuXrfJDFLhnjPYH0mo_%26ck%3D5928.1.88.204.144.203.141.370%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26wd%3D%26eqid%3Dd8edd0970001d1d5000000055d38734f; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c24828a0a7da-04394e03c34eeb-37647e02-3686400-16c24828a0b38c%22%2C%22%24device_id%22%3A%2216c24828a0a7da-04394e03c34eeb-37647e02-3686400-16c24828a0b38c%22%2C%22props%22%3A%7B%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2275.0.3770.100%22%7D%7D; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563930455,1563980627,1563980929; X_HTTP_TOKEN=253cd4b78efb158f3490893651ec9fe25c26f7f272; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563980944; LGRID=20190724230903-f95ec139-ae24-11e9-a4f1-5254005c3644; SEARCH_ID=6037dd1e422040d2a51a297696050e3f",
    "Referer": "https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=qiand"
}

# request.post方法的参数只需要在data这个参数中传递就可以刻，不需要编码，requests会自动帮我们处理好
res = requests.post("https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false",data=data,headers=headers)
print(res.content.decode("utf-8"))