class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(2, 3))
    print(calculator.subtract(10, 4))
    print(calculator.multiply(6, 7))
    print(calculator.divide(20, 5))
