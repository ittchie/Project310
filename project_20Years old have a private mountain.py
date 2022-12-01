# -*- coding: utf-8 -*-
"""Project_1640703870.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f0XU1m3y5vxeqnJ4p25mMCGxz8R4Smju
"""

# CS310 Project : 20 YEARS HAVE A PRIVATE MOUNTAIN 
# BY : ITT NIYOMSANTI 1640703870 127B 

import datetime;
ct = datetime.datetime.now()
ct = str(ct)
time = (ct[0:-7])

def buy (fee,cur,coin) :
  rate = float(input("Enter rate (%s/%s) : "%(cur,coin)))
  while rate <= 0 : 
    print("Please enter rate more than 0 %s/%s "%(cur,coin))
    rate = float(input("Enter rate (%s/%s) : "%(cur,coin)))
  spend = float(input("Enter your spend (%s) : "%(cur)))
  while spend <= 0 :
    print("Please enter spend more than 0 %s"%(cur))
    spend = float(input("Enter your spend (%s) : "%(cur)))
  spendlist.append(spend)
  buyratelist.append(rate)
  totalfee = spend * fee
  totalspend = spend - totalfee
  amt = totalspend/rate
  amtlist.append(amt)
  feebuylist.append(totalfee)
  print("-"*51)
  print("Spent                : %10.2f \t %s "%(totalspend,cur))
  print("Fees                 : %10s   \t %s"%(-totalfee,cur))
  print("Rate                 : %10.2f \t %s/%s"%(rate,cur,coin))
  print("You received         : %10f   \t %s"%(amt,coin))
  print("-"*51)
  print("BALANCE              : %10f   \t %s"%(sum(amtlist)-sum(selllist),coin))
  print("-"*51)
  return (spend,rate)

def funper (amtlist,sellrate,fee) :
  sellper = float(input("Enter sell percent (%) : "))
  while sellper < 0 or sellper > 100 :
    print("Please enter 0 - 100 %")
    sellper = float(input("Enter sell percent (%) : "))
  per = sellper/100
  sell = (sum(amtlist)-sum(selllist)) * per 
  totalsell = sell * sellrate 
  totalfee = totalsell * fee
  rec = totalsell - totalfee
  reclist.append(rec)
  selllist.append(sell)
  feeselllist.append(totalfee)
  print("-"*51)
  print("You sold            : %10f   \t %s"%(-sell,coin))
  print("Fees                : %10.2f \t %s"%(-totalfee,cur))
  print("Rate                : %10.2f \t %s/%s"%(sellrate,cur,coin))
  print("You Received        : %10.2f \t %s"%(rec,cur))
  print("-"*51)
  print("BALANCE             : %10f   \t %s"%(sum(amtlist)-sum(selllist),coin))
  print("-"*51)

def funfiat(maxfiatsell,sellrate,fee) :
  sellfix = float(input("Fix %s sell : "%(cur)))
  while maxfiatsell < sellfix :
    print("Your %s not enough"%(cur))
    sellfix = float(input("Fix %s sell : "%(cur)))
  while sellfix < 0 :
    print("Please input more than 0 : ")
    sellfix = float(input("Fix %s sell : "%(cur)))
  sell = sellfix/sellrate
  totalfee = sellfix * fee
  totalsell = sell + (sell*fee)
  reclist.append(sellfix)
  selllist.append(totalsell)
  feeselllist.append(totalfee)
  print("-"*51)
  print("You sold            : %10f   \t %s"%(-totalsell,coin))
  print("Fees                : %10.2f \t %s"%(-totalfee,cur))
  print("Rate                : %10.2f \t %s/%s"%(sellrate,cur,coin))
  print("You Received        : %10.2f \t %s"%(sellfix,cur))
  print("-"*51)
  print("BALANCE             : %10f   \t %s"%(sum(amtlist)-sum(selllist),coin))
  print("-"*51)

def funamt (maxamtsell,sellrate,fee):
  sellamt = float(input("Enter sell amount : "))
  while sellamt < 0 :
    print("Please input more than 0")
    sellamt = float(input("Enter sell amount : "))
  while maxamtsell < sellamt :
    print("Your %s not enough"%(coin))
    sellamt = float(input("Enter sell amount : "))
  sell = sellamt  * sellrate + (sellamt  * sellrate * fee)
  totalfee = sell*fee
  totalsell = sell - totalfee
  totalamt = sellamt+(sellamt*fee)
  selllist.append(totalamt)
  feeselllist.append(totalfee)
  reclist.append(totalsell)
  print("You sold            : %10f   \t %s"%(-sellamt,coin))
  print("Fees                : %10.2f \t %s"%(-totalfee,cur))
  print("Rate                : %10.2f \t %s/%s"%(sellrate,cur,coin))
  print("You Received        : %10.2f \t %s"%(totalsell,cur))
  print("-"*51)
  print("BALANCE             : %10f   \t %s"%(sum(amtlist)-sum(selllist),coin))
  print("-"*51)

