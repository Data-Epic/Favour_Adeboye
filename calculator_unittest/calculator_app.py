class Calculations:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

def get_valid_operand(prompt):
    while True:
        try:
            operand = float(input(prompt))
            return operand
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4']:
            a = get_valid_operand("Enter the first operand: ")
            b = get_valid_operand("Enter the second operand: ")

            calc = Calculations(a, b)

            operations = {
                '1': calc.get_sum,
                '2': calc.get_difference,
                '3': calc.get_product,
                '4': calc.get_quotient
            }

            try:
                result = operations[choice]()
                print(f"The result is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            print("Exiting the calculator app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()