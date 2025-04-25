import threading
import time

from threading import Thread, enumerate
from time import sleep

"""
1. use function to create thread
"""

print('-------------------------- 1. use function to create thread ----------------------------------')
def func(count):
    start = time.time()
    print('this is {} ...'.format(threading.current_thread().name))
    sleep(1)
    print('1 - use time {}'.format(time.time() - start))
    # with open(file='./test{}.txt'.format(count), mode='w', encoding='utf-8') as f:
    #     f.write("this is test")



start_main = time.time()
threads = []
for i in range(3):
    t = Thread(target=func, args=(i,))
    t.daemon = True
    t.start()
    threads.append(t)

## daemon=false: join阻塞主线程，子线程完成后，主线程才结束; 如果没有join，主程序执行完下面的print直接结束，子程序继续运行
for t in threads:
    t.join()

print('1 - all threads are end, use time {}'.format(time.time() - start_main))

"""
create a class to extend Thread class and implement run()
"""

print('-------------------------- 2. create a class to extend Thread class and implement run() ----------------------------------')
class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__(name=name)

    def run(self):
        start = time.time()
        print('this is {} ...'.format(self.name))
        sleep(1)
        print('use time {}'.format(time.time() - start))


start_main = time.time()
threads_1 = []
for i in range(3):
    t = MyThread('thread--{}'.format(i))
    t.start()
    threads_1.append(t)

for t in threads_1:
    t.join()

print('2 - all threads are end, use time {}'.format(time.time() - start_main))

"""
don't use lock for shared data in multi-threads
"""
print('-------------------------- 3. dont use lock for shared data in multi-threads ----------------------------------')
start_main = time.time()
total = 1000
def func(count):
    global total
    print('this is {} ...'.format(threading.current_thread().name))
    print('total {}'.format(total))
    num = total - count
    sleep(1)  ## when sleep can see total always 1000, if no sleep, the number are right  --线程不安全
    total = num
    print('left num {}'.format(total))


## start - code will return error num##
threads_2 = []
for i in range(1, 10):
    t = threading.Thread(target=func, name='thread-%d' % i, args=(10,))
    t.start()
    threads_2.append(t)

for t in threads_2:
    t.join()

print('total time used is {}'.format(time.time() - start_main))

# this is thread-1 ...
# total 1000
# this is thread-2 ...
# total 1000
# this is thread-3 ...
# total 1000
# left num 990left num 990
# left num 990
## end - code will return error num##

"""
use lock for shared data in multi-threads
"""
print('-------------------------- 4. use lock for shared data in multi-threads ----------------------------------')
start_main = time.time()
total = 1000
def func_2(count, lock):
    global total
    print('this is {} ...'.format(threading.current_thread().name))
    lock.acquire()
    print('total {}'.format(total))
    num = total - count
    sleep(1)
    total = num
    lock.release()
    print('left num {}'.format(total))

threads_3 = []
lock = threading.Lock()
for i in range(1, 10):
    t = threading.Thread(target=func_2, name='thread-%d' % i, args=(10, lock))
    t.start()
    threads_3.append(t)

for t in threads_3:
    t.join()
print('total time used is {}'.format(time.time() - start_main))