def result (coin,time,cur,feebuylist,exfee,spendlist,buyratelist,amtlist,reclist,sellratelist,feeselllist,selllist) :
  print("-"*51)
  print(" %s RESULT ".center(51)%(coin))
  print("-"*51)
  print(time)
  print("FIAT                  : %10s"%(cur))
  print("EXCHANGE FEE          : %10.2f %s "%(exfee,"%"))
  print("-"*51)
  for i in range(len(feebuylist)) :
    print("BUY %d".center(51)%(i+1))
    print("SPENT                 :  %10.2f \t %s "%(spendlist[i],cur))
    print("BUY RATE              :  %10.2f \t %s/%s"%(buyratelist[i],cur,coin))
    print("FEE                   :  %10.2f \t %s"%(-(feebuylist[i]),cur))
    print("AMOUNT                :  %10f   \t %s"%(amtlist[i],coin))
    print("-"*51)
  print("TOTAL BUY".center(51))
  print("SPENT                 :  %10.2f \t %s"%(sum(spendlist),cur))
  print("FEE                   :  %10.2f \t %s"%(-(sum(feebuylist)),cur))
  print("AMOUNT                :  %10f   \t %s"%(sum(amtlist),coin))
  print("-"*51)
  for i in range(len(feeselllist)) :
    print("SELL %d".center(51)%(i+1))
    print("RECIEVE               : %10.2f \t %s"%(reclist[i],cur))
    print("SELL RATE             : %10.2f \t %s/%s"%(sellratelist[i],cur,coin))
    print("FEE                   : %10.2f \t %s"%(-feeselllist[i],cur))
    print("SELL AMOUNT           : %10f   \t %s "%(-selllist[i],coin))
    print("-"*51)
  print("TOTAL SELL".center(51))
  print("RECIEVE               : %10.2f \t %s"%(sum(reclist),cur))
  print("FEE                   : %10.2f \t %s"%(-(sum(feeselllist)),cur))
  print("SELL AMOUNT           : %10f   \t %s"%(-sum(selllist),coin))
  print("-"*51)
  print("You total spent       :  %10.2f \t %s"%(sum(spendlist),cur))
  print("Total fee             :  %10.2f \t %s"%(-((sum(feebuylist)+(sum(feeselllist)))),cur))
  print("You amount balance    :  %10f   \t %s "%(sum(amtlist)-sum(selllist),coin))
  print("Lower rate sell       :  %10.2f \t %s/%s "%((float((sum(spendlist))/(sum(amtlist))+(((sum(spendlist))/(sum(amtlist))*fee)))),cur,coin))
  print("You recieve form sell :  %10.2f \t %s"%(sum(reclist),cur))
  print("-"*51)
  
def clear (spendlist,feebuylist,feeselllist,amtlist,selllist,reclist,buyratelist,sellratelist) :
  spendlist.clear()
  feebuylist.clear()
  feeselllist.clear()
  amtlist.clear()
  selllist.clear()
  reclist.clear()
  buyratelist.clear()
  sellratelist.clear()

  
def save (coin,time,cur,feebuylist,exfee,spendlist,buyratelist,amtlist,reclist,sellratelist,feeselllist,selllist) :
  with open("CRYPTO.txt","a+") as file :
    file.write("\n")
    file.write("-"*51)
    file.write("\n")
    file.write("%s RESULT".center(51)%(coin))
    file.write("\n")
    file.write("-"*51)
    file.write("\nFIAT                 : %10s\n"%(cur))
    file.write("EXCHANGE FEE         : %10.2f %s\n"%(exfee,"%"))
    file.write("%s\n"%(time))
    file.write("-"*51)
    file.write("\n")
    for i in range(len(feebuylist)) :
      file.write("BUY %d".center(51)%(i+1))
      file.write("\nSPENT                 :  %10.2f \t %s\n"%(spendlist[i],cur))
      file.write("BUY RATE              :  %10.2f \t %s/%s\n"%(buyratelist[i],cur,coin))
      file.write("FEE                   :  %10.2f \t %s\n"%(-(feebuylist[i]),cur))
      file.write("AMOUNT                :  %10f \t %s\n"%(amtlist[i],coin))
      file.write("-"*51)
    file.write("\n")
    file.write("TOTAL BUY".center(51))
    file.write("\nSPENT                 :  %10.2f \t %s\n"%(sum(spendlist),cur))
    file.write("FEE                   :  %10.2f \t %s\n"%(-(sum(feebuylist)),cur))
    file.write("AMOUNT                :  %10f \t %s\n"%(sum(amtlist),coin))
    file.write("-"*51)
    file.write("\n")
    for i in range(len(feeselllist)) :
      file.write("SELL %d".center(51)%(i+1))
      file.write("\nRECIEVE               : %10.2f \t %s\n"%(reclist[i],cur))
      file.write("SELL RATE             : %10.2f \t %s/%s\n"%(sellratelist[i],cur,coin))
      file.write("FEE                   : %10.2f \t %s\n"%(-feeselllist[i],cur))
      file.write("SELL AMOUNT           : %10f \t %s\n"%(selllist[i],coin))
      file.write("-"*51)
    file.write("\n")
    file.write("TOTAL SELL".center(51))
    file.write("\nRECIEVE               : %10.2f \t %s\n"%(sum(reclist),cur))
    file.write("FEE                   : %10.2f \t %s\n"%(-(sum(feeselllist)),cur))
    file.write("SELL AMOUNT           : %10f \t %s\n"%(sum(selllist),coin))
    file.write("-"*51)
    file.write("\nYou total spent       :  %10.2f \t %s\n"%(sum(spendlist),cur))
    file.write("Total fee             :  %10.2f \t %s\n"%(-((sum(feebuylist)+(sum(feeselllist)))),cur))
    file.write("You amount balance    :  %10f \t %s \n"%(sum(amtlist)-sum(selllist),coin))
    file.write("Lower rate sell       :  %10.2f \t %s/%s\n"%((float((sum(spendlist))/(sum(amtlist))+(((sum(spendlist))/(sum(amtlist))*fee)))),cur,coin))
    file.write("You recieve form sell :  %10.2f \t %s\n"%(sum(reclist),cur))
    file.write("-"*51)
    file.write("\n")
    print("----- SAVE TO FILE COMPLETE -----")

