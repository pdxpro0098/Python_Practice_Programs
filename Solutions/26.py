while (1):
    print("Simple calculator")
    print("1.) Add")
    print("2.) Sub")
    print("3.) Mul")
    print("4.) Div")
    print("5.) exit")
    INPUT = int(input("Enter choice: "))
    if 0 < INPUT < 6:
        match INPUT:
            case 1:
                print("Add")
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter Second number: "))
                print(num1 + num2)
            case 2:
                print("Sub")
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter Second number: "))
                print(num1 - num2)
            case 3:
                print("Mul")
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print(num1 * num2)
            case 4:
                print("Div")
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print(num1 / num2)
            case 5:
                print("Exiting")
                exit()
    else:
        print("Enter valid choice")
