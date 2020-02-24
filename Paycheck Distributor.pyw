# Importing
import os
from tkinter import *
import tkinter as tk
from math import floor


def float_round(num, places=0, direction=floor):  # Defines the float_round function
    return direction(num * (10**places)) / float(10**places)


mw = tk.Tk()  # Tkinter window initialization
mw.geometry("400x600")
mw.title("PayDay!")
mw.configure(bg='#B8B8B8')
mw.resizable(False, False)

payask = Entry(mw)  # Assigning variables to Tkinter's Entry boxes
creditask = Entry(mw)
billask = Entry(mw)
savingsask = Entry(mw)
groceryask = Entry(mw)
payask.grid(row=3, column=0, sticky=W)  # .get specifies where to play the Entry box


def openconfig():  # Defining openconfig to open the config.txt file
    os.startfile('config.txt')


def remout():  # Fills the labels with blank space with a gray background to erase previous output in case it exists
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

    payoutrem.grid(row=16, column=0, sticky=W)  # .grid specifies where to put the Labels
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
        savingshave = Label(mw, text="Savings amount/percentage has been set in the config.", bg='#B8B8B8')
        savingshave.grid(row=9, sticky=W)
    elif savingstxtlist == '\n':
        savingsask.grid(row=9, sticky=W)
        Label(mw, text='Enter your savings amount with a $ or percentage with a % ', bg='#B8B8B8')\
            .grid(row=8, column=0, sticky=W)

    grocerytxt = open('config.txt')
    grocerytxtlist = grocerytxt.readlines()[14]
    grocerytxt.close()
    if grocerytxtlist != '\n':
        groceryhave = Label(mw, text="Grocery amount/percentage has been set in the config.", bg='#B8B8B8')
        groceryhave.grid(row=11, sticky=W)
    elif grocerytxtlist == '\n':
        groceryask.grid(row=11, sticky=W)
        Label(mw, text='Enter your grocery amount with a $ or percentage with a % ', bg='#B8B8B8')\
            .grid(row=10, column=0, sticky=W)


def payday():
    remout()
    payout = payask.get()
    payfinal = float(payout) - float(bills) - float(credit)

    if "$" in payout:
        payout = payout.replace('$', '')
    paylist = payout.split(", ")
    paynosum = map(float, paylist)
    payout = sum(paynosum)

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
        elif creditunsplitask == '':
            creditunsplit = '0'
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
        elif billsunsplitask == '':
            billsunsplit = '0'
        else:
            billsunsplit = billsunsplitask
        billslist = billsunsplit.split(", ")
        billnosum = map(float, billslist)
        bills = sum(billnosum)

    grocerytxt = open('config.txt')
    grocerytxtlist = grocerytxt.readlines()[14]
    grocerytxt.close()

    if grocerytxtlist != '\n':
        if "%" in grocerytxtlist:
            grocerytxtlist = grocerytxtlist.replace('%', '')
            grocery = '.' + grocerytxtlist
            groceryfinal = payfinal*float(grocery)
        elif "$" in grocerytxtlist:
            grocerytxtlist = grocerytxtlist.replace('$', '')
            groceryfinal = grocerytxtlist
    else:
        grocerypercentraw = groceryask.get()
        if "%" in grocerypercentraw:
            grocerypercent = grocerypercentraw.replace('%', '')
            grocery = '.' + grocerypercent
            groceryfinal = payfinal*float(grocery)
        elif "$" in grocerypercentraw:
            groceryamount = grocerypercentraw.replace('$', '')
            groceryfinal = groceryamount
        elif grocerypercentraw == '':
            groceryfinal = '0'

    savingstxt = open('config.txt')
    savingstxtlist = savingstxt.readlines()[12]
    savingstxt.close()

    if savingstxtlist != '\n':
        if "%" in savingstxtlist:
            savingstxtlist = savingstxtlist.replace('%', '')
            savings = '.' + savingstxtlist
            savefinal = payfinal*float(savings)
        elif "$" in savingstxtlist:
            savingstxtlist = savingstxtlist.replace('$', '')
            savefinal = savingstxtlist
        else:
            print("null")
    else:
        savingspercentraw = savingsask.get()
        if "%" in savingspercentraw:
            savingspercent = savingspercentraw.replace('%', '')
            savings = '.' + savingspercent
            savefinal = payfinal*float(savings)
        elif "$" in savingspercentraw:
            savingamount = savingspercentraw.replace('$', '')
            savefinal = savingamount
        elif savingspercentraw == '':
            savefinal = '0'

    global credit
    global bills
    global groceryfinal
    global savefinal

    payoutlabel = Label(mw, text='Paycheck Amount: $' + str((float_round(float(payout), 2, round))), bg='#B8B8B8')
    creditout = Label(mw, text='Credit Amount: $' + str((float_round(float(credit), 2, round))), bg='#B8B8B8')
    billsout = Label(mw, text='Bills Amount: $' + str((float_round(float(bills), 2, round))), bg='#B8B8B8')
    other = ((float(payout)) - (float(bills)) - (float(credit)) - (float(savefinal)) - (float(groceryfinal)))
    saveout = Label(mw, text='Savings Amount: $' + str((float_round(float(savefinal), 2, round))), bg='#B8B8B8')
    otherout = Label(mw, text='Other/Frivolous: $' + str((float_round(float(other), 2, round))), bg='#B8B8B8')
    groceryout = Label(mw, text='Grocery/Food Budget: $' + str((float_round(float(groceryfinal), 2, round))),
                       bg='#B8B8B8')

    payoutlabel.grid(row=16, column=0, sticky=W)
    creditout.grid(row=17, column=0, sticky=W)
    billsout.grid(row=18, sticky=W)
    saveout.grid(row=19, column=0, sticky=W)
    groceryout.grid(row=20, column=0, sticky=W)
    otherout.grid(row=21, column=0, sticky=W)


remout()
inputmethods()
Welcome = Label(mw, text="Welcome to PayDay!\n", font='none 18 bold', bg='#B8B8B8')
Welcome.grid(row=0, column=0)
Warninglabel = Label(mw, text="If a box does not apply to you, you may leave it empty.", font='none 14', bg='#B8B8B8')
Warninglabel.grid(row=1, column=0)

Label(mw, text='Enter your paycheck amount. If you have multiple, separate by commas: ', bg='#B8B8B8').grid(row=2, column=0, sticky=W)
Label(mw, text='', bg='#B8B8B8').grid(row=12, column=0, sticky=W)
Calculate = Button(mw, text="Calculate", command=payday)
Calculate.grid(row=30, sticky=W)
OpenConfig = Button(mw, text="Open Config", command=openconfig)
OpenConfig.grid(row=32, sticky=W)

mw.mainloop()
