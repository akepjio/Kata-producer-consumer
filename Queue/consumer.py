from threading import Thread
import tkinter as tk
import time 
import random
import os.path
import qrcode


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
                   img = qrcode.make(datas[i]['lastname'])
                   pass_file_name = os.path.join(script_path, "Pass", datas[i]['lastname']+".png")
                   img.save(pass_file_name)
                   if i % 2 == 0:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,'QRcode available'),tags=('evenrow',))
                   else:
                    self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,'QRcode available'),tags=('oddrow',))

                else:
                    if i % 2 == 0:
                        self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,'No QRcode'),tags=('evenrow',))
                    else:
                        self.table.insert('', tk.END, values=(datas[i]['lastname'],datas[i]['firstname'],datas[i]['Birth Date'],datas[i]['Request Date'],datas[i]['Generation Date'],status,'No QRcode'),tags=('oddrow',))
                
            self.queue.task_done()
            print('Consumer consume: ' + str(datas) + '\n')
            time.sleep(15)
            j+=1