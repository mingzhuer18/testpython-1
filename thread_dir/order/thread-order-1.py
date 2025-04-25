import threading
import time

print(" ------------ 1. daemon is false, no join(), 主线程结束后子线程继续运行 -------------")
def func(count):
    start = time.time()
    print('this is {} ...'.format(threading.current_thread().name))
    time.sleep(1)
    print('1 - use time {}'.format(time.time() - start))

t_list = []
for i in range(4):
    t=threading.Thread(target=func, args=(10,))
    t_list.append(t)
    t.start()

print('main thread end')



