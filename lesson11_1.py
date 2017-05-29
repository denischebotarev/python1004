import threading
import time


def clock(interval):
    while True:
        print('The time is {}'.format(time.time()))
        time.sleep(interval)


def hello(interval):
    while True:
        print('Hello!')
        time.sleep(interval)


t1 = threading.Thread(target=clock, args=(2,))
t1.start()

t2 = threading.Thread(target=hello, args=(4,))
t2.start()