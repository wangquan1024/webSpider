import threading
import time

# 从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
class Writing(threading.Thread):
    def run(self):
        for x in range(1,5):
            print('%s is writing' % threading.current_thread())

class Painting(threading.Thread):
    def run(self):
        for x in range(1,5):
            print('%s is painting' % threading.current_thread())

def main():
    t1 = Writing()
    t2 = Painting()

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()