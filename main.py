# main.py
from app.calculator import Calculator

def display_menu():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Root")
    print("7. Show History")
    print("8. Clear History")
    print("9. Save History")
    print("10. Load History")
    print("11. Exit")

def get_operation_choice():
    try:
        choice = int(input("Select an operation (1-11): "))
        if choice not in range(1, 12):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice. Please select a number between 1 and 11.")
        return get_operation_choice()

def get_operands():
    try:
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_operands()

def main():
    calculator = Calculator()

    while True:
        display_menu()
        choice = get_operation_choice()

        if choice in [1, 2, 3, 4, 5, 6]:
            operation_map = {
                1: "add",
                2: "subtract",
                3: "multiply",
                4: "divide",
                5: "power",
                6: "root"
            }
            operation = operation_map[choice]
            a, b = get_operands()
            try:
                result = calculator.execute(operation, a, b)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == 7:  # Show History
            if calculator.history:
                for entry in calculator.history:
                    print(f"{entry['operation']}({entry['operands'][0]}, {entry['operands'][1]}) = {entry['result']}")
            else:
                print("No history available.")
        
        elif choice == 8:  # Clear History
            calculator.history = []
            print("History cleared.")
        
        elif choice == 9:  # Save History
            calculator.save_history()
            print("History saved successfully.")
        
        elif choice == 10:  # Load History
            calculator.load_history()
            print("History loaded successfully.")
        
        elif choice == 11:  # Exit
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
