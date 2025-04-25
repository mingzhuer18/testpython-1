print('--------------------- 死锁 Lock ---------------------------')
import time
from threading import Thread, Lock


def eat_noodle1(name, noodle_lock, fork_lock):
    noodle_lock.acquire()
    print(f"{name} get noodle")
    time.sleep(1)
    fork_lock.acquire()
    print(f"{name} get fork")
    print(f"{name} start eat noodle")
    fork_lock.release()
    print(f"{name} put down noodle")
    noodle_lock.release()
    print(f"{name} put down noodle")


def eat_noodle2(name, noodle_lock, fork_lock):
    fork_lock.acquire()
    print(f"{name} get fork")
    time.sleep(1)
    noodle_lock.acquire()
    print(f"{name} get noodle")
    print(f"{name} start eat noodle")
    noodle_lock.release()
    print(f"{name} put down noodle")
    fork_lock.release()
    print(f"{name} put down noodle")


t_list = []
name_list = ["Einstein", "Curie"]
noodle_lock = Lock()
fork_lock = Lock()
Einstein = Thread(target=eat_noodle1, name="Einstein", args=("Einstein", noodle_lock, fork_lock))
t_list.append(Einstein)
Curie = Thread(target=eat_noodle2, name="Curie", args=("Curie", noodle_lock, fork_lock))
t_list.append(Curie)
for t in t_list:
    t.start()


