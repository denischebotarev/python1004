import threading
import time


class ClockThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            print('The time is {}'.format(time.ctime()))
            time.sleep(self.interval)


class HelloThread(ClockThread):
    def run(self):
        while True:
            print('Hello!')
            time.sleep(self.interval)


t1 = ClockThread(2)
t1.start()

t2 = HelloThread(4)
t2.start()