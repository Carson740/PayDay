print("Welcome to your Paycheck Distributor!")

paycheck = input("To begin, please input the amount you received from your paycheck. Round to the nearest whole number"
                 '\n$')

print('$' + paycheck)

creditcard = input("How much is your credit card balance? Round to the nearest whole number" '\n$')

total = round(int(paycheck) - int(creditcard))
savings = 50
food = round(int(total) * .3)
foodweekly = round(int(food) * .5)
other = round(int(total) - int(food) - int(savings))

print("Paycheck: " + '$' + str(paycheck))
print("Credit Balance: " + '$' + str(creditcard))
print("Into Savings: " + '$' + str(savings))
print("Food Budget: " + '$' + str(food) + "($" + str(foodweekly) + " per week)")
print("Other/Frivolous: " + '$' + str(other))
print("" + '\n' + '\n')
input("Press any key to close.")
