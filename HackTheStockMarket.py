import numpy as np
import copy
import webbrowser
import wx
#import matplotlib.pyplot as plt
#import os
import pandas as pd
#data = np.getfromtxt('data_file.txt', delimiter=',')
from openpyxl import load_workbook
from tkinter import *
#df = pd.read_csv("AMEX.csv")
#wb=load_workbook('./test.xlsx')
#print(wb.get_sheet_names())
#sheet=wb.get_sheet_by_name('AMEX')







colnames=['name','symbol','dopen','dhigh','dlow','dclose','netchg','perc','vol','wkh','wkl','div','yield','pe','ytdp']
#CHANGE FILE HERE
data=pd.read_csv('AMEX2.csv', names=colnames)
name=data.name.tolist()
symbol=data.symbol.tolist()
dopen=data.dopen.tolist()
dhigh=data.dhigh.tolist()
dlow=data.dlow.tolist()
dclose=data.dclose.tolist()
perc=data.perc.tolist()
wkh=data.wkh.tolist()
wkl=data.wkl.tolist()
ytdp=data.ytdp.tolist()

#class stock:
#	total = 0
#	def __init__(self,do,dh,dl,dc,pc,yh,yl,ypc):
#		self.do=do
#		self.dh=dh
#		self.dl=dl
#		self.dc=dc
#		self.pc=pc
#		self.yh=yh
#		self.yl=yl
#		self.ypc=ypc
#		stock.total+=1
	
def giveRank(do,dh,dl,dc,pc,yh,yl,ypc):
##		self.dh=dh
#		self.dl=dl
#		self.dc=dc
#		self.pc=pc
#		self.yh=yh
#		self.yl=yl
#		self.ypc=ypc
		meme1 = (do+dc)/2
		#print(meme1)
		std=((do-(meme1))**2+(dh-meme1)**2+(dl-meme1)**2+(dc-meme1)**2)**0.5
		#print(std)
		mean = (yh+yl)/2
		#print(mean)
		ystd=((yl-mean)**2+(yh-mean)**2+(dc-mean)**2)**0.5
		#print(ystd)
		metric= ((pc+(.3*ypc))/((.4*std)+ystd))
		#print(metric)
		return metric
def useable(thinglist):
	try:
		thinglist=float(thinglist)
	except ValueError:
		thinglist[counter]=""
	return thinglist			


#starts at first row of data

counter=5
metrics=[]
while(counter<len(dopen)):
	num1=giveRank(useable(dopen[counter]),useable(dhigh[counter]),useable(dlow[counter]),useable(dclose[counter]),useable(perc[counter]),useable(wkh[counter]),useable(wkl[counter]),useable(ytdp[counter])) 
	#print(num1)
	#print(counter)
	metrics.append(num1)
	counter+=1
#print(metrics)	
#a= stock('hi',4,6,3,5,6,8,7,8)
#print(a.giveRank())

#rank stocks

i1=0.0
i2=0.0
i3=0.0
i4=0.0
i5=0.0
theMatrix=copy.copy(metrics)
theMatrix.sort(reverse=True)
counter1=0
while(counter1<len(metrics)):
	if(theMatrix[0]==metrics[counter1]):
		i1=counter1
	elif(theMatrix[1]==metrics[counter1]):
		i2=counter1		
	elif(theMatrix[2]==metrics[counter1]):
		i3=counter1	
	elif(theMatrix[3]==metrics[counter1]):
		i4=counter1					
	elif(theMatrix[4]==metrics[counter1]):
		i5=counter1		
	counter1+=1	
#print(i1)
#print(i2)
#print(i3)
#print(i4)
#print(i5)
#get correct index- account for shifting
i1+=5
i2+=5
i3+=5
i4+=5
i5+=5
print("   /\\   ")
print("  /  \\_/\\         HACK THE STOCK MARKET V1.0.1")
print(" /        \\  /    CASEY FORTMAN & ALEX STEINIG")
print("/          \\/")
print("---------------------------------------------------------------")
print()
print('The #1 stock is: '+ symbol[i1]+' - '+name[i1]+' with a rating of ', metrics[i1-5])
print('The #2 stock is: '+ symbol[i2]+' - '+name[i2]+' with a rating of ', metrics[i2-5])
print('The #3 stock is: '+ symbol[i3]+' - '+name[i3]+' with a rating of ', metrics[i3-5])
print('The #4 stock is: '+ symbol[i4]+' - '+name[i4]+' with a rating of ', metrics[i4-5])
print('The #5 stock is: '+ symbol[i5]+' - '+name[i5]+' with a rating of ', metrics[i5-5])
print("---------------------------------------------------------------")
s1 =0
s2=0
s3=0
s4=0
s5=0
s1p=float(dclose[i1])
s2p=float(dclose[i2])
s3p=float(dclose[i3])
s4p=float(dclose[i4])
s5p=float(dclose[i5])
balance=float(input("How much do you want to invest? "))
balanceCopy = copy.copy(balance)
remainder=0
buy2=True
buy3=True
buy4 = True
buy5 = True
if(((int(s2p/s1p)*s1p)+s2p)>(balance)):
	buy2 = false
if(((int(s3p/s1p)*s1p)+s3p)>balance):
	buy3 = false	
if(((int(s4p/s1p)*s1p)+s4p)>balance):
	buy4 = false
if(((int(s5p/s1p)*s1p)+s5p)>balance):
	buy5 = false

while(True):
	if(balance-s1p>0):
		s1+=1
		balance=balance-s1p
	if ((balance-s2p>0) and (buy2)):
		s2+=1
		balance = balance - s2p
	if ((balance - s3p > 0) and (buy3)):
		s3+=1
		balance = balance - s3p
	if ((balance - s4p > 0) and (buy4)):
		s4+=1
		balance = balance - s4p
	if ((balance - s5p > 0) and (buy5)):
		s5+=1
		balance = balance - s5p
	else:
		break
print("")
print("---------------------------------------------------------")
print("")
remainder = balance
print('Buy: ', s1 , ' stocks of '+ symbol[i1]+' - '+name[i1]+ '\t at $',dclose[i1])
print('Buy: ', s2 , ' stocks of '+ symbol[i2]+' - '+name[i2]+ '\t\t at $',dclose[i2])
print('Buy: ', s3 , ' stocks of '+ symbol[i3]+' - '+name[i3]+ '\t\t at $',dclose[i3])
print('Buy: ', s4 , ' stocks of '+ symbol[i4]+' - '+name[i4]+ '\t at $',dclose[i4])
print('Buy: ', s5 , ' stocks of '+ symbol[i5]+' - '+name[i5]+ '\t\t at $',dclose[i5])
print()
print('Totaling: $' , float('%.2f'%(balanceCopy-remainder)))
print()
browserChoice=str(input("Launch Brokerage? Y/N  "))
if(browserChoice=='Y'):
	webbrowser.open('https://www.tdameritrade.com/home.page')
else:
	print()
	print('Thank you for using "Hack the Stock Market"!')

print()