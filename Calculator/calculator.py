while True:
    print("select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    
    choice = input("Enter ur choice:")
    if choice =="6":
        print("Exiting a calculator .... gamashamnida, Annyeonghi gaseyo!..")
        break
    if choice not in['1', '2', '3', '4','5','6']:
        print("Invalid choice ! please enter the choice between (1-6)")
    try:
        num1=float(input("Enter ur first number:"))
        num2=float(input("Enter ur second number:"))
    except ValueError:
        print("Invalid input! Please enter numeric value")
        continue
        
    if choice == "1":
        
    
        print("Addition of number:" , num1 + num2)
    elif  choice == "2":
        
        print(f"Subtraction of {num2} from {num1}:" , num1 - num2)
    elif choice == "3":
        
        print("Multiolication of number:" , num1 * num2)
    elif choice == "4":
        
        print("Division of number:" , num1 / num2)
    elif choice == "5":
       
        print("Modulus of number:" , num1 % num2)
   
    
              
