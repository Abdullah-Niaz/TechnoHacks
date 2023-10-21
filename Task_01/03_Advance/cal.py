class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            self.result = "Cannot divide by zero"
        else:
            self.result = x / y

    def evaluate_expression(self, expression):
        try:
            self.result = eval(expression)
        except:
            self.result = "Invalid Expression"

    def get_result(self):
        return self.result


def main():
    while True:
        print("======Calculator (OOP)======")
        # Constructor Invoked Here.
        calculator = Calculator()
        print("Select Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Custom Expression")
        print("6. Exit")

        choice = input("Enter the operation number: ")
        if  (choice == '6'):
            break;
        if choice in ('1', '2', '3', '4'):
            val1 = float(input("Enter the first value: "))
            val2 = float(input("Enter the second value: "))
            
            if (choice == '1'):
                calculator.add(val1, val2)
            elif (choice == '2'):
                calculator.subtract(val1, val2)
            elif (choice == '3'):
                calculator.multiply(val1, val2)

            elif (choice == '4'):
                calculator.divide(val1, val2)
            print("Result:", calculator.get_result())

        if (choice == '5'):
            custom_expr = input("Enter a custom expression: ")
            calculator.evaluate_expression(custom_expr)
            print("Result:", calculator.get_result())
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    main()
