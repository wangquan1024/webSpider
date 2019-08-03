# python中的list，dict，set，tuple都不是线程安全队列
# python中的queue队列属于线程安全，因为queue底层封装了锁。
import threading
import queue,time

# queue队列中有block参数，默认为true。
# 当队列满的时候，又要往队列里添加值时会默认阻塞当前线程
def set_value(q):
    index = 0
    while True:
        q.put(index)
        index +=1
        time.sleep(1)

# queue队列中有block参数，默认为true。
# 当队列空的时候，又要往外取值时会默认阻塞当前线程
def get_value(q):
    while True:
        x = q.get(q)
        print(x)

def main():
    q = queue.Queue(4)
    t = threading.Thread(target=set_value,args=[q])
    t1 = threading.Thread(target=get_value,args=[q])

    t.start()
    t1.start()

if __name__ == "__main__":
    main()
