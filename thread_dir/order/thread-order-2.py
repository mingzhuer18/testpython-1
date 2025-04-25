import threading
import time

print(" ------------ 2. daemon is false, have join(), 子线程结束后 主线程结束运行 -------------")
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

for t in t_list:
    t.join()

print('main thread end')



