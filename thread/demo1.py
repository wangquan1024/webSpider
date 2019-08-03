import threading
import time

def writing():
    while True:
        print('thread %s is writing...' %threading.current_thread().name)
        time.sleep(5)

def painting():
    while True:
        print('thread %s is painting...' %threading.current_thread().name)
        time.sleep(5)

def main():
    # 通过threading模块配置两个线程，第一个参数是执行的函数,第二个参数是线程名字
    t1 = threading.Thread(target=writing,name='writing')
    t2 = threading.Thread(target=painting,name='painting')
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()