import pandas
import sqlite3

#為了連結至gmail申請頁面而import的package
import webbrowser

#為了寄信而import的package
import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.text import MIMEText

#打開電腦裡面儲存使用者輸入的資料
fileObject = open('sampleList.txt', 'r')
user_input = fileObject.read()
user_input = user_input.strip()
user_input = user_input.split(',')
user_email = user_input[0] #Gmail帳號
user_currency = user_input[1] #選擇之幣別
user_CashBuy = user_input[2] #是否有勾現金買入匯率(1:有；0:沒有)
user_CashSell = user_input[3] #是否有勾現金賣出匯率(1:有；0:沒有)
user_CurrBuy = user_input[4] #是否有勾即期買入匯率(1:有；0:沒有)
user_CurrSell = user_input[5] #是否有勾即期賣出匯率(1:有；0:沒有)
user_low = user_input[6] #希望價格低於...
user_high = user_input[7] #希望價格高於...

if user_low == '' :
	user_low = 0
elif user_low == '-' :
	user_low = 0 
else :
	user_low = float(user_low)
if user_high == '' :
	user_high = 100000
elif user_high == '-' :
	user_high = 100000 
else :
	user_high = float(user_high)

#抓取台銀匯率資料
dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
table = dfs[0]

currency = table.iloc[:,0:5]

currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')

#將抓取的資料存取至電腦
with sqlite3.connect('currency.sqlite') as db :
	currency.to_sql('currency',con = db, if_exists='replace')

#讀取所存取的資料
with sqlite3.connect('currency.sqlite') as db :
	table = pandas.read_sql_query('select * from currency',con = db )		

target_currency_name = user_currency

#設定要出現在信件中的當期匯率的值
currency_list = ["美金 (USD)", "港幣 (HKD)", "英鎊 (GBP)",
				"澳幣 (AUD)", "加拿大幣 (CAD)", "新加坡幣 (SGD)",
				"瑞士法郎 (CHF)", "日圓 (JPY)", "南非幣 (ZAR)",
				"瑞典幣 (SEK)", "紐元 (NZD)", "泰幣 (THB)",
				"菲國比索 (PHP)", "印尼幣 (IDR)", "歐元 (EUR)",
				"韓元 (KRW)", "越南盾 (VND)", "馬來幣 (MYR)",
				"人民幣 (CNY)"]

for i in range(len(currency_list)):
	if target_currency_name == currency_list[i]:
		#若選擇之幣別為南非幣，則僅即期匯率有值
		if i == 8: 
			user_currency_cashbuy = "－"
			user_currency_cashsell = "－"
			user_currency_currbuy = float(table.iloc[i,4])
			user_currency_currsell = float(table.iloc[i,5])
		#若選擇之幣別為菲國比索、印尼幣、韓元、越南盾、馬來幣，則僅現金匯率有值
		elif i == 12 or i == 13 or i == 15 or i ==16 or i == 17:
			user_currency_cashbuy = float(table.iloc[i,2])
			user_currency_cashsell = float(table.iloc[i,3])
			user_currency_currbuy = "－"
			user_currency_currsell = "－"
		#若選擇之幣別非為上述之貨幣，則現金及即期匯率均有值
		else:
			user_currency_cashbuy = float(table.iloc[i,2])
			user_currency_cashsell = float(table.iloc[i,3])
			user_currency_currbuy = float(table.iloc[i,4])
			user_currency_currsell = float(table.iloc[i,5])

#定義：匯率(現金匯率－銀行買入)到達設定低點時寄的郵件
def send_email_low_cashbuy() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'
	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(現金匯率－銀行買入)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	for i in range(len(currency_list)):
		if target_currency_name == currency_list[i]:
			user_currency_cashbuy = float(table.iloc[i,2])

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(現金匯率－銀行買入)已經低於新台幣' + str(user_low) + '元囉!'
		'\n\n目前的匯率(現金匯率－銀行買入)為：' + str(user_currency_cashbuy) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8') 
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

def send_email_high_cashbuy() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'

	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(現金匯率－銀行買入)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(現金匯率－銀行買入)已經高於新台幣' + str(user_high) + '元囉!'
		'\n\n目前的匯率(現金匯率－銀行買入)為：' + str(user_currency_cashbuy) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8') 
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

#定義：匯率(現金匯率－銀行賣出)到達設定低點時寄的郵件
def send_email_low_cashsell() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'
	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(現金匯率－銀行賣出)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(現金匯率－銀行賣出)已經低於新台幣' + str(user_low) + '元囉!'
		'\n\n目前的匯率(現金匯率－銀行賣出)為：' + str(user_currency_cashsell) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8') 
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

def send_email_high_cashsell() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'

	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(現金匯率－銀行賣出)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(現金匯率－銀行賣出)已經高於新台幣' + str(user_high) + '元囉!'
		'\n\n目前的匯率(現金匯率－銀行賣出)為：' + str(user_currency_cashsell) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8') 
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

