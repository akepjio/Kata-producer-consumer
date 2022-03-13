import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from queue import Queue
from Queue.consumer import Consumer
from Queue.producer import Producer

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # making the window
        self.geometry('620x200')

        self.table= self.create_tree_widget()


    def create_tree_widget(self):
        #define columns 
        cols = ('Name', 'firstname', 'Birth Date', 'Request Date', 'Generation Date', 'Status', 'QRcode')

        # initiating the table
        table = ttk.Treeview(self, columns=cols, show='headings')

        # define headings
        for col in cols:
            table.heading(col, text=col)
            table.grid(row=1, column=10, columnspan=300)
            table.place(x=300, y=200)
            
        move_down_button = Button(text="Move Down", command=self.down)
        move_down_button.grid(row=0, column=4, padx=5, pady=5)

        move_up_button = Button(text="Move Up", command=self.up)
        move_up_button.grid(row=0, column=5, padx=10, pady=10)
        
        table.bind('<Double-Button-1>', self.item_selected)

        table.grid(row=0, column=50, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=9, sticky='ns')

        # Create Striped Row Tags
        table.tag_configure('oddrow', background="white")
        table.tag_configure('evenrow', background="lightblue")

        # add data to tableview
        queue = Queue(10)
        p = Producer(queue)
        c = Consumer(queue, table)
        p.setDaemon(True)
        c.setDaemon(True)
        p.start()
        c.start()
        queue.join()

        return table

    #item selection
    def item_selected(self,event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    # Move Row Up
    def up(self):
        for row in self.table.selection():
            self.table.move(row, self.table.parent(row), self.table.index(row)-1)

    # Move Rown Down
    def down(self):
        for row in reversed(self.table.selection()):
            self.table.move(row, self.table.parent(row), self.table.index(row)+1)