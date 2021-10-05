from threading import Thread, Lock
from time import sleep

count = 0

def increase(by, lock):
    global count

    lock.acquire()

    local_count = count
    local_count += by

    sleep(0.1)

    count = local_count
    print(f'counter={count}')

    lock.release()

lock = Lock()

t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'The final counter is {count}')
