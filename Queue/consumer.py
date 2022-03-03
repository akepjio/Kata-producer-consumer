from threading import Thread
import tkinter as tk
import time 
import random
import os.path


class Consumer(Thread):
    def __init__(self, queue, table):
        Thread.__init__(self)
        self.queue = queue
        self.table = table

    def run(self):
        j=0
        while j<10:
            datas = self.queue.get(True)

            status = random.choice(["vaccinated", "not vaccinated"])

            #add data to tableview
            for i in datas.keys():
                if status == "vaccinated":
                   script_path = os.getcwd()
                   pass_file_name = os.path.join(script_path, "Pass", datas[i]['lastname']+".txt")
                   f = open(pass_file_name, 'w+')
                   f.write("Pass of " + datas[i]['lastname'])
                   f.close()
                else:
                    pass_file_name = "No pass"

                if i % 2 == 0:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,pass_file_name),tags=('evenrow',))
                else:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,pass_file_name),tags=('oddrow',))
                
            self.queue.task_done()
            print('Consumer consume: ' + str(datas) + '\n')
            time.sleep(15)
            j+=1