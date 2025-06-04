# ATM Machine Simulation in Python

# Dummy user data
user_pin = "5005"
user_balance = 1000000.00

def atm():
    print("Welcome to the ATM Machine Simulation!")
    attempts = 0
    
    # PIN Authentication
    while attempts < 3:
        entered_pin = input("Please enter your 4-digit PIN: ")
        if entered_pin == user_pin:
            print("\nPIN accepted.\n")
            main_menu()
            return
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts left: {3 - attempts}")
    
    print("\nToo many incorrect attempts. Your account is locked.")

def main_menu():
    global user_balance
    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            print(f"\nYour current balance is: ${user_balance:.2f}")
        
        elif choice == '2':
            deposit = input("Enter amount to deposit: $")
            try:
                deposit = float(deposit)
                if deposit <= 0:
                    print("Deposit amount must be positive.")
                else:
                    user_balance += deposit
                    print(f"Deposit successful. New balance: ${user_balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == '3':
            withdraw = input("Enter amount to withdraw: $")
            try:
                withdraw = float(withdraw)
                if withdraw <= 0:
                    print("Withdrawal amount must be positive.")
                elif withdraw > user_balance:
                    print("Insufficient funds.")
                else:
                    user_balance -= withdraw
                    print(f"Withdrawal successful. New balance: ${user_balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == '4':
            print("\nThank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select an option (1-4).")

# Run the ATM simulation
atm()
