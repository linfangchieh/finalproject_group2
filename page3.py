import tkinter as tk #視窗
import tkinter.font as tkFont #字體
import tkinter.ttk as tt #下拉選單

import tkinter.messagebox #對話框

#為了連結至gmail申請頁面而import的package
import webbrowser

#為了寄信而import的package
import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.text import MIMEText

#儲存抓取的匯率資料
import sqlite3


class Page3(tk.Frame):

	def __init__(self, parent, controller):
		'''建立物件時一定要做的事'''
		tk.Frame.__init__(self, parent)
		self.creatWidgets()

	def creatWidgets(self):

		def callback(url):
			webbrowser.open_new(url)

		#設定格式(f1)
		f1 = tkFont.Font(size = 14, family = "微軟正黑體", weight=tkFont.BOLD)
		f2 = tkFont.Font(size = 16, family = "Consolas", weight=tkFont.BOLD, underline=2)

		#設定第一部分：輸入Gmail的資訊，並設定相關位置
		self.firstpart1 = tk.Label(self, text = "輸入您的Gmail：", height = 1, width = 15, font = f1)
		self.firstpart2 = tk.Text(self, height = 1, width = 40, font = f1)
		self.firstpart3 = tk.Label(self, text = "@gmail.com", font = f1)
		self.firstpart4 = tk.Label(self, height = 1, width = 15, font = f1) #排版用
		self.firstpart1.grid(row = 0, column = 0, columnspan = 1)
		self.firstpart2.grid(row = 0, column = 1, columnspan = 2, sticky = tk.W)
		self.firstpart3.grid(row = 0, column = 3, columnspan = 1, sticky = tk.W)
		self.firstpart4.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W)
		
		#設定第二部分：輸入目標幣別，並設定相關位置
		self.secondpart1 = tk.Label(self, text = "目標幣別：", height = 1, width = 15, font = f1)
		self.secondpart2 = tt.Combobox(self,  values = [" 美金 (USD) ", " 港幣 (HKD) ", " 英鎊 (GBP) ",
														" 澳幣 (AUD) ", " 加拿大幣 (CAD) ", " 新加坡幣 (SGD) ",
														" 瑞士法郎 (CHF) ", " 日圓 (JPY) ", " 南非幣 (ZAR) ",
														" 瑞典幣 (SEK) ", " 紐元 (NZD) ", " 泰幣 (THB) ",
														" 菲國比索 (PHP) ", " 印尼幣 (IDR) ", " 歐元 (EUR) ",
														" 韓元 (KRW) ", " 越南盾 (VND) ", " 馬來幣 (MYR) ",
														" 人民幣 (CNY) "], height = 10, width = 40, font = f1)		
		self.secondpart3 = tk.Label(self, height = 1, width = 15, font = f1) #排版用
		self.secondpart1.grid(row = 2, column = 0, columnspan = 1)
		self.secondpart2.grid(row = 2, column = 1, columnspan = 2)
		self.secondpart3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W)

		#設定第三部分：設定匯率種類，並設定相關位置
		self.CashBuy = tk.IntVar()
		self.CashSell = tk.IntVar()
		self.CurrBuy = tk.IntVar()
		self.CurrSell = tk.IntVar()

		self.thirdpart1 = tk.Label(self, text = "匯率種類：", height = 1, width = 15, font = f1)
		self.thirdpart2 = tk.Checkbutton(self, text = "現金匯率－銀行買入", variable = self.CashBuy,
										 onvalue=1, offvalue=0, height = 1, width = 15, font = f1, fg = "DodgerBlue3")
		self.thirdpart3 = tk.Checkbutton(self, text = "現金匯率－銀行賣出", variable = self.CashSell,
										 onvalue=1, offvalue=0, height = 1, width = 15, font = f1, fg = "dark orange")
		self.thirdpart4 = tk.Checkbutton(self, text = "即期匯率－銀行買入", variable = self.CurrBuy,
										 onvalue=1, offvalue=0, height = 1, width = 15, font = f1, fg = "green4")
		self.thirdpart5 = tk.Checkbutton(self, text = "即期匯率－銀行賣出", variable = self.CurrSell,
										 onvalue=1, offvalue=0, height = 1, width = 15, font = f1, fg = "red3")
		self.thirdpart6 = tk.Label(self, height = 1, width = 15, font = f1) #排版用

		self.thirdpart1.grid(row = 4, column = 0, columnspan = 1)
		self.thirdpart2.grid(row = 4, column = 1, columnspan = 1, sticky = tk.W)
		self.thirdpart3.grid(row = 4, column = 2, columnspan = 1, sticky = tk.W)
		self.thirdpart4.grid(row = 5, column = 1, columnspan = 1, sticky = tk.W)
		self.thirdpart5.grid(row = 5, column = 2, columnspan = 1, sticky = tk.W)
		self.secondpart3.grid(row = 6, column = 0, columnspan = 1, sticky = tk.W)

		#設定第四部分：說明文字，並設定相關位置
		self.fourthpart1 = tk.Label(self, text = "請在下方輸入希望低於或高於之價格", font = f1)
		self.fourthpart2 = tk.Label(self, text = "(至少要填一個！)", font = f1, fg = "red")
		self.fourthpart1.grid(row = 7, column = 0, columnspan = 2)
		self.fourthpart2.grid(row = 7, column = 2, columnspan = 2, sticky = tk.W)

		#設定第五部分：輸入目標價格(最低價)，並設定相關位置
		self.fifthpart1 = tk.Label(self, text = "希望價格低於：", height = 1, width = 12, font = f1)
		self.fifthpart2 = tk.Text(self, height = 1, width = 40, font = f1)
		self.fifthpart1.grid(row = 8, column = 0, columnspan = 1)
		self.fifthpart2.grid(row = 8, column = 1, columnspan = 3, sticky = tk.W)

		#設定第六部分：輸入目標價格(最高價)，並設定相關位置
		self.sixthpart1 = tk.Label(self, text = "希望價格高於：", height = 1, width = 12, font = f1)
		self.sixthpart2 = tk.Text(self, height = 1, width = 40, font = f1)
		self.sixthpart3 = tk.Label(self, height = 1, width = 15, font = f1) #排版用
		self.sixthpart1.grid(row = 9, column = 0, columnspan = 1)
		self.sixthpart2.grid(row = 9, column = 1, columnspan = 3, sticky = tk.W)
		self.sixthpart3.grid(row = 10, column = 0, columnspan = 1, sticky = tk.W)

		#設定第七部分：送出資料及取得驗證信，並設定相關位置
		self.seventhpart1 = tk.Button(self, text = "確認送出", command = self.clickseventhpart, height = 1, width = 22, font = f1, bg = "gold")
		self.seventhpart1.grid(row = 11, column = 0, columnspan = 4)	

		#設定第八部分：說明文字，並設定相關位置
		self.eighthpart1 = tk.Label(self, text = "請去信箱確認認證信，如5分鐘內未收到請重新輸入", font = f1)
		self.eighthpart1.grid(row = 12, column = 0, columnspan = 4)

		#設定第九部分：連結至Gmail申請頁，並設定相關位置
		self.ninthpart1 = tk.Label(self, text="還沒有Gmail嗎?快點這裡申請!", fg="blue", cursor="hand2", font = f1)
		self.ninthpart1.grid(row = 13, column = 0, columnspan = 4)
		self.ninthpart1.bind("<Button-1>",
							 lambda e: callback("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"))
		self.ninthpart2 = tk.Label(self, height = 1, width = 15, font = f1) #排版用
		self.ninthpart2.grid(row = 14, column = 0, columnspan = 1, sticky = tk.W)

		#設定第十部分：注意事項，並設定相關位置
		self.tenthpart1 = tk.Label(self, text = "確認送出前請先確認：", font = f2, fg = "orangered")
		self.tenthpart2 = tk.Label(self, text = '1. 僅需輸入Gmail帳號，"@gmail.com"是不需要的', font = f1)
		self.tenthpart3 = tk.Label(self, text = '2. 目標幣別一定要選，別忘了喔~', font = f1)
		self.tenthpart4 = tk.Label(self, text = '3. 匯率種類至少要選一個喔！', font = f1)
		self.tenthpart5 = tk.Label(self, text = '4. "希望低於或高於之價格"至少要填一個喔！且僅限阿拉伯數字！(有小數點是ok的~)', font = f1)
		self.tenthpart1.grid(row = 15, column = 0, columnspan = 4, sticky = tk.W)
		self.tenthpart2.grid(row = 16, column = 0, columnspan = 4, sticky = tk.W)
		self.tenthpart3.grid(row = 17, column = 0, columnspan = 4, sticky = tk.W)
		self.tenthpart4.grid(row = 18, column = 0, columnspan = 4, sticky = tk.W)
		self.tenthpart5.grid(row = 19, column = 0, columnspan = 4, sticky = tk.W)

	#定義按鈕
	def clickseventhpart(self):
		data = []
		gmail_test = str(self.firstpart2.get("1.0", tk.END))[0:-1]
		break_ruls = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","{","[","]","}",
					"\\","|",";",":","'","\"","<",",",">",".","?","/","\t","\r","\n"," "]
		#先檢測是否有填入Gmail
		#若沒有填Gmail，則跳出警示視窗
		if len(str(self.firstpart2.get("1.0", tk.END))) == 1:
			tkinter.messagebox.showinfo(title='Ooooooops!', message='要寫一下Gmail帳號啦!')
			return None
		#若有輸入Gmail，則檢測是否僅輸入Gmail帳號(也就是沒有輸入@gmail.com)
		else:
			if len(gmail_test) >= 10 and gmail_test[-10] == "@":
				tkinter.messagebox.showinfo(title='Ooooooops!', message='嗯...Gmail輸入的資訊可能要修正喔！只要填入帳號，不用填寫"@gmail.com"')
				return None
			#若僅輸入Gmail帳號，則檢測是否輸入符合帳號規格
			else:
				gmail_test_result = 0
				for j in range(len(gmail_test)):
					for k in range(len(break_ruls)):
						if gmail_test[j] == break_ruls[k]:
							gmail_test_result += 1
							break
				if gmail_test_result != 0:
					tkinter.messagebox.showinfo(title='Ooooooops!', message='嗯...Gmail輸入的資訊可能要修正喔！亂碼或空格是無法辨識的...')
					return None
				#若Gmail輸入正確，則檢測是否有選擇幣別
				else:
					#若沒選擇幣別，則跳出警示視窗
					if self.secondpart2.get() == "" :
						tkinter.messagebox.showinfo(title='Ooooooops!', message='選一下目標幣別啦!')
						return None
					#若有選擇幣別，則檢測是否有選擇匯率種類
					else:
						#若沒選擇匯率種類，則跳出警示視窗
						if self.CashBuy.get() == 0 and self.CashSell.get() == 0 and self.CurrBuy.get() == 0 and self.CurrSell.get() == 0:
							tkinter.messagebox.showinfo(title='Ooooooops!', message='拜託你選一下匯率種類好嗎?')
							return None
						#若有選擇幣別，則檢測是否有輸入最低價或最高價
						else:
							#若沒有填最低或最高價，則跳出警示視窗
							if len(str(self.fifthpart2.get("1.0", tk.END))) == 1 and len(str(self.sixthpart2.get("1.0", tk.END))) == 1:
								tkinter.messagebox.showinfo(title='Ooooooops!', message='求求你填一下最高價或最低價好嗎?')
								return None
							#確認輸入的最高、最低價為數字
							if len(str(self.fifthpart2.get("1.0", tk.END))) != 1 and len(str(self.sixthpart2.get("1.0", tk.END))) == 1:
								try: # check for valid number
									input_number = float(self.fifthpart2.get("1.0", tk.END))
								except:
									tkinter.messagebox.showinfo(title='Ooooooops!', message='我只看得懂阿拉伯數字啦！')
									return None
							elif len(str(self.fifthpart2.get("1.0", tk.END))) == 1 and len(str(self.sixthpart2.get("1.0", tk.END))) != 1:
								try: # check for valid number
									input_number = float(self.sixthpart2.get("1.0", tk.END))
								except:
									tkinter.messagebox.showinfo(title='Ooooooops!', message='我只看得懂阿拉伯數字啦！')
									return None
							else :
								try: 
									input_number = float(self.sixthpart2.get("1.0", tk.END))
									input_number = float(self.fifthpart2.get("1.0", tk.END))
								except:
									tkinter.messagebox.showinfo(title='Ooooooops!', message='我只看得懂阿拉伯數字啦！')
									return None
		#若該填的都有填，則執行以下code
		user_mail = str(self.firstpart2.get("1.0", tk.END))  #擷取使用者輸入之Gmail帳號
		mail_word_currency = str(self.secondpart2.get())     #擷取使用者選取之目標幣別
		mail_word_lowest = str(self.fifthpart2.get("1.0", tk.END))  #擷取使用者輸入之最低價格
		mail_word_highest = str(self.sixthpart2.get("1.0", tk.END))  #擷取使用者輸入之最高價格

		#將使用者選取之目標幣別進行轉換，因第一個及最後一個字會為空白或分隔，因而取第二個至倒數第二個字
		name_currency = mail_word_currency[1:len(mail_word_currency)-1]
		
		#將使用者選取之匯率種類進行轉換
		name_type_original = []

		if self.CashBuy.get() == 1:
			name_type_original.append("現金匯率－銀行買入")
			type_CashBuy = "1"
		else:
			type_CashBuy = "0"

		if self.CashSell.get() == 1:
			name_type_original.append("現金匯率－銀行賣出")
			type_CashSell = "1"
		else:
			type_CashSell = "0"

		if self.CurrBuy.get() == 1:
			name_type_original.append("即期匯率－銀行買入")
			type_CurrBuy = "1"
		else:
			type_CurrBuy = "0"

		if self.CurrSell.get() == 1:
			name_type_original.append("即期匯率－銀行賣出")
			type_CurrSell = "1"
		else:
			type_CurrSell = "0"

		name_type = "、".join(name_type_original)

		#將使用者輸入之最低價進行轉換，因最後一個字會為空白或分隔，因而取第一個至倒數第二個字
		name_lowest = mail_word_lowest[0:len(mail_word_lowest)-1]
		if len(mail_word_lowest) == 1:
			name_lowest = "無填寫"

		#將使用者輸入之最高價進行轉換，因最後一個字會為空白或分隔，因而取第一個至倒數第二個字
		name_highest = mail_word_highest[0:len(mail_word_highest)-1]
		if len(mail_word_highest) == 1:
			name_highest = "無填寫"

		#設立發信的電子郵件地址
		fromaddr = "r07pythonfinal@gmail.com"

		#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
		toaddr = (user_mail[0:len(user_mail)-1] + "@gmail.com")

		msg = MIMEMultipart()
		mail_title = "換匯資訊認證信"  #信件標題
		msg['Subject'] = mail_title
		msg['From'] = fromaddr
		msg['To'] = toaddr

		body = MIMEText(u"Hello!\n\n收到此封信表示我們已收到您輸入的資訊！" 
			+ "\n\n\t幣別：" + name_currency
			+ "\n\n\t匯率種類：" + str(name_type)
			+ "\n\n\t希望價格低於：" + str(name_lowest) 
			+ "\n\n\t希望價格高於：" + str(name_highest) 
			+ "\n\n希望近期就能出現您希望的匯率～\n\n製作團隊敬上", 'plain', 'utf-8') 
		msg.attach(body)

		try:
			stmp = smtplib.SMTP('smtp.gmail.com', 587)
			stmp.ehlo()
			stmp.starttls()
			stmp.login(fromaddr, "r07722027")
			stmp.sendmail(fromaddr, toaddr, msg.as_string())
			stmp.close()
			tkinter.messagebox.showinfo(title='OH!YES!', message='快去信箱收一下認證信吧!')

		except Exception as e:
			tkinter.messagebox.showinfo(title='Ooooooops!', message='某個環節好像出錯了...請稍後再試...')
			stmp.close()
			return None
		data.append(user_mail.strip())
		data.append(mail_word_currency.strip())
		data.append(type_CashBuy.strip())
		data.append(type_CashSell.strip())
		data.append(type_CurrBuy.strip())
		data.append(type_CurrSell.strip())
		data.append(mail_word_lowest.strip())
		data.append(mail_word_highest.strip())

		fileObject = open('sampleList.txt', 'w')
		for d in data:
			if d == data[-1] :
				fileObject.write(d)
			else :	
				fileObject.write(d)
				fileObject.write(',')
		fileObject.close()