#定義：匯率(即期匯率－銀行買入)到達設定低點時寄的郵件
def send_email_low_currbuy() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'
	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(即期匯率－銀行買入)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(即期匯率－銀行買入)已經低於新台幣' + str(user_low) + '元囉!'
		'\n\n目前的匯率(即期匯率－銀行買入)為：' + str(user_currency_currbuy) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8')
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

def send_email_high_currbuy() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'

	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(即期匯率－銀行買入)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(即期匯率－銀行買入)已經高於新台幣' + str(user_high) + '元囉!'
		'\n\n目前的匯率(即期匯率－銀行買入)為：' + str(user_currency_currbuy) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8')
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

#定義：匯率(即期匯率－銀行賣出)到達設定低點時寄的郵件
def send_email_low_currsell() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'
	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(即期匯率－銀行賣出)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(即期匯率－銀行賣出)已經低於新台幣' + str(user_low) + '元囉!'
		'\n\n目前的匯率(即期匯率－銀行賣出)為：' + str(user_currency_currsell) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8')
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()

def send_email_high_currsell() :
	fromaddr = "r07pythonfinal@gmail.com"

	#設立收信的電子郵件地址，亦為使用者自行輸入之Gmail帳號，又因擷取出的Gmail帳號的最後一個字會為空白或分隔，因此取第一個至倒數第二個字
	toaddr = user_email+'@gmail.com'

	msg = MIMEMultipart()
	mail_title = '您觀望的' +user_currency+'匯率(即期匯率－銀行賣出)已達標囉!'  #信件標題
	msg['Subject'] = mail_title
	msg['From'] = fromaddr
	msg['To'] = toaddr

	body = MIMEText(u"Hello!" 
		'\n\n您觀望的' + user_currency + '匯率(即期匯率－銀行賣出)已經高於新台幣' + str(user_high) + '元囉!'
		'\n\n目前的匯率(即期匯率－銀行賣出)為：' + str(user_currency_currsell) + '\n\n趕快下單吧!\n\n製作團隊敬上', 'plain', 'utf-8')
	msg.attach(body)

	stmp = smtplib.SMTP('smtp.gmail.com', 587)
	stmp.ehlo()
	stmp.starttls()
	stmp.login(fromaddr, "r07722027")
	stmp.sendmail(fromaddr, toaddr, msg.as_string())
	stmp.close()


