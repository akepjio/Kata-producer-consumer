from threading import Thread
import tkinter as tk
import time 
import random


class Consumer(Thread):
    def __init__(self, queue, table):
        Thread.__init__(self)
        self.queue = queue
        self.table = table

    def run(self):
        j=0
        while j<5:
            datas = self.queue.get(True)

            choice = random.choice(["vaccinated", "not vaccinated"])

            #add data to tableview
            for i in datas.keys():
                if i % 2 == 0:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],choice),tags=('evenrow',))
                else:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],choice),tags=('oddrow',))
                
            self.queue.task_done()
            print('Consumer consume: ' + str(datas))
            time.sleep(random.random())
            j+=1