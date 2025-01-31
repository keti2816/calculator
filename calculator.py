def calculator():
    while True:
        try:
            numb1 = float(input('Enter first number: '))
            numb2 = float(input('Enter second number: '))

            print("choose which operation would you like to perform"
                  "\n 1-Addition"
                  "\n 2-Subtraction"
                  "\n 3-Multiplication"
                  "\n 4-Division"
                  "\n 5-exit")

            choice = int(input("Enter your choice (1-5) : "))

            if choice == 1:
                print(f"{numb1} + {numb2} = {numb1 + numb2}")
            elif choice == 2:
                print(f"{numb1} - {numb2} = {numb1 - numb2}")
            elif choice == 3:
                print(f"{numb1} * {numb2} = {numb1 * numb2}")
            elif choice == 4:
                print(f"{numb1} / {numb2} = {numb1 / numb2}")
            elif choice == 5:
                break
            else:
                print("invalid choice, please try again")
                continue
        except:
            print("please enter a valid number")

calculator()
