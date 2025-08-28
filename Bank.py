balance = 100000
pin=1804

for attempt in range(3):
    pin_entered = int(input("Enter You Pin: "))
    if pin_entered == pin:
        print("Login Success.\n")
        print("Welcome To Bank Of Dholakpur")
        while True:
            print("1.Deposite\n2.Withdraw\n3.Check Balance\n4.Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                amount = int(input("Enter Amount To Deposite: "))
                balance += amount
                print("Amount Deposited")

            elif choice == 2:
                amount = int(input("Enter Amount To Withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print("Amount Withdrawn")
                else:
                    print("Insufficient Balance!")

            elif choice == 3:
                print("Your Balance Is:", balance)

            elif choice == 4:
                print("Thank You For Banking With Us!")
                exit()

            else:
                print("invalid Choice!")
        break
    else:
        print("Wrong Try Again")
else:
    print("Too Many Try")

             

