from concurrent.futures import ThreadPoolExecutor
import time

def task(count):
    time.sleep(3)
    print('task done - %d \n' % count)

with ThreadPoolExecutor(max_workers=3) as executor:
    results = {str(i):executor.submit(task, i) for i in range(10)}
    for i, r in results.items():
        print(i, r.result())
