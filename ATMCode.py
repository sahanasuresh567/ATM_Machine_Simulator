balance = 98765
print("=======================================")
print("      WELCOME TO CYBER ATM SYSTEM      ")
print("=======================================")
while True:
    print("\n---------------------------------------")
    print("           CYBER ATM MENU              ")
    print("---------------------------------------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit ATM")
    print("---------------------------------------")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue
    if choice == 1:
        print("\nProcessing your request...")
        print("Fetching account details...")
        print("---------------------------------------")
        print("Your Current Balance = Rs.", balance)
        print("---------------------------------------")
        print("Thank you for checking your balance!")
    elif choice == 2:
        print("\nDEPOSIT SECTION")
        amount = float(input("Enter deposit amount: Rs. "))
        if amount > 0:
            print("Please wait... Depositing amount")
            balance = balance + amount
            print("Amount of Rs.", amount, "has been deposited successfully!")
            print("Updated Balance = Rs.", balance)
        else:
            print("Invalid amount! Deposit amount must be positive.")
    elif choice == 3:
        print("\nWITHDRAW SECTION")
        amount = float(input("Enter withdraw amount: Rs. "))
        if amount <= 0:
            print("Invalid amount! Withdrawal amount must be positive.")
        elif amount <= balance:
            print("Checking balance availability...")
            balance = balance - amount
            print("Transaction approved!")
            print("Please collect your cash of Rs.", amount)
            print("Remaining Balance = Rs.", balance)
        else:
            print("Transaction failed!")
            print("Insufficient balance in your account.")
            print("Your available balance is only Rs.", balance)

    elif choice == 4:
        print("\nThank you for using CYBER ATM SERVICES")
        print("Your final account balance is Rs.", balance)
        print("Have a nice day!")
        print("=======================================")
        break
    else:
        print("Invalid choice! Please select a valid option from 1 to 4.")
print("\nSystem shutting down...")
print("Goodbye!")














