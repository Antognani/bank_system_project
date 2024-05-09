options = """
===================== Hello, dear client! =====================
============== Welcome to the Open Bank System! ===============
Please select the operation you want to execute on your account.

[q] Deposit
[w] Withdraw
[e] Extract
[r] Finish

=> """

balance = 0
balance_limit = 500
extract = ""
withdraw_quantity = 0
WITHDRAW_LIMIT = 3

while True:
    chosen_option = input(options)

    if chosen_option == "q":
        
        value = float(input("Digit the deposit value:"))

        if value > 0:
            balance += value
            extract += f"Deposit: ${value:.2f}\n"

            print("The operation has suceed! Check your extract to see the balance.")

        else:
            print("The operation has failed! The value entered is not valid.")

    elif chosen_option == "w":
        
        value = float(input("Digit the withdraw value:"))

        balance_exceeded = value > balance

        limit_exceeded = value > balance_limit

        withdraw_exceeded = withdraw_quantity >= WITHDRAW_LIMIT
        
        if balance_exceeded:
            print("The operation has failed! Your balance is not enought to proceed.")

        elif limit_exceeded:
            print("The operation has failed! The value you are trying to withdraw exceeds the daily limit. Try another value.")

        elif withdraw_exceeded:
            print("The operation has failed! You have reached the limit of withdraws per day. Try again later")

        elif value > 0:
            balance -=value
            extract += f"Withdraw: ${value:.2f}\n"
            withdraw_quantity += 1

            print("The operation has suceed! Check your extract to see the balance.")

        else:
            print("The operation has failed! The value entered is not valid.")

    elif chosen_option == "e":
        print(("\n================ EXTRATO ================"))
        print("No movimentations have been done on this account." if not extract else extract)
        print(f"\nFinal balance: R$ {balance:.2f}")
        print("==========================================")

    elif chosen_option == "r":
        print("You sucessfully finished your session.")
        break

    else:
        print("Invalid operation. Please, select a valid option on the menu")