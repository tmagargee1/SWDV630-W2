from CheckingAccount import CheckingAccount

def printBalence(account):
    if(account.checkBalence() < 0):
        print("WARNING: Your account is overdrawn")
    print("Current Balence: " + moneyString(account.checkBalence()))

def moneyString(number):
    if abs(number) >= 1:
        money = "${:,.2f}".format(abs(number))
    else:
        money = "¢" + str(int(abs(number) * 100)) 
    return "-" + money if number < 0 else money

def depositIntoAccount(account, amount):
    print("Depositing " + moneyString(amount)) 
    account.deposit(amount)
    printBalence(account)

def withdrawFromAccount(account, amount):
    #Account can overdrawl up to $25 
    if(account.checkBalence() + 25 >= amount):
        print("Withdrawling " + moneyString(amount))
        account.withdrawl(amount)
        printBalence(account)
    else:
        print("Attempted to withdrawl "+ moneyString(amount))
        print("Insufficient funds you can only withdraw up to " + moneyString(account.checkBalence() + 25))

def main():
    account = CheckingAccount("Tim", "Magargee", "123 Road Rd", "111-111-1111")
    print(account)
    print()

    depositIntoAccount(account, 100)
    withdrawFromAccount(account, 50)
    depositIntoAccount(account, 0.5)
    withdrawFromAccount(account, 100)
    withdrawFromAccount(account, 75)
    depositIntoAccount(account, 24.50)

main()
