import os
from tkinter import *
import tkinter as tk
from math import ceil, floor


def float_round(num, places=0, direction=floor):
    return direction(num * (10**places)) / float(10**places)


mw = tk.Tk()
mw.geometry("400x600")
mw.title("PayDay!")
mw.configure(bg='#B8B8B8')

payask = Entry(mw)
payask.grid(row=3, column=0, sticky=W)
creditask = Entry(mw)
billask = Entry(mw)
savingsask = Entry(mw)
groceryask = Entry(mw)

def openconfig():
    os.startfile('config.txt')


def remout():
    payoutrem = Label(mw, text='                                                                                       '
                               '     ', bg='#B8B8B8')
    creditoutrem = Label(mw, text='                                                                                    '
                                  '     ', bg='#B8B8B8')
    billsoutrem = Label(mw, text='                                                                                     '
                                 '     ', bg='#B8B8B8')
    saveoutrem = Label(mw, text='                                                                                      '
                                '     ', bg='#B8B8B8')
    groceryoutrem = Label(mw, text='                                                                                   '
                                   '     ', bg='#B8B8B8')
    otheroutrem = Label(mw, text='                                                                                     '
                                 '     ', bg='#B8B8B8')
    blankspace = Label(mw, text='                                                                                      '
                                '       ', bg='#B8B8B8')

    payoutrem.grid(row=16, column=0, sticky=W)
    creditoutrem.grid(row=17, column=0, sticky=W)
    billsoutrem.grid(row=18, sticky=W)
    saveoutrem.grid(row=19, column=0, sticky=W)
    groceryoutrem.grid(row=20, column=0, sticky=W)
    otheroutrem.grid(row=21, column=0, sticky=W)
    blankspace.grid(row=22, column=0, sticky=W)


def inputmethods():
    credittxt = open('config.txt')
    credittxtlist = credittxt.readlines()[8]
    credittxt.close()
    if credittxtlist != '\n':
        credithave = Label(mw, text="Credit amounts have been set in the config.", bg='#B8B8B8')
        credithave.grid(row=5, sticky=W)
    elif credittxtlist == '\n':
        creditask.grid(row=5, sticky=W)
        Label(mw, text='Enter your credit payment amount: ', bg='#B8B8B8').grid(row=4, column=0, sticky=W)

    billstxt = open('config.txt')
    billstxtlist = billstxt.readlines()[10]
    billstxt.close()
    if billstxtlist != '\n':
        billhave = Label(mw, text="Bill amounts have been set in the config.", bg='#B8B8B8')
        billhave.grid(row=7, sticky=W)
    elif billstxtlist == '\n':
        billask.grid(row=7, sticky=W)
        Label(mw, text='Enter any bills, separated by a comma: ', bg='#B8B8B8').grid(row=6, column=0, sticky=W)

    savingstxt = open('config.txt')
    savingstxtlist = savingstxt.readlines()[12]
    savingstxt.close()
    if savingstxtlist != '\n':
        savingshave = Label(mw, text="Savings amounts have been set in the config.", bg='#B8B8B8')
        savingshave.grid(row=9, sticky=W)
    elif savingstxtlist == '\n':
        savingsask.grid(row=9, sticky=W)
        Label(mw, text='Enter your savings amount: ', bg='#B8B8B8').grid(row=8, column=0, sticky=W)

    grocerytxt = open('config.txt')
    grocerytxtlist = grocerytxt.readlines()[14]
    grocerytxt.close()
    if grocerytxtlist != '\n':
        groceryhave = Label(mw, text="Grocery amounts have been set in the config.", bg='#B8B8B8')
        groceryhave.grid(row=11, sticky=W)
    elif grocerytxtlist == '\n':
        groceryask.grid(row=11, sticky=W)
        Label(mw, text='Enter your grocery amount: ', bg='#B8B8B8').grid(row=10, column=0, sticky=W)


