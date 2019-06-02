import tkinter as tk #視窗
import tkinter.font as tkFont #字體
import tkinter.ttk as tt #下拉選單
from PIL import ImageTk, Image #插圖檔
import tkinter.messagebox #對話框
import pandas #爬的
import sys #贊助用
import webbrowser #贊助用
import matplotlib.pyplot as plt

class Page2(tk.Frame):

	def __init__(self, parent, controller):
		'''建立物件時一定要做的事'''
		tk.Frame.__init__(self, parent)
		self.creatWidgets()

	def creatWidgets(self):
		'''建立元件'''
		#格式
		f1 = tkFont.Font(size = 15, family = "Consolas")
		f2 = tkFont.Font(size = 12, family = "微軟正黑體")

		self.var1 = tk.StringVar(None, " ")
		self.var2 = tk.StringVar(None, " ")

		'''物件'''
		#匯率種類
		self.labelname1 = tk.Label(self, text = "**匯率種類**", height = 1, width = 12, font = f2, fg = "SpringGreen4")
		self.rbuttonl = tk.Radiobutton(self, text = "現金匯率", variable = self.var1, value = "cash", height = 1, width = 8, font = f2)
		self.rbutton2 = tk.Radiobutton(self, text = "即期匯率", variable = self.var1, value = "current", height = 1, width = 8, font = f2)
		#持有幣別
		self.labelname6 = tk.Label(self, text = "**換匯模式**", height = 1, width = 12, font = f2, fg = "SpringGreen4")
		self.rbutton3 = tk.Radiobutton(self, text = "持有幣別", variable = self.var2, value = "hold", height = 1, width = 12, font = f2)
		self.droplist1 = tt.Combobox(self, width = 14, values = ["請選擇持有幣別", "新臺幣 (NTD)", "美金 (USD)", "港幣 (HKD)", "英鎊 (GBP)", "澳幣 (AUD)", "加拿大幣 (CAD)", "新加坡幣 (SGD)", "瑞士法郎 (CHF)", "日圓 (JPY)", "南非幣 (ZAR)", "瑞典幣 (SEK)", "紐元 (NZD)", "泰幣 (THB)", "菲國比索 (PHP)", "印尼幣 (IDR)", "歐元 (EUR)", "韓元 (KRW)", "越南盾 (VND)", "馬來幣 (MYR)", "人民幣 (CNY)"],  font = f2, state = "readonly")
		self.droplist1.current(0)
		self.txtlabel1 = tk.Text(self, height = 1, width = 16, font = f2)
		#兌換幣別
		self.rbutton4 = tk.Radiobutton(self, text = "兌換幣別", variable = self.var2, value = "convert", height = 1, width = 12, font = f2)
		self.droplist2 = tt.Combobox(self, width = 14, values = ["請選擇兌換幣別", "新臺幣 (NTD)", "美金 (USD)", "港幣 (HKD)", "英鎊 (GBP)", "澳幣 (AUD)", "加拿大幣 (CAD)", "新加坡幣 (SGD)", "瑞士法郎 (CHF)", "日圓 (JPY)", "南非幣 (ZAR)", "瑞典幣 (SEK)", "紐元 (NZD)", "泰幣 (THB)", "菲國比索 (PHP)", "印尼幣 (IDR)", "歐元 (EUR)", "韓元 (KRW)", "越南盾 (VND)", "馬來幣 (MYR)", "人民幣 (CNY)"],  font = f2, state = "readonly")
		self.droplist2.current(0)
		self.txtlabel2 = tk.Text(self, height = 1, width = 16, font = f2)
		#參考匯率
		self.labelname7 = tk.Label(self, text = "**參考匯率（外幣：臺幣）**", height = 1, width = 20, font = f2, fg = "SpringGreen4")
		self.labelname2 = tk.Label(self, text = "匯率1", height = 1, width = 8, font = f2)
		self.labelname3 = tk.Label(self, height = 1, width = 14, font = f2 , bg = "white")
		self.labelname4 = tk.Label(self, text = "匯率2", height = 1, width = 8, font = f2)
		self.labelname5 = tk.Label(self, height = 1, width = 14, font = f2 , bg = "white")
		#按鈕
		self.btn1 = tk.Button(self, text = "試算", height = 1, width = 4, font = f2, bg = "gold", command = self.clickBtn_convert)
		self.btn2 = tk.Button(self, text = "互換", height = 1, width = 4, font = f2, bg = "gold", command = self.clickBtn_change)
		self.btn3 = tk.Button(self, text = "清除", height = 1, width = 4, font = f2, bg = "gold", command = self.clickBtn_clean)

		#排版
		self.blankc0r1 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r2 = tk.Label(self, height = 1, width = 4, font = f2)
		self.blankc0r4 = tk.Label(self, height = 1, width = 4, font = f2)
		self.blankc0r5 = tk.Label(self, height = 1, width = 4, font = f2)
		self.blankc0r6 = tk.Label(self, height = 1, width = 4, font = f2)
		self.blankc0r7 = tk.Label(self, height = 1, width = 4, font = f2)
		self.blankc0r10 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r11 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r12 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r13 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r14 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r15 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r16 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r17 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r18 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r19 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r20 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r21 = tk.Label(self, height = 1, width = 7, font = f2)
		self.blankc0r22 = tk.Label(self, height = 1, width = 7, font = f2)

		self.blankc30r3 = tk.Label(self, text = "|", height = 1, width = 5, font = f2)
		self.blankc30r4 = tk.Label(self, text = "|", height = 1, width = 5, font = f2)
		self.blankc30r5 = tk.Label(self, text = "|", height = 1, width = 5, font = f2)
		self.blankc30r6 = tk.Label(self, text = "|", height = 1, width = 5, font = f2)

		#圖_轉換箭頭
		self.imagearrow = ImageTk.PhotoImage(file = "./img/arrow1.png")
		self.labelname_arrow = tk.Label(self, image = self.imagearrow, height = 12, width = 30, font = f2)
		#圖_右方大圖
		self.image1 = ImageTk.PhotoImage(file = "./img/exchange2.png")
		self.label_image = tk.Label(self, image = self.image1, height = 250, width = 255, font = f2)

		#使用說明
		self.labelname_ins0 = tk.Label(self, text = " ", height = 1, width = 12, font = f2)
		self.labelname_ins1 = tk.Label(self, text = "**使用說明**", height = 1, width = 12, font = f2, fg = "SpringGreen4")
		self.labelname_ins2 = tk.Label(self, text = "STEP 1 選擇匯率種類", height = 1, width = 20, font = f2)
		self.labelname_ins3 = tk.Label(self, text = "STEP 2 選擇換匯模式", height = 1, width = 20, font = f2)
		self.labelname_ins4 = tk.Label(self, text = "　(1)計算特定金額之持有幣別「能換取多少兌換幣別」", height = 1, width = 42, font = f2)
		self.labelname_ins5 = tk.Label(self, text = "　　 點選持有幣別，並輸入持有幣別之金額", height = 1, width = 36, font = f2)
		self.labelname_ins6 = tk.Label(self, text = "　(2)計算欲換取特定金額之兌換幣別「需要準備多少持有幣別」", height = 1, width = 48, font = f2)
		self.labelname_ins7 = tk.Label(self, text = " 　　點選兌換幣別，並輸入欲兌換多少兌換幣別", height = 1, width = 39, font = f2)
		self.labelname_ins8 = tk.Label(self, text = "STEP 3 點選按鈕", height = 1, width = 18, font = f2)
		self.labelname_ins9 = tk.Label(self, text = "　(1)試算：計算出結果與參考匯率", height = 1, width = 29, font = f2)
		self.labelname_ins10 = tk.Label(self, text = "　(2)互換：轉換至另一換匯模式", height = 1, width = 27, font = f2)
		self.labelname_ins11 = tk.Label(self, text = "　(3)清除：清除輸入之金額", height = 1, width = 24, font = f2)
		self.labelname_exc = tk.Label(self, text = "**輸入之外幣←匯率1→新台幣←匯率2→計算之外幣", height = 1, width = 39, font = f2)

		'''位置'''
		self.labelname1.grid(row = 0, column = 4, columnspan = 12, sticky = tk.W) #匯率種類
		self.rbuttonl.grid(row = 1, column = 7, columnspan = 8, sticky = tk.W) #現金匯率
		self.rbutton2.grid(row = 1, column = 17,columnspan = 8, sticky = tk.W) #即期匯率

		self.labelname6.grid(row = 2, column = 4, columnspan = 12, sticky = tk.W) #換匯模式
		self.rbutton3.grid(row = 3, column = 6, columnspan = 12, sticky = tk.W) #持有幣別-單選
		self.droplist1.grid(row = 4, column = 6,columnspan = 14, sticky = tk.W) #持有幣別-下拉選單
		self.txtlabel1.grid(row = 5, column = 6, columnspan = 16, sticky = tk.W) #持有幣別-金額

		self.rbutton4.grid(row = 3, column = 24,columnspan = 12, sticky = tk.W)  #兌換幣別-單選
		self.droplist2.grid(row = 4, column = 24, columnspan = 19, sticky = tk.W) #兌換幣別-下拉選單
		self.txtlabel2.grid(row = 5, column = 24, columnspan = 20, sticky = tk.W) #兌換幣別-金額

		self.labelname7.grid(row = 2, column = 57, columnspan = 21, sticky = tk.W) #參考匯率
		self.labelname2.grid(row = 4, column = 55, columnspan = 8, sticky = tk.W) #匯率1
		self.labelname3.grid(row = 4, column = 63, columnspan = 14, sticky = tk.W) #參考匯率1-顯示
		self.labelname4.grid(row = 5, column = 55, columnspan = 8, sticky = tk.W) #匯率2
		self.labelname5.grid(row = 5, column = 63, columnspan = 14, sticky = tk.W) #參考匯率2-顯示

		self.btn1.grid(row = 7, column = 6, columnspan = 4, sticky = tk.W) #按鈕-試算
		self.btn2.grid(row = 7, column = 11, columnspan = 4, sticky = tk.W) #按鈕-互換
		self.btn3.grid(row = 7, column = 16, columnspan = 5, sticky = tk.W) #按鈕-清除

		#排版
		self.blankc0r1.grid(row = 1, column = 0, columnspan = 7)
		self.blankc0r2.grid(row = 4, column = 0, columnspan = 4)
		self.blankc0r4.grid(row = 5, column = 0, columnspan = 4)
		self.blankc0r5.grid(row = 6, column = 0, columnspan = 4)
		self.blankc0r6.grid(row = 7, column = 0, columnspan = 4)

		self.blankc0r10.grid(row = 11, column = 0, columnspan = 7)
		self.blankc0r11.grid(row = 12, column = 0, columnspan = 7)
		self.blankc0r12.grid(row = 13, column = 0, columnspan = 7)
		self.blankc0r13.grid(row = 14, column = 0, columnspan = 7)
		self.blankc0r14.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r15.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r16.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r17.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r18.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r19.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r20.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r21.grid(row = 15, column = 0, columnspan = 7)
		self.blankc0r22.grid(row = 15, column = 0, columnspan = 7)

		self.blankc30r3.grid(row = 2, column = 48, columnspan = 5)
		self.blankc30r4.grid(row = 3, column = 48, columnspan = 5)
		self.blankc30r5.grid(row = 4, column = 48, columnspan = 5)
		self.blankc30r6.grid(row = 5, column = 48, columnspan = 5)

		self.labelname_arrow.grid(row = 5, column = 14, columnspan = 15) #圖_箭頭
		self.label_image.grid(row = 10, column = 55, rowspan = 255, columnspan = 255) #右方大圖

		#使用說明
		self.labelname_ins0.grid(row = 10, column = 4, columnspan = 12, sticky = tk.W)
		self.labelname_ins1.grid(row = 11, column = 4, columnspan = 12, sticky = tk.W)
		self.labelname_ins2.grid(row = 12, column = 4, columnspan = 20, sticky = tk.W)
		self.labelname_ins3.grid(row = 13, column = 4, columnspan = 20, sticky = tk.W)
		self.labelname_ins4.grid(row = 14, column = 4, columnspan = 50, sticky = tk.W)
		self.labelname_ins5.grid(row = 15, column = 4, columnspan = 50, sticky = tk.W)
		self.labelname_ins6.grid(row = 16, column = 4, columnspan = 50, sticky = tk.W)
		self.labelname_ins7.grid(row = 17, column = 4, columnspan = 50, sticky = tk.W)
		self.labelname_ins8.grid(row = 18, column = 4, columnspan = 20, sticky = tk.W)
		self.labelname_ins9.grid(row = 19, column = 4, columnspan = 30, sticky = tk.W)
		self.labelname_ins10.grid(row = 20, column = 4, columnspan = 30, sticky = tk.W)
		self.labelname_ins11.grid(row = 21, column = 4, columnspan = 30, sticky = tk.W)
		self.labelname_exc.grid(row = 22, column = 4, columnspan = 50, sticky = tk.W)

	def checkMode(self, mode_cacuf, mode_convertf, currency_holdf, currency_convertf):
		'''檢驗有沒有選模式'''
		if mode_cacuf != "cash" and mode_cacuf != "current":
			tkinter.messagebox.showerror(title = "未選擇模式", message = "請選擇匯率種類！")

		if currency_holdf == "請選擇持有幣別":
			tkinter.messagebox.showerror(title = "未選擇幣別", message = "請選擇持有幣別！")
		if currency_convertf == "請選擇兌換幣別":
			tkinter.messagebox.showerror(title = "未選擇幣別", message = "請選擇兌換幣別！")

	def checkNum(self, checknumf):
		'''驗證輸入的是否為數字'''
		try:
			numf = float(checknumf)
			return numf
		except ValueError:
			tkinter.messagebox.showerror(title = "輸入錯誤", message = "請輸入阿拉伯數字！")
			self.txtlabel1.delete("1.0", tk.END)
			self.txtlabel2.delete("1.0", tk.END)

	def creatWindow(self, myTitle):
		'''贊助視窗'''
		self.top = tkinter.Toplevel(self)
		self.top.title(myTitle)
		self.top.attributes('-topmost', 1)

		window1 = tk.IntVar(self, value = 0)
		self.imagedonate = ImageTk.PhotoImage(file = "./img/donate.jpg")
		labeldonate = tk.Label(self.top, image = self.imagedonate, height = 500, width = 500)
		labeldonate.grid(row = 0, column = 0, columnspan = 4, sticky = tk.W)

	def rich(self, numrich):
		'''是否為富豪用戶'''
		if numrich >= 1000000:
			yesno = tkinter.messagebox.askyesno(title = "大大請贊助", message = "喜歡我們的程式嗎\n除了去修商管程式設計外\n請贊助我們:)")

			if yesno == True:
				window_donate = self.creatWindow("請掃描QRcode來贊助我們哦❤")
			else:
				tkinter.messagebox.showinfo(title = "我們會繼續努力！", message = "期待你成為我們的乾爹/乾媽")

	def getExrate(self, cacu, buysell, ctype):
		'''爬匯率'''
		dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
		table = dfs[0]
		if cacu == "cash":
			if buysell == "本行買入":
				if ctype == "美金 (USD)":
					return float(table.iat[0,1])
				elif ctype == "港幣 (HKD)":
					return float(table.iat[1,1])
				elif ctype == "英鎊 (GBP)":
					return float(table.iat[2,1])
				elif ctype == "澳幣 (AUD)":
					return float(table.iat[3,1])
				elif ctype == "加拿大幣 (CAD)":
					return float(table.iat[4,1])
				elif ctype == "新加坡幣 (SGD)":
					return float(table.iat[5,1])
				elif ctype == "瑞士法郎 (CHF)":
					return float(table.iat[6,1])
				elif ctype == "日圓 (JPY)":
					return float(table.iat[7,1])
				elif ctype == "南非幣 (ZAR)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供南非幣現金買賣！")
				elif ctype == "瑞典幣 (SEK)":
					return float(table.iat[9,1])
				elif ctype == "紐元 (NZD)":
					return float(table.iat[10,1])
				elif ctype == "泰幣 (THB)":
					return float(table.iat[11,1])
				elif ctype == "菲國比索 (PHP)":
					return float(table.iat[12,1])
				elif ctype == "印尼幣 (IDR)":
					return float(table.iat[13,1])
				elif ctype == "歐元 (EUR)":
					return float(table.iat[14,1])
				elif ctype == "韓元 (KRW)":
					return float(table.iat[15,1])
				elif ctype == "越南盾 (VND)":
					return float(table.iat[16,1])
				elif ctype == "馬來幣 (MYR)":
					return float(table.iat[17,1])
				elif ctype == "人民幣 (CNY)":
					return float(table.iat[18,1])
			else: #本行賣出
				if ctype == "美金 (USD)":
					return float(table.iat[0,2])
				elif ctype == "港幣 (HKD)":
					return float(table.iat[1,2])
				elif ctype == "英鎊 (GBP)":
					return float(table.iat[2,2])
				elif ctype == "澳幣 (AUD)":
					return float(table.iat[3,2])
				elif ctype == "加拿大幣 (CAD)":
					return float(table.iat[4,2])
				elif ctype == "新加坡幣 (SGD)":
					return float(table.iat[5,2])
				elif ctype == "瑞士法郎 (CHF)":
					return float(table.iat[6,2])
				elif ctype == "日圓 (JPY)":
					return float(table.iat[7,2])
				elif ctype == "南非幣 (ZAR)":
					return float(table.iat[8,2])
				elif ctype == "瑞典幣 (SEK)":
					return float(table.iat[9,2])
				elif ctype == "紐元 (NZD)":
					return float(table.iat[10,2])
				elif ctype == "泰幣 (THB)":
					return float(table.iat[11,2])
				elif ctype == "菲國比索 (PHP)":
					return float(table.iat[12,2])
				elif ctype == "印尼幣 (IDR)":
					return float(table.iat[13,2])
				elif ctype == "歐元 (EUR)":
					return float(table.iat[14,2])
				elif ctype == "韓元 (KRW)":
					return float(table.iat[15,2])
				elif ctype == "越南盾 (VND)":
					return float(table.iat[16,2])
				elif ctype == "馬來幣 (MYR)":
					return float(table.iat[17,2])
				elif ctype == "人民幣 (CNY)":
					return float(table.iat[18,2])
		else: #"current"
			if buysell == "本行買入":
				if ctype == "美金 (USD)":
					return float(table.iat[0,3])
				elif ctype == "港幣 (HKD)":
					return float(table.iat[1,3])
				elif ctype == "英鎊 (GBP)":
					return float(table.iat[2,3])
				elif ctype == "澳幣 (AUD)":
					return float(table.iat[3,3])
				elif ctype == "加拿大幣 (CAD)":
					return float(table.iat[4,3])
				elif ctype == "新加坡幣 (SGD)":
					return float(table.iat[5,3])
				elif ctype == "瑞士法郎 (CHF)":
					return float(table.iat[6,3])
				elif ctype == "日圓 (JPY)":
					return float(table.iat[7,3])
				elif ctype == "南非幣 (ZAR)":
					return float(table.iat[8,3])
				elif ctype == "瑞典幣 (SEK)":
					return float(table.iat[9,3])
				elif ctype == "紐元 (NZD)":
					return float(table.iat[10,3])
				elif ctype == "泰幣 (THB)":
					return float(table.iat[11,3])
				elif ctype == "菲國比索 (PHP)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供菲律賓比索即期匯率買賣！")
				elif ctype == "印尼幣 (IDR)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供印尼幣即期匯率買賣！")
				elif ctype == "歐元 (EUR)":
					return float(table.iat[14,3])
				elif ctype == "韓元 (KRW)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供韓元即期匯率買賣！")
				elif ctype == "越南盾 (VND)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供越南盾即期匯率買賣！")
				elif ctype == "馬來幣 (MYR)":
					tkinter.messagebox.showerror(title = "無此服務", message = "很抱歉，目前臺灣銀行未提供馬來幣即期匯率買賣！")
				elif ctype == "人民幣 (CNY)":
					return float(table.iat[18,3])
			else: #本行賣出
				if ctype == "美金 (USD)":
					return float(table.iat[0,4])
				elif ctype == "港幣 (HKD)":
					return float(table.iat[1,4])
				elif ctype == "英鎊 (GBP)":
					return float(table.iat[2,4])
				elif ctype == "澳幣 (AUD)":
					return float(table.iat[3,4])
				elif ctype == "加拿大幣 (CAD)":
					return float(table.iat[4,4])
				elif ctype == "新加坡幣 (SGD)":
					return float(table.iat[5,4])
				elif ctype == "瑞士法郎 (CHF)":
					return float(table.iat[6,4])
				elif ctype == "日圓 (JPY)":
					return float(table.iat[7,4])
				elif ctype == "南非幣 (ZAR)":
					return float(table.iat[8,4])
				elif ctype == "瑞典幣 (SEK)":
					return float(table.iat[9,4])
				elif ctype == "紐元 (NZD)":
					return float(table.iat[10,4])
				elif ctype == "泰幣 (THB)":
					return float(table.iat[11,4])
				elif ctype == "菲國比索 (PHP)":
					return float(table.iat[12,4])
				elif ctype == "印尼幣 (IDR)":
					return float(table.iat[13,4])
				elif ctype == "歐元 (EUR)":
					return float(table.iat[14,4])
				elif ctype == "韓元 (KRW)":
					return float(table.iat[15,4])
				elif ctype == "越南盾 (VND)":
					return float(table.iat[16,4])
				elif ctype == "馬來幣 (MYR)":
					return float(table.iat[17,4])
				elif ctype == "人民幣 (CNY)":
					return float(table.iat[18,4])

	def holdToConvert(self, mode_cacuf1, currency_holdf1, currency_convertf1, amount_in):
		'''輸入持有貨幣，計算兌換貨幣'''
		if currency_holdf1 == "新臺幣 (NTD)" and currency_convertf1 != "新臺幣 (NTD)":
			cacu_in = mode_cacuf1
			buysell_in = "本行賣出"
			ctype_in = currency_convertf1
			exrate1 = self.getExrate(cacu_in, buysell_in, ctype_in)
			exrate2 = "－"
			amount_out = self.equation_1(amount_in, exrate1)
		elif currency_holdf1 != "新臺幣 (NTD)" and currency_convertf1 == "新臺幣 (NTD)":
			cacu_in = mode_cacuf1
			buysell_in = "本行買入"
			ctype_in = currency_holdf1
			exrate1 = self.getExrate(cacu_in, buysell_in, ctype_in)
			exrate2 = "－"
			amount_out = self.equation_2(amount_in, exrate1)
		elif currency_holdf1 != "新臺幣 (NTD)" and currency_convertf1 != "新臺幣 (NTD)" and (currency_holdf1 != currency_convertf1):
			cacu_in = mode_cacuf1
			buysell_in1 = "本行買入"
			ctype_in1 = currency_holdf1
			exrate1 = self.getExrate(cacu_in, buysell_in1, ctype_in1)
			buysell_in2 = "本行賣出"
			ctype_in2 = currency_convertf1
			exrate2 = self.getExrate(cacu_in, buysell_in2, ctype_in2)
			amount_out = self.equation_3(amount_in, exrate1, exrate2)
		elif currency_holdf1 == currency_convertf1:
			amount_out = amount_in
			exrate1 = "－"
			exrate2 = "－"
		return amount_out, exrate1, exrate2


	def convertToHold(self, mode_cacuf2, currency_holdf2, currency_convertf2, amount_in):
		'''輸入兌換貨幣，計算持有貨幣'''
		if currency_holdf2 == "新臺幣 (NTD)" and currency_convertf2 != "新臺幣 (NTD)":
			cacu_in = mode_cacuf2
			buysell_in = "本行賣出"
			ctype_in = currency_convertf2
			exrate1 = self.getExrate(cacu_in, buysell_in, ctype_in)
			exrate2 = "－"
			amount_out = self.equation_2(amount_in, exrate1)
		elif currency_holdf2 != "新臺幣 (NTD)" and currency_convertf2 == "新臺幣 (NTD)":
			cacu_in = mode_cacuf2
			buysell_in = "本行買入"
			ctype_in = currency_holdf2
			exrate1 = self.getExrate(cacu_in, buysell_in, ctype_in)
			exrate2 = "－"
			amount_out = self.equation_1(amount_in, exrate1)
		elif currency_holdf2 != "新臺幣 (NTD)" and currency_convertf2 != "新臺幣 (NTD)" and (currency_holdf2 != currency_convertf2):
			cacu_in = mode_cacuf2
			buysell_in1 = "本行賣出"
			ctype_in1 = currency_convertf2
			exrate1 = self.getExrate(cacu_in, buysell_in1, ctype_in1)
			buysell_in2 = "本行買入"
			ctype_in2 = currency_holdf2
			exrate2 = self.getExrate(cacu_in, buysell_in2, ctype_in2)
			amount_out = self.equation_3(amount_in, exrate1, exrate2)
		elif currency_holdf2 == currency_convertf2:
			amount_out = amount_in
			exrate = "－"
			exrate2 = "－"
		return amount_out, exrate1, exrate2


	def equation_1(self, amount_in1, exratef1):
		'''
		輸入持有貨幣: NTD(in) / 本行賣出 = fc(out)
		輸入兌換貨幣: NTD(in) / 本行買入 = fc(out)
		'''
		return (amount_in1 / exratef1)

	def equation_2(self, amount_in2, exratef2):
		'''
		輸入持有貨幣: fc(in) * 本行買入 = NTD(out)
		輸入兌換貨幣: fc(in) * 本行賣出 = NTD(out)
		'''
		return (amount_in2 * exratef2)

	def equation_3(self, amount_in3, exratef3, exratef4):
		'''
		輸入持有貨幣: fc(A)(in) * 本行買入 / 本行賣出 = fc(B)(out)
		輸入兌換貨幣: fc(B)(in) * 本行賣出 / 本行買入 = fc(A)(out)
		'''
		return (amount_in3 * exratef3 / exratef4)

	def clickBtn_convert(self):
		'''按鈕功能-試算'''
		mode_cacu = self.var1.get() #現金匯率or即期匯率
		mode_convert = self.var2.get() #持有<->兌換
		currency_hold = self.droplist1.get() #持有幣別
		currency_convert = self.droplist2.get() #兌換幣別

		#驗證輸入
		self.checkMode(mode_cacu, mode_convert, currency_hold, currency_convert) #檢驗有沒有選模式

		if mode_convert == "hold":
			checknum = self.txtlabel1.get("1.0", tk.END)
		else:
			checknum = self.txtlabel2.get("1.0", tk.END)
		num = self.checkNum(checknum) #驗證輸入的是否為數字
		self.rich(num) #是否為富豪

		#試算並輸出
		#金額
		if mode_convert == "hold":
			displaynum , exrate_1, exrate_2 = self.holdToConvert(mode_cacu, currency_hold, currency_convert, num) #持有換兌換
			self.txtlabel2.delete("1.0", tk.END)
			self.txtlabel2.insert("1.0", "%0.4f" %displaynum)
		else:
			displaynum , exrate_1, exrate_2 = self.convertToHold(mode_cacu, currency_hold, currency_convert, num) #兌換換持有
			self.txtlabel1.delete("1.0", tk.END)
			self.txtlabel1.insert("1.0", "%0.4f" %displaynum)
		#匯率
		self.labelname3.configure(text = "1：%0.5f" %exrate_1)
		if exrate_2 != "－":
			self.labelname5.configure(text = "1：%0.5f" %exrate_2)
		else:
			self.labelname5.configure(text = "－")

	def clickBtn_change(self):
		'''按鈕功能-互換'''
		if self.var2.get() == "hold":
			#改單選按鈕
			self.rbutton4.select()
			self.rbutton3.deselect()
			#改金額
			content = self.txtlabel1.get("1.0", tk.END)
			self.txtlabel2.delete("1.0", tk.END)
			self.txtlabel2.insert("1.0", content)
			self.txtlabel1.delete("1.0", tk.END)
			#清除匯率
			self.labelname3.configure(text = "")
			self.labelname5.configure(text = "")
			#改幣別
			hold_index = self.droplist1.current()
			convert_index = self.droplist2.current()
			self.droplist1.current(convert_index)
			self.droplist2.current(hold_index)
		else:
			#改單選按鈕
			self.rbutton3.select()
			self.rbutton4.deselect()
			#改金額
			content = self.txtlabel2.get("1.0", tk.END)
			self.txtlabel1.delete("1.0", tk.END)
			self.txtlabel1.insert("1.0", content)
			self.txtlabel2.delete("1.0", tk.END)
			#清除匯率
			self.labelname3.configure(text = "")
			self.labelname5.configure(text = "")
			#改幣別
			hold_index = self.droplist1.current()
			convert_index = self.droplist2.current()
			self.droplist1.current(convert_index)
			self.droplist2.current(hold_index)

	def clickBtn_clean(self):
		'''按鈕功能-清除'''
		self.txtlabel1.delete("1.0", tk.END)
		self.txtlabel2.delete("1.0", tk.END)
		self.labelname3.configure(text = "")
		self.labelname5.configure(text = "")
