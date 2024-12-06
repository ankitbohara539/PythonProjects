# this is python slot machine
import random
def spin_row():
    symbols = ['🍎','🍉','🍋','🔔','⭐']

    return[random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("--------------------------")
    print(" | " .join(row))
    print("--------------------------")


def get_payout(row, bet):
    if row [0] == row [1] ==row [2]:
        if row[0] == '🍎':
            return bet * 3 
        elif row [0] == '🍉':
            return bet * 2 
        elif row [0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row [0] =='⭐':
            return bet * 10
            
    return 0


def main():
    balance = 100

    print("--------------------------")
    print("Welcome to python slots")
    print("Symbols: 🍎🍉🍋🔔⭐")
    print("--------------------------")


    while balance > 0:
        print(f"Current balace: ${balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficent Funds")
            continue 
        balance -= bet

        row = spin_row()
        print("Spinnig........\n")
        print_row(row)


        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won ${payout}")
        else:
            print("You Lost the round")

        balance += payout

        play_again = input("Do you wanna play again ? (yes/no) :").upper()

        if play_again != "yes":
            break

if __name__== '__main__':
    main()
        
