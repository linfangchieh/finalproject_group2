import tkinter as tk #視窗
import tkinter.font as tkFont #字體
import tkinter.ttk as tt #下拉選單


''' 三個子視窗獨立寫出 '''
from page1 import Page1 as WinOne
from page2 import Page2 as WinTwo
from page3 import Page3 as WinThree


class Projectapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.container = tk.Frame(self)
        self.container.grid(row = 0, column = 0)

        self.frames = {}

        for F in (WinOne, WinTwo, WinThree):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(WinOne)
        self.menubar = tk.Menu( self.container )
        self.win1 = tk.Menu(self.menubar, tearoff = 0)
        self.win1.add_command(label = "GOGOGO!", command = lambda: self.show_frame(WinOne))
        self.menubar.add_cascade(label="查詢即時匯率", menu=self.win1)

        self.win2 = tk.Menu(self.menubar, tearoff = 0)
        self.win2.add_command(label = "GOGOGO!", command = lambda: self.show_frame(WinTwo))
        self.menubar.add_cascade(label = "換匯計算機", menu = self.win2)


        self.win3 = tk.Menu(self.menubar, tearoff = 0)
        self.win3.add_command(label = "GOGOGO!", command = lambda: self.show_frame(WinThree))
        self.menubar.add_cascade(label = "寄信通知我", menu = self.win3)

        self.config(menu = self.menubar)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Projectapp()
app.iconbitmap('./img/notes.ico')
app.title('小傑換錢給小盧')
app.mainloop()