def payday():
    payout = payask.get()
    billsunsplitask = billask.get()
    if "$" in payout:
        payout = payout.replace('$', '')
    credittxt = open('config.txt')
    credittxtlist = credittxt.readlines()[8]
    credittxt.close()

    if credittxtlist != '\n':
        if "$" in credittxtlist:
            credittxtlist = credittxtlist.replace('$', '')
        creditunsplit = str(credittxtlist)
        creditlist = creditunsplit.split(", ")
        creditnosum = map(float, creditlist)
        credit = sum(creditnosum)
    else:
        creditunsplitask = creditask.get()
        if "$" in creditunsplitask:
            creditunsplit = creditunsplitask.replace('$', '')
        else:
            creditunsplit = creditunsplitask
        creditlist = creditunsplit.split(", ")
        creditnosum = map(float, creditlist)
        credit = sum(creditnosum)

    billstxt = open('config.txt')
    billstxtlist = billstxt.readlines()[10]
    billstxt.close()

    if billstxtlist != '\n':
        if "$" in billstxtlist:
            billstxtlist = billstxtlist.replace('$', '')
        billsunsplit = str(billstxtlist)
        billslist = billsunsplit.split(", ")
        billnosum = map(float, billslist)
        bills = sum(billnosum)
    else:
        billsunsplitask = billask.get()
        if "$" in billsunsplitask:
            billsunsplit = billsunsplitask.replace('$', '')
        else:
            billsunsplit = billsunsplitask
        billslist = billsunsplit.split(", ")
        billnosum = map(float, billslist)
        bills = sum(billnosum)

    savingstxt = open('config.txt')
    savingstxtlist = savingstxt.readlines()[12]
    savingstxt.close()

    if savingstxtlist != '\n':
        if "$" in savingstxtlist:
            savingstxtlist = savingstxtlist.replace('$', '')
        savingsunsplit = str(savingstxtlist)
        savingslist = savingsunsplit.split(", ")
        savingsnosum = map(float, savingslist)
        savings = sum(savingsnosum)
    else:
        savingsunsplit = savingsask.get()
        if "$" in savingsunsplit:
            savingsunsplit = savingsunsplit.replace('$', '')
        else:
            savingsunsplit = savingsunsplit
        savingslist = savingsunsplit.split(", ")
        savingsnosum = map(float, savingslist)
        savings = sum(savingsnosum)

    grocerytxt = open('config.txt')
    grocerytxtlist = grocerytxt.readlines()[14]
    grocerytxt.close()

    if grocerytxtlist != '\n':
        if "$" in grocerytxtlist:
            grocerytxtlist = grocerytxtlist.replace('$', '')
        groceryunsplit = str(grocerytxtlist)
        grocerylist = groceryunsplit.split(", ")
        grocerynosum = map(float, grocerylist)
        grocery = sum(grocerynosum)
    else:
        groceryunsplit = groceryask.get()
        if "$" in groceryunsplit:
            groceryunsplit = groceryunsplit.replace('$', '')
        else:
            groceryunsplit = groceryunsplit
        grocerylist = groceryunsplit.split(", ")
        grocerynosum = map(float, grocerylist)
        grocery = sum(grocerynosum)

    other = ((float(payout)) - (float(bills)) - (float(credit)) - (float(savings)) - (float(grocery)))
    payout = Label(mw, text='Paycheck Amount: ' + str((float_round(float(payout), 2, round))), bg='#B8B8B8')
    creditout = Label(mw, text='Credit Amount: ' + str((float_round(float(credit), 2, round))), bg='#B8B8B8')
    billsout = Label(mw, text='Bills Amount: ' + str((float_round(float(bills), 2, round))), bg='#B8B8B8')
    saveout = Label(mw, text='Savings Amount: ' + str((float_round(float(savings), 2, round))), bg='#B8B8B8')
    groceryout = Label(mw, text='Grocery/Food Budget: ' + str((float_round(float(grocery), 2, round))), bg='#B8B8B8')
    otherout = Label(mw, text='Other/Frivolous: ' + str((float_round(float(other), 2, round))), bg='#B8B8B8')

    payout.grid(row=16, column=0, sticky=W)
    creditout.grid(row=17, column=0, sticky=W)
    billsout.grid(row=18, sticky=W)
    saveout.grid(row=19, column=0, sticky=W)
    groceryout.grid(row=20, column=0, sticky=W)
    otherout.grid(row=21, column=0, sticky=W)


remout()
inputmethods()
Welcome = Label(mw, text="Welcome to PayDay!\n", font='none 18 bold', bg='#B8B8B8')
Welcome.grid(row=0, column=0)
Warning = Label(mw, text="If a box does not apply to you, please input a 0.", font='none 14', bg='#B8B8B8')
Warning.grid(row=1, column=0)

Label(mw, text='Enter your paycheck amount: ', bg='#B8B8B8').grid(row=2, column=0, sticky=W)
Label(mw, text='', bg='#B8B8B8').grid(row=12, column=0, sticky=W)
Calculate = Button(mw, text="Calculate", command=payday)
Calculate.grid(row=30, sticky=W)
RemoveOutput = Button(mw, text="Remove Output", command=remout)
RemoveOutput.grid(row=31, sticky=W)
OpenConfig = Button(mw, text="Open Config", command=openconfig)
OpenConfig.grid(row=32, sticky=W)

mw.mainloop()
