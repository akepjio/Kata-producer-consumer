from threading import Thread
from Data.data_generator import Data
import time

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        j=0
        while j<10:
            data = Data()
            datas = data.data_generator()
            self.queue.put(datas)

            print('Producer produce: ' + str(datas) + '\n')

            time.sleep(15)
            j+=1
            