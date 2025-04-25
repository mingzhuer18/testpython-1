import sys
import threading
import time
from time import sleep

print(" ------------ 3. daemon is True, no join(), 主线程（以及所有非守护进程）结束运行,子线程立即结束 -------------")
def func(count):
    start = time.time()
    print('this is {} ...'.format(threading.current_thread().name), threading.current_thread().daemon)
    time.sleep(4)
    print('{} use time {}'.format(threading.current_thread().name,time.time() - start), "\n")

for i in range(4):
    t=threading.Thread(target=func, name="thread-{}".format((i+1)), args=(10,))
    # if i<2:
    #     t.daemon=True
    t.daemon = True
    t.start()

sleep(1)
print('main thread end')

"""
所有子线程都设置为daemon为true，主线程结束后，子线程也结束
但是如果部分设置为true，部分为false，实际现象是主线程结束时子线程仍然执行 -- chatgpt说python解释器要等待非后台守护进程结束才真的结束
"""


