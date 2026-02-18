#simple ATM machine

# pin=0000
#balance = 5000
#uer enters the pin
#has to validate whether the pin is correct and proceed
#if pin is correct show the menu
#1 check balance
#2 Deposit money
#3 withdraw money- check available balance when withdrawing,if balance is less restrict
#4 exit
#user should be able to perform these activities until he decided to exit the program
import time

import time

# Set predefined PIN and initial balance
correct_pin = "0000"
balance = 5000.0
attempts = 0

# --- PIN Validation ---
while attempts < 3:
    entered_pin = str(input("Please enter your PIN: "))

    if entered_pin == correct_pin:
        print("✅ PIN accepted. Login successful!")
        break
    else:
        attempts += 1
        print(f" Incorrect PIN. Attempts left: {3 - attempts}")

        if attempts == 3:
            print(" Too many incorrect attempts. Exiting the system.")
            exit()

# --- Main Banking Menu ---
while True:
    print("""
    ----------- MENU -----------
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit Account
    -----------------------------
    """)

    choice = input("Please enter a menu number (1-4): ")

    if choice == "1":
        print(f" Your current balance is: Rs.{balance}")
        time.sleep(3)

    elif choice == "2":
            deposit_amount = float(input("Enter amount to deposit: Rs."))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f" Rs.{deposit_amount} deposited successfully.")
                time.sleep(3)
                print(f"Updated balance: Rs.{balance}")
                time.sleep(3)
            else:
                print(" Deposit amount must be greater than zero.")
                time.sleep(3)

    elif choice == "3":
            withdraw_amount = float(input("Enter amount to withdraw: Rs."))
            if 0 < withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f" Rs.{withdraw_amount} withdrawn successfully.")
                time.sleep(3)
                print(f"Remaining balance: Rs.{balance}")
                time.sleep(3)
            else:
                print(" Insufficient funds or invalid amount.")
                time.sleep(3)


    elif choice == "4":
        print("👋 Thank you for banking with us. Goodbye!")
        break

    else:
        print(" Invalid menu choice. Please select between 1 and 4.")
        time.sleep(3)






