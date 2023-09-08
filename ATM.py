import sys


'''
This challenge taught me the  benefit of starting over. 
I spent a long time trying multiple ways for this to work, unsucessfully.
Finally I copied out what I had, and then reset the workspace. 
Once I had the default, putting everything back together was much easier and somehow worked. 
'''


account_balance = float(500.25) #how much is in the account
def printbalance(): #printbalance function prints existing balance
  print('Your current balance:\n')
  print(account_balance)
  
def deposit(): #cycles through the deposit steps
  deposit_amount = float(input("How much would you like to deposit today?")) #how much...?
  account_balance = float(500.25) #reads current balance, function would not work without local variable
  account_balance += deposit_amount #new account balance
  print('Deposit was $%.2f, current balance is $%.2f' % (deposit_amount, account_balance))

def withdrawal(): #cycles through withdrawal steps
  withdrawal_amount = float(input("How much would you like to withdraw today?\n")) #how much...?
  account_balance = float(500.25) #reads current balance, function would not work without local variable
  if withdrawal_amount > account_balance: #if withdrawal_amount is greater than current, no withdrawal
    print('$%.2f is greater than your account balance of $%.2f' % (withdrawal_amount, account_balance))
  else:
    account_balance -= withdrawal_amount # if not, print previous and new balance
    print('Withdrawal amount was $%.2f, current balance is $%.2f' % (withdrawal_amount, account_balance))
    
userchoice = input ("What would you like to do?\n") #user input

if (userchoice == 'D'): #deposit
    deposit ()
elif (userchoice == 'B'): #balance
    printbalance()
elif (userchoice == 'W'): #withdrawal
    withdrawal()
elif (userchoice == 'Q'): #quit()
  print('Thank you for banking with us.')