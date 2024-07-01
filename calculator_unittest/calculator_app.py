class Calculations:
    """
    A class to perform basic arithmetic calculations.

    Attributes:
        a (float): The first operand.
        b (float): The second operand.
    """
    
    def __init__(self, a, b):
        """
        Initializes the Calculations with two operands (both positive and/or negative integer and/or float).
        
        Args:
            a (float): The first operand.
            b (float): The second operand.
        """
        self.a = a
        self.b = b

    def get_sum(self):
        """
        Returns the sum of the two operands.
        
        Returns:
            float: The sum of a and b.
        """
        return self.a + self.b

    def get_difference(self):
        """
        Returns the difference between the two operands.
        
        Returns:
            float: The difference between a and b.
        """
        return self.a - self.b

    def get_product(self):
        """
        Returns the product of the two operands.
        
        Returns:
            float: The product of a and b.
        """
        return self.a * self.b

    def get_quotient(self):
        """
        Returns the quotient of the two operands.
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ValueError: If the second operand b is zero.
        """
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

def get_valid_operand(prompt):
    """
    Prompts the user to enter a valid floating-point number.
    
    Args:
        prompt (str): The input prompt for the user.
        
    Returns:
        float: The validated floating-point number.
    """
    while True:
        try:
            operand = float(input(prompt))
            return operand
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    The main function to run the calculator app, providing a menu for the user to select operations.
    """
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