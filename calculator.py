def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "[WARN] Cannot divide by zero."
    return f"{a} / {b} = {a / b}"

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def main():
    history = []
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Power", power),
        "6": ("Modulus", modulus),
    }

    while True:
        print("\n--- CLI Calculator ---")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("7. View History")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()
        if choice == "8":
            print("Exiting calculator.")
            break
        if choice == "7":
            print("\n--- Calculation History ---")
            print("\n".join(history) if history else "No calculations yet.")
            continue
        if choice not in operations:
            print("Invalid selection. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        op_name, func = operations[choice]
        result = func(num1, num2)
        record = f"{op_name}({num1}, {num2}) = {result}"
        history.append(record)
        print("Result:", result)

if __name__ == "__main__":
    main()
