from threading import Thread
from Data.data_generator import Data
import time
import random

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        j=0
        while j<5:
            data = Data()
            datas = data.data_generator()
            self.queue.put(datas)

            print('Producer produce: ' + str(datas))

            time.sleep(random.random())
            j+=1
            