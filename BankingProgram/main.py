# Python 4th mini project
# python banking program using basic functions()

def show_balance():
    print(f"Your balance is ${balance:.2f}") # Here .2f is for two decimal value (0.00)
    

def deposit():
    amount = float(input("Enter your depositing amount: $"))
    if amount < 0:
        print("That is not valid amount ! ")
        return 0
    else:
        return amount
def withdraw():
       amount = float(input("Enter amout to be withdrawn: $ "))
       if amount > balance:
           print("Oops!, insufficent Fund !")
           return 0
       elif amount <= balance:
            print("--------------------")
            print(f"Dear customer,\nYour balance is credited: ${amount}\nAnkit Bank Ltd.")
            print(f"Your current balance is: ${balance-amount}")
            print("\n--------------------")

            return balance

       elif amount<0:
           print("Amount must be greater than 0")
           return 0
balance =0
is_runnig = True 



while is_runnig:
    print("Mini Banking Program")
    print("--------------------")
    print("1.Deposit Balance")
    print("2.Show my Balance")
    print("3.Withdraw Balance")
    print("4.Exit")
    print("--------------------")

    choice = input("Enter Your choice (1 to 4): ")


    if choice == "1":
        balance += deposit()
    elif choice=='2':
        show_balance()
    elif choice=='3':
        withdraw()
    elif choice=='4':
        is_runnig=False
    else:
        print("You have entered a ivalid choice !")

print("Thank you for visting !")