#若使用者有勾選現金匯率－銀行買入，則依其設定之標準寄信
if user_CashBuy == "1":
	if target_currency_name == "美金 (USD)":
		if float(table.iloc[0,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[0,2]) >= float(user_high) :
			send_email_high_cashbuy()
	elif target_currency_name == "港幣 (HKD)":
		if float(table.iloc[1,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[1,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "英鎊 (GBP)":
		if float(table.iloc[2,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[2,2]) >= float(user_high) :	
			send_email_high_cashbuy()
	elif target_currency_name == "澳幣 (AUD)":
		if float(table.iloc[3,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[3,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "加拿大幣 (CAD)":
		if float(table.iloc[4,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[4,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "新加坡幣 (SGD)":
		if float(table.iloc[5,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[5,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "瑞士法郎 (CHF)":
		if float(table.iloc[6,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[6,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "日圓 (JPY)":
		if float(table.iloc[7,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[7,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "瑞典幣 (SEK)":
		if float(table.iloc[9,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[9,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name ==  "紐元 (NZD)":
		if float(table.iloc[10,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[10,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "泰幣 (THB)":
		if float(table.iloc[11,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[11,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "菲國比索 (PHP)":
		if float(table.iloc[12,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[12,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "印尼幣 (IDR)":
		if float(table.iloc[13,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[13,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "歐元 (EUR)":
		if float(table.iloc[14,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[14,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "韓元 (KRW)":
		if float(table.iloc[15,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[15,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "越南盾 (VND)":
		if float(table.iloc[16,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[16,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "馬來幣 (MYR)":
		if float(table.iloc[17,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[17,2]) >= float(user_high) : 
			send_email_high_cashbuy()
	elif target_currency_name == "人民幣 (CNY)":
		if float(table.iloc[18,2]) <= float(user_low) :
			send_email_low_cashbuy()
		if float(table.iloc[18,2]) >= float(user_high) : 
			send_email_high_cashbuy()

#若使用者有勾選現金匯率－銀行賣出，則依其設定之標準寄信
if user_CashSell == "1":
	if target_currency_name == "美金 (USD)":
		if float(table.iloc[0,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[0,3]) >= float(user_high) :
			send_email_high_cashsell()
	elif target_currency_name == "港幣 (HKD)":
		if float(table.iloc[1,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[1,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "英鎊 (GBP)":
		if float(table.iloc[2,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[2,3]) >= float(user_high) :	
			send_email_high_cashsell()
	elif target_currency_name == "澳幣 (AUD)":
		if float(table.iloc[3,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[3,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "加拿大幣 (CAD)":
		if float(table.iloc[4,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[4,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "新加坡幣 (SGD)":
		if float(table.iloc[5,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[5,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "瑞士法郎 (CHF)":
		if float(table.iloc[6,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[6,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "日圓 (JPY)":
		if float(table.iloc[7,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[7,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "瑞典幣 (SEK)":
		if float(table.iloc[9,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[9,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name ==  "紐元 (NZD)":
		if float(table.iloc[10,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[10,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "泰幣 (THB)":
		if float(table.iloc[11,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[11,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "菲國比索 (PHP)":
		if float(table.iloc[12,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[12,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "印尼幣 (IDR)":
		if float(table.iloc[13,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[13,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "歐元 (EUR)":
		if float(table.iloc[14,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[14,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "韓元 (KRW)":
		if float(table.iloc[15,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[15,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "越南盾 (VND)":
		if float(table.iloc[16,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[16,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "馬來幣 (MYR)":
		if float(table.iloc[17,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[17,3]) >= float(user_high) : 
			send_email_high_cashsell()
	elif target_currency_name == "人民幣 (CNY)":
		if float(table.iloc[18,3]) <= float(user_low) :
			send_email_low_cashsell()
		if float(table.iloc[18,3]) >= float(user_high) : 
			send_email_high_cashsell()

#若使用者有勾選即期匯率－銀行買入，則依其設定之標準寄信
if user_CurrBuy == "1":
	if target_currency_name == "美金 (USD)":
		if float(table.iloc[0,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[0,4]) >= float(user_high) :
			send_email_high_currbuy()
	elif target_currency_name == "港幣 (HKD)":
		if float(table.iloc[1,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[1,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "英鎊 (GBP)":
		if float(table.iloc[2,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[2,4]) >= float(user_high) :	
			send_email_high_currbuy()
	elif target_currency_name == "澳幣 (AUD)":
		if float(table.iloc[3,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[3,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "加拿大幣 (CAD)":
		if float(table.iloc[4,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[4,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "新加坡幣 (SGD)":
		if float(table.iloc[5,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[5,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "瑞士法郎 (CHF)":
		if float(table.iloc[6,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[6,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "日圓 (JPY)":
		if float(table.iloc[7,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[7,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "南非幣 (ZAR)":
		if float(table.iloc[8,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[8,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "瑞典幣 (SEK)":
		if float(table.iloc[9,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[9,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name ==  "紐元 (NZD)":
		if float(table.iloc[10,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[10,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "泰幣 (THB)":
		if float(table.iloc[11,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[11,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "歐元 (EUR)":
		if float(table.iloc[14,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[14,4]) >= float(user_high) : 
			send_email_high_currbuy()
	elif target_currency_name == "人民幣 (CNY)":
		if float(table.iloc[18,4]) <= float(user_low) :
			send_email_low_currbuy()
		if float(table.iloc[18,4]) >= float(user_high) : 
			send_email_high_currbuy()

#若使用者有勾選即期匯率－銀行賣出，則依其設定之標準寄信
if user_CurrSell == "1":
	if target_currency_name == "美金 (USD)":
		if float(table.iloc[0,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[0,5]) >= float(user_high) :
			send_email_high_currsell()
	elif target_currency_name == "港幣 (HKD)":
		if float(table.iloc[1,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[1,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "英鎊 (GBP)":
		if float(table.iloc[2,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[2,5]) >= float(user_high) :	
			send_email_high_currsell()
	elif target_currency_name == "澳幣 (AUD)":
		if float(table.iloc[3,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[3,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "加拿大幣 (CAD)":
		if float(table.iloc[4,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[4,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "新加坡幣 (SGD)":
		if float(table.iloc[5,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[5,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "瑞士法郎 (CHF)":
		if float(table.iloc[6,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[6,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "日圓 (JPY)":
		if float(table.iloc[7,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[7,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "南非幣 (ZAR)":
		if float(table.iloc[8,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[8,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "瑞典幣 (SEK)":
		if float(table.iloc[9,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[9,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name ==  "紐元 (NZD)":
		if float(table.iloc[10,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[10,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "泰幣 (THB)":
		if float(table.iloc[11,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[11,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "歐元 (EUR)":
		if float(table.iloc[14,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[14,5]) >= float(user_high) : 
			send_email_high_currsell()
	elif target_currency_name == "人民幣 (CNY)":
		if float(table.iloc[18,5]) <= float(user_low) :
			send_email_low_currsell()
		if float(table.iloc[18,5]) >= float(user_high) : 
			send_email_high_currsell()