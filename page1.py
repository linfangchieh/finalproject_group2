import tkinter as tk #視窗
import tkinter.font as tkFont #字體
import tkinter.ttk as tt #下拉選單
import pandas #爬的
import tkinter.messagebox #對話框
import matplotlib.pyplot as py #畫圖
import os
from PIL import ImageTk

class Page1(tk.Frame):
    exit1 = 0
    exit2 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.creatWidgets()

    def creatWidgets(self):
        '''建立元件'''
        #格式
        f1 = tkFont.Font(size = 15, family = "Consolas")
        f2 = tkFont.Font(size = 12, family = "微軟正黑體")
        f3 = tkFont.Font(size = 8, family = "微軟正黑體")
        f4 = tkFont.Font(size = 3, family = "微軟正黑體")
        f5 = tkFont.Font(size = 1, family = "微軟正黑體")
        '''物件'''
        #文字方塊-標題文字
        self.labelname = tk.Label(self, text = " **匯率查詢** ", height = 1, width = 10, font = f2)
        #文字方塊-幣別1
        self.labelname1_1 = tk.Label(self, text = " (必選)* ", height = 1, width = 5, font = f2, fg = "red")
        self.sublabel1 = tk.Label(self, text = " 現金匯率 ", height = 1, width = 10, font = f2)
        self.sublabel2 = tk.Label(self, text = " 即期匯率 ", height = 1, width = 10, font = f2)
        self.sublabel3 = tk.Label(self, text = " 銀行買入 ", height = 1, width = 10, font = f2)
        self.txtlabel1 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.txtlabel2 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.sublabel4 = tk.Label(self, text = " 銀行賣出 ", height = 1, width = 10, font = f2)
        self.txtlabel3 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.txtlabel4 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        #文字方塊-幣別2
        self.sublabel5 = tk.Label(self, text = " 現金匯率 ", height = 1, width = 10, font = f2)
        self.sublabel6 = tk.Label(self, text = " 即期匯率 ", height = 1, width = 10, font = f2)
        self.sublabel7 = tk.Label(self, text = " 銀行買入 ", height = 1, width = 10, font = f2)
        self.txtlabel5 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.txtlabel6 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.sublabel8 = tk.Label(self, text = " 銀行賣出 ", height = 1, width = 10, font = f2)
        self.txtlabel7 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        self.txtlabel8 = tk.Label(self, height = 1, width = 10, font = f2, bg = "white")
        #文字方塊-走勢圖
        self.figurename = tk.Label(self, text = " 近三個月匯率走勢圖 ", height = 1, width = 15, font = f2)
        self.lengendname1 = tk.Label(self, text = "現金匯率-銀行買入", fg = "DodgerBlue3")
        self.lengendname2 = tk.Label(self, text = "現金匯率-銀行賣出", fg = "dark orange")
        self.lengendname3 = tk.Label(self, text = "即期匯率-銀行買入", fg = "green4")
        self.lengendname4 = tk.Label(self, text = "即期匯率-銀行賣出", fg = "red3")
        self.cvsMain1 = tk.Canvas(self, width = 800, height = 400, bg = "white")
        self.cvsMain2 = tk.Canvas(self, width = 400, height = 200, bg = "white")
        #文字方塊-資料來源
        self.soursename = tk.Label(self, text = " 資料來源：臺灣銀行 ", height = 1, width = 15, font = f3)
        #文字方塊-空白行
        self.blank_r1 = tk.Label(self, height = 1, width = 1, font = f4)
        self.blank_r2 = tk.Label(self, height = 1, width = 1, font = f4)
        #文字方塊-空白欄
        self.blank_c1 = tk.Label(self, height = 1, width = 1, font = f4)
        self.blank_c2 = tk.Label(self, height = 1, width = 1, font = f4)
        #下拉選單-幣別1
        self.labelname1 = tk.Label(self, text = " 幣別 1： ", height = 1, width = 10, font = f2)
        self.droplist1 = tt.Combobox(self, width = 14, values = ["請選擇幣別1"," 美金 (USD) ", " 港幣 (HKD) ", " 英鎊 (GBP) ",
                                                                " 澳幣 (AUD) ", " 加拿大幣 (CAD) ", " 新加坡幣 (SGD) ",
                                                                " 瑞士法郎 (CHF) ", " 日圓 (JPY) ", " 南非幣 (ZAR) ",
                                                                " 瑞典幣 (SEK) ", " 紐元 (NZD) ", " 泰幣 (THB) ",
                                                                " 菲國比索 (PHP) ", " 印尼幣 (IDR) ", " 歐元 (EUR) ",
                                                                " 韓元 (KRW) ", " 越南盾 (VND) ", " 馬來幣 (MYR) ",
                                                                " 人民幣 (CNY) "], font = f2, state = "readonly")
        self.droplist1.current(0)
        #下拉選單-幣別2
        self.labelname2 = tk.Label(self, text = " 幣別 2： ", height = 1, width = 10, font = f2)
        self.droplist2 = tt.Combobox(self, width = 14, values = ["請選擇幣別2"," 美金 (USD) ", " 港幣 (HKD) ", " 英鎊 (GBP) ",
                                                                " 澳幣 (AUD) ", " 加拿大幣 (CAD) ", " 新加坡幣 (SGD) ",
                                                                " 瑞士法郎 (CHF) ", " 日圓 (JPY) ", " 南非幣 (ZAR) ",
                                                                " 瑞典幣 (SEK) ", " 紐元 (NZD) ", " 泰幣 (THB) ",
                                                                " 菲國比索 (PHP) ", " 印尼幣 (IDR) ", " 歐元 (EUR) ",
                                                                " 韓元 (KRW) ", " 越南盾 (VND) ", " 馬來幣 (MYR) ",
                                                                " 人民幣 (CNY) "],  font = f2, state = "readonly")
        self.droplist2.current(0)
        #按鈕
        self.btn = tk.Button(self, text = "查詢", height = 1, width = 8, font = f2, bg = "gold", command = self.clickBtn)

        '''位置'''
        self.labelname.grid(row = 0, column = 0, columnspan = 3, sticky = tk.NW) #查詢匯率

        self.labelname1.grid(row = 1, column = 0,columnspan = 1, sticky = tk.NW) #幣別1選單
        self.droplist1.grid(row = 1, column = 1, columnspan = 1, sticky = tk.NW)
        self.blank_c1.grid(row = 1, column = 4) #空欄
        self.labelname1_1.grid(row = 1, column = 3,columnspan = 1, sticky = tk.NW)
        self.sublabel1.grid(row = 2, column = 1, columnspan = 1, sticky = tk.NW) #幣別1-現金匯率
        self.sublabel2.grid(row = 2, column = 3, columnspan = 1, sticky = tk.NW) #幣別1-即期匯率
        self.sublabel3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.NW) #幣別1-銀行買入
        self.txtlabel1.grid(row = 3, column = 1, columnspan = 1, sticky = tk.NW) #幣別1-現金買入
        self.txtlabel2.grid(row = 3, column = 3, columnspan = 1, sticky = tk.NW) #幣別1-即期買入
        self.blank_r1.grid(row = 4, column = 0) #空行
        self.sublabel4.grid(row = 5, column = 0, columnspan = 1, sticky = tk.NW) #幣別1-銀行賣出
        self.txtlabel3.grid(row = 5, column = 1, columnspan = 1, sticky = tk.NW) #幣別1-現金賣出
        self.txtlabel4.grid(row = 5, column = 3, columnspan = 1, sticky = tk.NW) #幣別1-即期賣出
        self.blank_r2.grid(row = 6, column = 0) #空行

        self.labelname2.grid(row = 1, column = 5,columnspan = 1, sticky = tk.NW) #幣別2選單
        self.droplist2.grid(row = 1, column = 6, columnspan = 1, sticky = tk.NW)
        self.blank_c2.grid(row = 1, column = 10) #空欄
        self.sublabel5.grid(row = 2, column = 6, columnspan = 1, sticky = tk.NW) #幣別2-現金匯率
        self.sublabel6.grid(row = 2, column = 9, columnspan = 1, sticky = tk.NW) #幣別2-即期匯率
        self.sublabel7.grid(row = 3, column = 5, columnspan = 1, sticky = tk.NW) #幣別2-銀行買入
        self.txtlabel5.grid(row = 3, column = 6, columnspan = 1, sticky = tk.NW) #幣別2-現金買入
        self.txtlabel6.grid(row = 3, column = 9, columnspan = 1, sticky = tk.NW) #幣別2-即期買入
        self.sublabel8.grid(row = 5, column = 5, columnspan = 1, sticky = tk.NW) #幣別2-銀行賣出
        self.txtlabel7.grid(row = 5, column = 6, columnspan = 1, sticky = tk.NW) #幣別2-現金賣出
        self.txtlabel8.grid(row = 5, column = 9, columnspan = 1, sticky = tk.NW) #幣別2-即期賣出

        self.btn.grid(row = 1, column = 9, columnspan = 1) #按鍵

        self.figurename.grid(row = 7, column = 0, columnspan = 5, sticky = tk.W) #近三個月匯率走勢圖
        self.lengendname1.grid(row = 8, column = 0, columnspan = 2, sticky = tk.W) #現金匯率-銀行買入
        self.lengendname2.grid(row = 8, column = 1, columnspan = 2, sticky = tk.W) #現金匯率-銀行賣出
        self.lengendname3.grid(row = 8, column = 3, columnspan = 2, sticky = tk.W) #即期匯率-銀行買入
        self.lengendname4.grid(row = 8, column = 4, columnspan = 2, sticky = tk.W) #即期匯率-銀行賣出
        self.cvsMain1.grid(row = 9, column = 0, rowspan = 20, columnspan = 10, sticky = tk.NE + tk.SW)
        self.cvsMain2.grid(row = 9, column = 5, rowspan = 20, columnspan = 10, sticky = tk.NE + tk.SW)

        self.soursename.grid(row = 30, column = 0, columnspan = 25, sticky = tk.E) #資料來源

    def bank(self):
        '''讀取匯率頁面'''
        dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
        table = dfs[0]
        return table

    def currency(self, currencyName, ftable):
        '''讀取幣別之匯率資料'''
        if currencyName == " 美金 (USD) ":
            table_rowf = ftable.iloc[0,0:5]
        elif currencyName == " 港幣 (HKD) ":
            table_rowf = ftable.iloc[1,0:5]
        elif currencyName == " 英鎊 (GBP) ":
            table_rowf = ftable.iloc[2,0:5]
        elif currencyName == " 澳幣 (AUD) ":
            table_rowf = ftable.iloc[3,0:5]
        elif currencyName == " 加拿大幣 (CAD) ":
            table_rowf = ftable.iloc[4,0:5]
        elif currencyName == " 新加坡幣 (SGD) ":
            table_rowf = ftable.iloc[5,0:5]
        elif currencyName == " 瑞士法郎 (CHF) ":
            table_rowf = ftable.iloc[6,0:5]
        elif currencyName == " 日圓 (JPY) ":
            table_rowf = ftable.iloc[7,0:5]
        elif currencyName == " 南非幣 (ZAR) ":
            table_rowf = ftable.iloc[8,0:5]
        elif currencyName == " 瑞典幣 (SEK) ":
            table_rowf = ftable.iloc[9,0:5]
        elif currencyName ==  " 紐元 (NZD) ":
            table_rowf = ftable.iloc[10,0:5]
        elif currencyName == " 泰幣 (THB) ":
            table_rowf = ftable.iloc[11,0:5]
        elif currencyName == " 菲國比索 (PHP) ":
            table_rowf = ftable.iloc[12,0:5]
        elif currencyName == " 印尼幣 (IDR) ":
            table_rowf = ftable.iloc[13,0:5]
        elif currencyName == " 歐元 (EUR) ":
            table_rowf = ftable.iloc[14,0:5]
        elif currencyName == " 韓元 (KRW) ":
            table_rowf = ftable.iloc[15,0:5]
        elif currencyName == " 越南盾 (VND) ":
            table_rowf = ftable.iloc[16,0:5]
        elif currencyName == " 馬來幣 (MYR) ":
            table_rowf = ftable.iloc[17,0:5]
        elif currencyName == " 人民幣 (CNY) ":
            table_rowf = ftable.iloc[18,0:5]
        return table_rowf

    def type(self, ftable1):
        table_col_1 = ftable1.iat[1] #現金匯率-本行買入
        table_col_2 = ftable1.iat[3] #即期匯率-本行買入
        table_col_3 = ftable1.iat[2] #現金匯率-本行賣出
        table_col_4 = ftable1.iat[4] #即期匯率-本行賣出
        return table_col_1, table_col_2, table_col_3, table_col_4

    def makeLinechart(self, money, picturename):
        self.picturename = str(picturename)
        py.figure()
        self.money = money
        print(self.money)
        dfs = pandas.read_html("https://rate.bot.com.tw/xrt/quote/ltm/" + self.money)
        money = dfs[0]
        money = money.iloc[:, 0:6]
        money.columns = ["Quoted Date", "Currency", "Cash Rate - Buying", "Cash Rate - Selling",
                         "Spot Rate - Buying", "Spot Rate - Selling"]
        money["Currency"] = money["Currency"].str.extract("\((\w+)\)")    #https://ithelp.ithome.com.tw/articles/10194954

        x = sorted(money["Quoted Date"].tolist())[-1:: -10]
        x = x[:: -1]
        '''
        for t in range(len(x)):
            y = x[t]
            x[t] = y[5:]
        '''

        money.sort_values("Quoted Date") #把資料按照時間排序

        date_list = money["Quoted Date"]
        cashbuy_list = money["Cash Rate - Buying"]
        cashsell_list = money["Cash Rate - Selling"]
        spotbuy_list = money["Spot Rate - Buying"]
        spotsell_list = money["Spot Rate - Selling"]

        py.plot(date_list, cashbuy_list)
        py.plot(date_list, cashsell_list)
        py.plot(date_list, spotbuy_list)
        py.plot(date_list, spotsell_list)

        # py.tight_layout()

        py.xlabel("Date")
        py.xticks(rotation=270)
        py.ylabel("Cash Rate")
        py.xticks(x)
        py.tight_layout()
        py.savefig(self.picturename + ".png")

    def clickBtn(self):
        '''按鈕功能-顯示匯率'''
        if self.droplist1.get() == "請選擇幣別1": #沒選幣別1，跳警示
            self.txtlabel1.configure(text = "")
            self.txtlabel2.configure(text = "")
            self.txtlabel3.configure(text = "")
            self.txtlabel4.configure(text = "")
            self.txtlabel5.configure(text = "")
            self.txtlabel6.configure(text = "")
            self.txtlabel7.configure(text = "")
            self.txtlabel8.configure(text = "")
            tkinter.messagebox.showerror(title = "未選擇模式", message = "沒選擇幣別1啦!")

        else:
            table_web = self.bank()
            currency1_choose  =  self.droplist1.get() #幣別1
            table_row1 = self.currency(currency1_choose, table_web)
            table_column_1 = self.type(table_row1)
            content1 = table_column_1
            self.txtlabel1.configure(text = content1[0])
            self.txtlabel2.configure(text = content1[1])
            self.txtlabel3.configure(text = content1[2])
            self.txtlabel4.configure(text = content1[3])

            if self.droplist2.get() != "請選擇幣別2":
                if self.droplist1.get() == self.droplist2.get(): #如果幣別1=幣別2，跳警示
                    self.txtlabel5.configure(text = "")
                    self.txtlabel6.configure(text = "")
                    self.txtlabel7.configure(text = "")
                    self.txtlabel8.configure(text = "")
                    tkinter.messagebox.showerror(title = "Oh Oh!!", message = "幣別1跟幣別2一樣耶!")
                else:
                    currency2_choose =  self.droplist2.get() #幣別2
                    table_row2 = self.currency(currency2_choose, table_web)
                    table_column_2 = self.type(table_row2)
                    content2 = table_column_2
                    self.txtlabel5.configure(text = content2[0])
                    self.txtlabel6.configure(text = content2[1])
                    self.txtlabel7.configure(text = content2[2])
                    self.txtlabel8.configure(text = content2[3])
            else:
                self.txtlabel5.configure(text = "")
                self.txtlabel6.configure(text = "")
                self.txtlabel7.configure(text = "")
                self.txtlabel8.configure(text = "")

        '''按鈕功能-顯示匯率走勢圖'''
        '''幣別1'''
        if self.droplist1.get() != "請選擇幣別1":
            picture = "line1"
            if self.exit1 == 0:
                self.exit1 = 1
            elif self.exit1 == 1:
                self.cvsMain1.delete(self.image1)

            money1 = self.droplist1.get()[-3: -6: -1][::-1]
            self.makeLinechart(money1, picture)

            self.imageMain1 = ImageTk.PhotoImage(file = picture + ".png")
            self.image1 = self.cvsMain1.create_image(200, 200, image = self.imageMain1)
            os.system("del line1.png")

        else:
            if self.exit1 != 0 and self.exit2 == 0:
                self.cvsMain1.delete(self.image1)
                print(1)
            elif self.exit1 != 0 and self.exit2 != 0:
                self.cvsMain1.delete(self.image1)
                self.cvsMain2.delete(self.image2)
                print(2)
            #if self.exit1 == 0 and self.exit2 == 0:
                #不做任何事
            elif self.exit1 == 0 and self.exit2 != 0:
                self.cvsMain2.delete(self.image2)


        '''幣別2'''
        if (self.droplist2.get() != "請選擇幣別2") and (self.droplist2.get() != self.droplist1.get()) and (self.droplist1.get() != "請選擇幣別1"):
            picture = "line2"
            if self.exit2 == 0:
                self.exit2 = 1
            elif self.exit2 == 1:
                self.cvsMain2.delete(self.image2)

            money2 = self.droplist2.get()[-3: -6: -1][::-1]
            self.makeLinechart(money2, picture)

            self.imageMain2 = ImageTk.PhotoImage(file = picture + ".png")
            self.image2 = self.cvsMain2.create_image(200, 200, image = self.imageMain2)
            os.system("del line1.png")

        elif (self.droplist2.get() != "請選擇幣別2") and (self.droplist2.get() == self.droplist1.get()):
            self.cvsMain2.delete(self.image2)

        elif (self.droplist2.get() == "請選擇幣別2"):
            if self.exit2 != 0:
                self.cvsMain2.delete(self.image2)