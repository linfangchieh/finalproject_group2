import tkinter as tk #視窗
import tkinter.font as tkFont #字體
import tkinter.ttk as tt #下拉選單

class Page3(tk.Frame):

    def __init__(self, parent, controller):
        '''建立物件時一定要做的事'''
        tk.Frame.__init__(self, parent)
        self.creatWidgets()

    def creatWidgets(self):
        button2 = tk.Button(self, text="HAHAHAHHAHAHAHAHAHAHA")
        button2.grid(row = 0, column = 0)
