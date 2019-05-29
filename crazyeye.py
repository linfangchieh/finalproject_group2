import tkinter as tk
import tkinter as tk
import tkinter.font as tkFont
import random

class Game(tk.Frame):
	score = 0
	ans = -1
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
		
	def createWidgets(self):
		font1 = tkFont.Font(size = 32, family = "Berlin Sans FB Demi") #設定字型
		self.label = tk.Label(self,text ="Crazy Eyes", font = font1,height = 1, width = 20)
		self.label.grid(row=0, column = 0, columnspan = 4, sticky = tk.SE + tk.NW )
		rgb1 = (183, 247, 49) #rgb顏色設定
		bgcolor = '#%02x%02x%02x'% rgb1 #將rgb格式轉成hex格式
		self.button = {}
		for i in range(16):
			self.button[i] = tk.Button(self, width = 8, height = 8, bg = bgcolor, command = lambda f = i:self.clickBtn(f))
			self.button[i].grid(row = int(i / 4) + 2, column = i % 4, sticky = tk.SE + tk.NW)  		
			
	def clickBtn(self, index):
		self.checkAnswer(index)
		self.changeColor()
	def checkAnswer(self, index):
		if self.ans == index:
			self.score += 1
			self.label.configure(text = "Score:" + str(self.score))
		else:
			self.score = 0
			self.label.configure(text = "Score:" + str(self.score))
	def changeColor(self):
		r = random.randint(0, 255) 
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		rgb1 = (r, g, b)
		a = 50 - self.score * 2 #隨著分數越高，色差會越近
		if a < 5:
			a = 5
		if r + a > 255:
			rgb2 = (r - a, g, b)
		else:
			rgb2 = (r + a, g, b)
		bgcolor1 = '#%02x%02x%02x'% rgb1 
		bgcolor2 = '#%02x%02x%02x'% rgb2
		for i in range(16):
			self.button[i].configure(bg = bgcolor1)
		self.ans = random.randint(0, 15)
		self.button[self.ans].configure(bg = bgcolor2)
			
gg = Game()
gg.master.title("CrazyEyesGame")
gg.mainloop()


