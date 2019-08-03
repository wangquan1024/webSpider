import threading,queue,requests,os,time
from urllib import request
from lxml import etree

class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parser_url(url)
    
    def parser_url(self,url):
        res = requests.get(url,headers=self.headers)
        text = res.text
        html = etree.HTML(text)
        print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
        imgs = html.xpath("//div[@class='random_article']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            self.img_queue.put((img_url,filename))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    
    def run(self):
        while True:
            if self.page_queue.empty and self.img_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'images/'+filename)
            print(filename)

def main():
    page_queue = queue.Queue(10)
    img_queue = queue.Queue(100)
    for x in range(10):
        url = "https://www.doutula.com/article/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()
    
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == "__main__":
    main()
