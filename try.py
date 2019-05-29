from tkinter import *
 
master = Tk()
 
w = Label(master, text="Hello, world!")
b = Button(master, text="Louder",
           command=lambda: w.config(text='HELLO, WORLD!', font=("", 20)))
 
v = StringVar()
v.set("Hello from StringVar.")
w2 = Label(master, textvariable=v)
b2 = Button(master, text="Louder, StringVar",
            command=lambda: v.set("HEELLOOO FROM STRINGVAR!!!"))
w.pack()
b.pack()
w2.pack()
b2.pack()
mainloop()