spendlist = []
feebuylist = []
feeselllist = []
amtlist = []
selllist = []
reclist = []
buyratelist = []
sellratelist = []
maxamtsell,maxfiatsell=(0,0)

print("Start the Crypto currency calulater")
exfee = float(input("Enter your exchange fees(%) : "))
while exfee < 0 or exfee > 100:
  print("Please enter 0 - 100 % ")
  exfee = float(input("Enter your exchange fees(%) : "))
fee = exfee/100
cur = input("Enter your Fait : ").upper()
coin = input("Enter your Token : ").upper()
start = "S"
while start != "N":
  buy(fee,cur,coin)
  print("SELL ")
  print("YES  (1)")
  print("NO   (2)")
  sell = input("SELECT THE MENU : ").upper()
  print("-"*51)
  while sell != "1" and sell != "2" :
    sell = input("Please select 1 or 2  ").upper()
  while sell == "1" :
    sellrate = float(input("Enter sell rate (%s/%s) : "%(cur,coin)))
    while sellrate <= 0 :
      sellrate = float(input("Enter sell rate more than 0 (%s/%s) : "%(cur,coin)))
    sellratelist.append(sellrate)
    maxamtsell = (sum(amtlist)-sum(selllist)) - ((sum(amtlist)-sum(selllist))  * fee)
    maxfiatsell = ((sum(amtlist)-sum(selllist))*sellrate) - ((sum(amtlist)-sum(selllist)) * sellrate * fee)
    print("Sell max amount : %10f   \t %s "%(maxamtsell,coin))
    print("Sell max fiat   : %10.2f \t %s "%(maxfiatsell,cur))
    print("-"*51)
    print("|  PERCENT (1)  |  FIAT %s (2)  | %s AMOUNT (3) |"%(cur,coin))
    print("-"*51)
    menu = input("Select sell menu : ").upper()
    while menu != "1" and menu != "2" and menu != "3" :
      menu = input("Please select (1)(2)(3) : ").upper()
    if menu == "1" :
      funper (amtlist,sellrate,fee)
    elif menu == "2" :
      funfiat(maxfiatsell,sellrate,fee)
    elif menu == "3" :
      funamt(maxamtsell,sellrate,fee)
    print("-"*51)
    print("SELL MORE ? ")
    print("YES  (1)")
    print("NO   (2)")
    sell = input("SELECT THE MENU : ").upper()
    print("-"*51)
    while sell != "1" and sell != "2" :
      sell = input("Please select (1)(2) : ").upper()
  result (coin,time,cur,feebuylist,exfee,spendlist,buyratelist,amtlist,reclist,sellratelist,feeselllist,selllist,)
  print()
  print("-"*51)
  print("|  BUY MORE (1)  |   RESET (2)   |    QUIT (3)    |")
  print("-"*51)
  print("|-----------SAVE ALL RESULT TO FILE (4)-----------|")
  print("-"*51)
  endmenu = input("Select menu : ").upper()
  while endmenu != "1" and endmenu != "2" and endmenu != "3" and endmenu != "4" :
    endmenu = input("Please select (1)(2)(3)(4) : ")
  if endmenu == "1" :
    start != "N"
  elif endmenu == "2" :
    clear(spendlist,feebuylist,feeselllist,amtlist,selllist,reclist,buyratelist,sellratelist)
    print("----- RESET COMPLETED -----")
    exfee = float(input("Enter your exchange fees(%) : "))
    while exfee < 0 or exfee > 100:
      print("Please enter 0 - 100 % ")
      exfee = float(input("Enter your exchange fees(%) : "))
    fee = exfee/100
    cur = input("Enter your Fait : ").upper()
    coin = input("Enter your Token : ").upper()
  elif endmenu == "3" :
    start = "N"
  elif endmenu == "4" :
    save (coin,time,cur,feebuylist,exfee,spendlist,buyratelist,amtlist,reclist,sellratelist,feeselllist,selllist)
    start = "N"
print("----- EXIT PROGRAM -----")