# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("===== Simple Calculator =====")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'exit': ").strip()

        if choice.lower() == "exit":
            print("Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("Invalid operation. Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue

        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
