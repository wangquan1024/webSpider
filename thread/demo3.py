import threading

glock = threading.Lock()
value = 0

def add_value():
    # global关键字标记改变量为全局变量
    # python在函数内只能对全局变量引用，不能修改，但是可以通过global关键字标记改变量为全局变量后就可以修改
    global value
    # 获取全局锁
    glock.acquire()
    for x in range(1000000):
        value +=1
    # 释放锁
    # 锁是为了防止多线程计算中，同时修改全局变量造成的数据错误
    glock.release()
    print(value)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
    main()
