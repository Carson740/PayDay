from tkinter import *
import tkinter as tk
from math import ceil, floor


def float_round(num, places=0, direction=floor):
    return direction(num * (10**places)) / float(10**places)


mw = tk.Tk()
mw.geometry("400x500")
mw.title("PayDay!")

Welcome = Label(mw, text="Welcome to PayDay!\n", font='none 18 bold')
Welcome.grid(row=0, column=0)
Warning = Label(mw, text="If a box does not apply to you, please input a 0.", font='none 14')
Warning.grid(row=1, column=0)


def payday():
    paycheck = payask.get()
    credit = creditask.get()
    savings = saveask.get()
    foodbudget = foodask.get()
    billsunsplit = billask.get()
    billslist = billsunsplit.split(", ")
    billnosum = map(float, billslist)
    bills = sum(billnosum)
    other = ((float(paycheck)) - (float(credit)) - (float(savings)) - (float(foodbudget)))

    payout = Label(mw, text='Paycheck Amount: ' + str((float_round(float(paycheck), 2, round))))
    payout.grid(row=16, column=0, sticky=W)
    creditout = Label(mw, text='Credit Amount: ' + str((float_round(float(credit), 2, round))))
    creditout.grid(row=17, column=0, sticky=W)
    billsout = Label(mw, text='Bills Amount: ' + str((float_round(float(bills), 2, round))))
    billsout.grid(row=18, sticky=W)
    saveout = Label(mw, text='Savings Amount: ' + str((float_round(float(savings), 2, round))))
    saveout.grid(row=19, column=0, sticky=W)
    foodout = Label(mw, text='Food Budget: ' + str((float_round(float(foodbudget), 2, round))))
    foodout.grid(row=20, column=0, sticky=W)
    otherout = Label(mw, text='Other/Frivolous: ' + str((float_round(float(other), 2, round))))
    otherout.grid(row=21, column=0, sticky=W)


Label(mw, text='Enter your paycheck amount: ').grid(row=2, column=0, sticky=W)
Label(mw, text='Enter your credit amount: ').grid(row=4, column=0, sticky=W)
Label(mw, text='Enter any bills, seperated by a comma: ').grid(row=6, column=0, sticky=W)
Label(mw, text='Enter your savings amount (default $50): ').grid(row=8, column=0, sticky=W)
Label(mw, text='Enter your food budget (default $50): ').grid(row=10, column=0, sticky=W)
payask = Entry(mw)
payask.grid(row=3, column=0, sticky=W)
creditask = Entry(mw)
creditask.grid(row=5, column=0, sticky=W)
billask = Entry(mw)
billask.grid(row=7, sticky=W)
saveask = Entry(mw)
saveask.grid(row=9, column=0, sticky=W)
foodask = Entry(mw)
foodask.grid(row=11, column=0, sticky=W)
button = Button(mw, text="Calculate", command=payday)
button.grid(row=30, sticky=W)


mw.mainloop()
