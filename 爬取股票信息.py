import re
import requests
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url,code='utf-8'):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ''

def getStockList(lst,stock_listURL):
	html = getHTMLText(stock_listURL,'GB2312')
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
	num = 0
	for i in a:
		try:
			if num >= 50:
				break
			href = i.attrs['href']
			lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
			num = num + 1
		except:
			continue

def getStockInfo(lst,stock_infoURL,fpath):
	count = 0
	for stock in lst:
		
		url = stock_infoURL + stock + ".html"
		html =getHTMLText(url)
		try:
			if html=='':
				continue
			infoDict = {}
			soup = BeautifulSoup(html,'html.parser')
			stockInfo = soup.find('div',attrs={'class':'stock-bets'})
			
			name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
			infoDict.update({'股票名称':name.text.split()[0]})
			
			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val
				
			with open(fpath,'a',encoding='uft-8') as f:
				f.write(str(infoDict)) + '\n'
				count = count + 1
				print('\r当前进度:{:.2f}%'.format(count*100/len(lst)),end='')

		except:
			count = count + 1
			print('\r当前进度:{:.2f}%'.format(count*100/len(lst)),end='')
			continue
		
def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'http://gupiao.baidu.com/stock/'
	output_file = r'C:\Users\hp\Desktop\python_work\Stocks.txt'
	slist = []
	getStockList(slist,stock_list_url)
	getStockInfo(slist,stock_info_url,output_file)

main()
