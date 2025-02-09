def calculator():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    try:
        choice = input("Enter choice 1/2/3/4: ")
        numa = float(input("Enter 1st number: "))
        numb = float(input("Enter 2nd number: "))
        if choice == '1':
            result = numa + numb
            operation = "+"

        elif choice == '2':
            result = numa - numb
            operation = "-"

        elif choice == '3':
            result = numa * numb
            operation = "*"

        elif choice == '4':
            if numb == 0:
                print("Division by zero is not allowed.")
                return
            result = numa / numb
            operation = "/"

        else:
            print("Wrong choice")
            return

        print(f"{numa} {operation} {numb} = {result}")

    except ValueError:
        print("Invalid input!")

calculator()