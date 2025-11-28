balance = 70000
pin = 170200
attempts = 0

while attempts < 3:
    user_pin = input("Enter your PIN: ")

    if not user_pin.isdigit():
        print("PIN must be a number!")
        attempts += 1
        print(f"Attempts left: {3 - attempts}")
        continue     # go to next attempt

    user_pin = int(user_pin)

    if user_pin == pin:
        print("PIN verified successfully!")
        print("\nSelect operation")
        print("1. Amount Deposit")
        print("2. Amount Withdrawal")

        choice = input("Enter your operation (1 or 2): ")

        if choice not in ["1", "2"]:
            print("Invalid choice!")
            break

        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("Invalid input! Please enter amount in numerals.")
            break

        if choice == "2":  
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "1":  
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance:", balance)

        break  

    else:
        attempts += 1
        print("Incorrect PIN!")
        print(f"Attempts left: {3 - attempts}")

        if attempts == 3:
            print("Your ATM access is BLOCKED after 3 invalid attempts.")
