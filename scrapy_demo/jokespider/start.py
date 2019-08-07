from scrapy import cmdline

# 字符串会切割为列表
cmdline.execute("scrapy crawl joke".split())