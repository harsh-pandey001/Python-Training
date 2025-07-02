def multiplication(a, b):
    return a*b

def addtion(a, b):
    return a+b

def division(a,b):
    return a/b

def substraction(a,b):
    return a-b
    

while True:
    print("\n1. Multiply")
    print("2. Add")
    print("3. Divide")
    print("4. Subtract")
    print("5. Exit")
    operation = int(input("\nEnter Your choice :- "))

    if operation == 5 :
        break

    print("Okay, So the Your choice is ", operation)
    a = int(input("\nEnter first number\n"))
    b = int(input("\nEnter Second number\n"))

    if operation == 3 and b >= 0:
        print("\nCan't be divisible by 0")
        break

    if operation == 1:
        print("So the result : ", multiplication(a, b), "\n")
    elif operation == 2:
        print("\n", end="")
        print("So the result : ", addtion(a, b), "\n")
    elif operation == 3:
        print("\n", end="")
        print("So the result : ", division(a, b), "\n")
    elif operation == 4:
        print("\n", end="")
        print("So the result : ", substraction(a, b), "\n")
    else:
        print("\nInvalid Input\n")

# Match statements require Python 3.10
    # match operation:
    #     case 1:
    #         multiplication(a,b)
    #     case 2: 
    #         addtion(a,b)
    #     case 3: 
    #         division(a,b)
    #     case 4:
    #         substraction(a,b)
    #     case _: 
    #         print("Invalid Input")
   


