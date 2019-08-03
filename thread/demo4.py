import threading
import random,time

# 采用while True这种方式的这者生产者和消费者模式，会造成一些性能浪费。
# 因为锁的获取和取消很消耗资源。
MONEY = 1000
glock = threading.Lock()
gTotalTime = 10
gTime = 0

# 生成者进行生成
class Producer(threading.Thread):
    def run(self):
        global MONEY
        global gTime
        while True:
            money = random.randint(100,1000)
            glock.acquire()
            gTime = gTime + 1
            if gTime >= gTotalTime:
                glock.release()
                break
            MONEY = MONEY + money
            print('%s 生成%d钱，剩余%d钱' %(threading.current_thread(),money,MONEY))
            glock.release()
            time.sleep(0.5)
        
# 消费者进行消费
class Consumer(threading.Thread):
    def run(self):
        global MONEY
        while True:
            money = random.randint(100,1000)
            glock.acquire()
            if MONEY > money:
                MONEY = MONEY - money
                print('消费者%s消费%d钱，剩余%d钱' %(threading.current_thread(),money,MONEY))
            else:
                if gTime >= gTotalTime:
                    glock.release()
                    break
                print('消费者%s想消费%d钱，余额不足' %(threading.current_thread(),money))
            glock.release()
            time.sleep(0.5)

def main():
    for x in range(5):
        t= Producer()
        t.start()
    
    for x in range(5):
        t = Consumer()
        t.start()


if __name__ == "__main__":
    main()