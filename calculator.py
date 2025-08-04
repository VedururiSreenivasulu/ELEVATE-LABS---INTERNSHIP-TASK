def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zero."
    return a / b
def calculator():
    print("Welcome to Command-Line Calculator!")
    while True:
        print("Choose an operation:")
        print("1.Addition (+)")
        print("2.Subtraction (-)")
        print("3.Multiplication (*)")
        print("4.Divide (/)")
        print("5.Exit")
        choice=input("Enter your choice (1-5): ")
        if choice=='5':
            print("Exiting calculator")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice.")
            continue
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        if choice=='1':
            result=add(num1,num2)
        elif choice=='2':
            result=subtract(num1,num2)
        elif choice=='3':
            result=multiply(num1,num2)
        elif choice=='4':
            result=divide(num1,num2)
        print(f"Result: {result}")
calculator()
