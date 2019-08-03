# condition方式的消费者和生成者模式
import threading,random,time

gCondition = threading.Condition()
gMoney = 1000
gTime = 0
gTotalTime = 10

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            gTime +=1
            if gTime >=gTotalTime:
                gCondition.release()
                break
            gMoney = gMoney + money
            # 唤醒所有休眠的线程
            gCondition.notify_all()
            print('生产者%s生成了%d的钱,一共有%d钱' %(threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            # 防止线程被唤醒是前面有线程排队，到本线程执行时，金库里的钱又不足的情况
            while gMoney < money:
                if gTime >=gTotalTime:
                    gCondition.release()
                    return
                print('消费者%s想消费了%d的钱,余额不足' %(threading.current_thread(),money))
                # 线程休眠，释放锁
                gCondition.wait()
            gMoney = gMoney - money
            print("消费者%s消费了%d的钱,剩余%d的钱" %(threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(1)

def main():
    for x in range(5):
        t= Producer()
        t.start()
    
    for x in range(5):
        t = Consumer()
        t.start()

if __name__ == "__main__":
    main()

